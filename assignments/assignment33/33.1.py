import os
import sys
import time
import hashlib
import smtplib
from datetime import datetime
from email.message import EmailMessage


# -------------------------------------------------------------------
# Calculate Checksum
# -------------------------------------------------------------------

def calculate_checksum(file_name):
  

    hash_object = hashlib.md5()

    try:
        with open(file_name, "rb") as file_obj:
            while True:
                buffer = file_obj.read(1024 * 1024)  # Read 1 MB at a time

                if not buffer:
                    break

                hash_object.update(buffer)

        return hash_object.hexdigest()

    except Exception as e:
        print(f"Error calculating checksum for {file_name}: {e}")
        return None


# -------------------------------------------------------------------
# Find Duplicate Files
# -------------------------------------------------------------------

def find_duplicate_files(directory_name):
    """Find duplicate files using their SHA-256 checksum."""

    if not os.path.exists(directory_name):
        return {}

    if not os.path.isdir(directory_name):
        return {}

    duplicate = {}

    for folder_name, sub_folders, file_names in os.walk(directory_name):

        for file_name in file_names:

            file_path = os.path.join(folder_name, file_name)

            try:
                checksum = calculate_checksum(file_path)

                if checksum is None:
                    continue

                if checksum in duplicate:
                    duplicate[checksum].append(file_path)

                else:
                    duplicate[checksum] = [file_path]

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return duplicate


# -------------------------------------------------------------------
# Delete Duplicate Files
# -------------------------------------------------------------------

def delete_duplicate_files(directory_name, log):
  

    my_dict = find_duplicate_files(directory_name)

    # Keep only checksum groups containing duplicates
    result = [
        file_list
        for file_list in my_dict.values()
        if len(file_list) > 1
    ]

    total_files = sum(
        len(value)
        for value in my_dict.values()
    )

    total_duplicate = 0
    total_deleted = 0

    for file_list in result:

        # First file is considered original
        original = file_list[0]

        log.write(
            f"Original Kept: {original}\n"
        )

        # Delete remaining duplicate files
        for duplicate_file in file_list[1:]:

            total_duplicate += 1

            try:

                if os.path.exists(duplicate_file):

                    os.remove(duplicate_file)

                    total_deleted += 1

                    log.write(
                        f"Deleted Duplicate: {duplicate_file}\n"
                    )

            except Exception as e:

                log.write(
                    f"Error deleting {duplicate_file}: {e}\n"
                )

    return (
        total_files,
        total_duplicate,
        total_deleted
    )


# -------------------------------------------------------------------
# Send Email
# -------------------------------------------------------------------

def send_email(
    receiver,
    log_file,
    start_time,
    end_time,
    directory,
    total_files,
    total_duplicate,
    total_deleted
):
    """Send duplicate-removal report through Gmail."""

    # Environment variable names
    sender = os.environ.get("SENDER_EMAIL")
    password = os.environ.get("EMAIL_PASSWORD")

    if sender is None or password is None:

        return (
            "Email credentials not configured."
        )

    message = EmailMessage()

    message["Subject"] = (
        "Duplicate File Removal Report"
    )

    message["From"] = sender
    message["To"] = receiver

    body = f"""
Duplicate File Removal Automation Completed

Starting Time       : {start_time}
Completion Time     : {end_time}
Directory Scanned   : {directory}

Total Files Scanned : {total_files}
Duplicate Files     : {total_duplicate}
Files Deleted       : {total_deleted}

Please find the detailed log file attached.
"""

    message.set_content(body)

    try:

        # Attach log file
        with open(log_file, "rb") as file_obj:

            message.add_attachment(
                file_obj.read(),
                maintype="text",
                subtype="plain",
                filename=os.path.basename(log_file)
            )

        # Connect to Gmail SMTP server
        with smtplib.SMTP(
            "smtp.gmail.com",
            587
        ) as server:

            server.starttls()

            server.login(
                sender,
                password
            )

            server.send_message(message)

        return "Email sent successfully."

    except Exception as e:

        return f"Email Error: {e}"


# -------------------------------------------------------------------
# Main Automation
# -------------------------------------------------------------------

def start_automation(
    directory_name,
    interval,
    receiver_email
):
    

    os.makedirs(
        "Testing",
        exist_ok=True
    )

    while True:

        start_time = datetime.now()

        log_file = os.path.join(
            "Testing",
            f"DuplicateRemovalLog_"
            f"{start_time.strftime('%d-%m-%Y-%H-%M-%S')}.log"
        )

        # -----------------------------------------------------------
        # Create log
        # -----------------------------------------------------------

        with open(
            log_file,
            "w",
            encoding="utf-8"
        ) as log:

            log.write(
                "Duplicate File Removal Automation\n"
            )

            log.write(
                "=" * 60 + "\n"
            )

            log.write(
                f"Starting time of scanning: "
                f"{start_time}\n"
            )

            log.write(
                f"Directory scanned: "
                f"{directory_name}\n\n"
            )

            # -------------------------------------------------------
            # Find and delete duplicates
            # -------------------------------------------------------

            (
                total_files,
                total_duplicate,
                total_deleted
            ) = delete_duplicate_files(
                directory_name,
                log
            )

            end_time = datetime.now()

            log.write("\n")

            log.write(
                f"Total number of files scanned: "
                f"{total_files}\n"
            )

            log.write(
                f"Total number of duplicate files found: "
                f"{total_duplicate}\n"
            )

            log.write(
                f"Total number of duplicate files deleted: "
                f"{total_deleted}\n"
            )

            log.write(
                f"Completion time of scanning: "
                f"{end_time}\n"
            )

        # -----------------------------------------------------------
        # Send email
        # -----------------------------------------------------------

        email_status = send_email(
            receiver_email,
            log_file,
            start_time,
            end_time,
            directory_name,
            total_files,
            total_duplicate,
            total_deleted
        )

        # Add email status to log
        with open(
            log_file,
            "a",
            encoding="utf-8"
        ) as log:

            log.write(
                f"Email delivery status: "
                f"{email_status}\n"
            )

        print(
            f"\nScan completed at {end_time}"
        )

        print(
            f"Files scanned    : {total_files}"
        )

        print(
            f"Duplicates found : {total_duplicate}"
        )

        print(
            f"Files deleted    : {total_deleted}"
        )

        print(
            f"Email status     : {email_status}"
        )

        print(
            f"Next scan in {interval} minutes..."
        )

        # -----------------------------------------------------------
        # Wait before next scan
        # -----------------------------------------------------------

        time.sleep(
            interval * 60
        )


# -------------------------------------------------------------------
# Help
# -------------------------------------------------------------------

def show_help():

    print(
        """
Duplicate File Removal Automation

Usage:
    python DuplicateFileRemoval.py <DirectoryPath> <Interval> <ReceiverEmail>

Example:
    python DuplicateFileRemoval.py E:/Data/Demo 50 receiver@gmail.com

Arguments:
    DirectoryPath
        Absolute path of the directory to scan.

    Interval
        Time interval between scans in minutes.

    ReceiverEmail
        Email address where the report will be sent.

Options:
    -h, --help
        Show help.

    -u, --usage
        Show usage.
"""
    )


# -------------------------------------------------------------------
# Main Function
# -------------------------------------------------------------------

def main():

    # ---------------------------------------------------------------
    # Help
    # ---------------------------------------------------------------

    if len(sys.argv) == 2:

        if sys.argv[1] in ("-h", "--help"):

            show_help()
            return

        if sys.argv[1] in ("-u", "--usage"):

            print(
                "Usage:"
            )

            print(
                "python DuplicateFileRemoval.py "
                "<AbsoluteDirectoryPath> "
                "<TimeIntervalInMinutes> "
                "<ReceiverEmailAddress>"
            )

            return

    # ---------------------------------------------------------------
    # Check number of arguments
    # ---------------------------------------------------------------

    if len(sys.argv) != 4:

        print("Invalid arguments.")
        print("Use --help for help.")

        return

    directory_name = sys.argv[1]
    interval = sys.argv[2]
    receiver_email = sys.argv[3]

    # ---------------------------------------------------------------
    # Validate directory
    # ---------------------------------------------------------------

    if not os.path.isabs(directory_name):

        print(
            "Directory path must be absolute."
        )

        return

    if not os.path.exists(directory_name):

        print(
            "Path is invalid."
        )

        return

    if not os.path.isdir(directory_name):

        print(
            "Specified path is not a directory."
        )

        return

    # ---------------------------------------------------------------
    # Validate interval
    # ---------------------------------------------------------------

    try:

        interval = float(interval)

        if interval <= 0:

            print(
                "Interval must be greater than zero."
            )

            return

    except ValueError:

        print(
            "Interval must be numeric."
        )

        return

    # ---------------------------------------------------------------
    # Validate email
    # ---------------------------------------------------------------

    if (
        "@" not in receiver_email
        or "." not in receiver_email.split("@")[-1]
    ):

        print(
            "Invalid email address."
        )

        return

    # ---------------------------------------------------------------
    # Start automation
    # ---------------------------------------------------------------

    print(
        "Duplicate File Removal Automation Started..."
    )

    print(
        f"Directory : {directory_name}"
    )

    print(
        f"Interval  : {interval} minutes"
    )

    print(
        f"Receiver  : {receiver_email}"
    )

    start_automation(
        directory_name,
        interval,
        receiver_email
    )


# -------------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------------

if __name__ == "__main__":
    main()