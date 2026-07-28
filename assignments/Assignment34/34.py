import sys
import os
import psutil
import smtplib
from email.message import EmailMessage
from datetime import datetime


# -------------------------------------------------------------------
# Get Process Information
# -------------------------------------------------------------------

def get_process_info(process_name=None):
    """Get information about running processes."""

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "username"]
    ):
        try:
            info = process.info

            name = info["name"]

            if process_name is None or (
                name and name.lower() == process_name.lower()
            ):
                processes.append({
                    "name": name or "N/A",
                    "pid": info["pid"],
                    "username": info["username"] or "N/A"
                })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return processes


# -------------------------------------------------------------------
# Display Processes
# -------------------------------------------------------------------

def display_processes(processes):
    """Display process information on the screen."""

    if not processes:
        print("No process found.")
        return

    print("-" * 80)
    print(
        f"{'PROCESS NAME':30} "
        f"{'PID':10} "
        f"{'USERNAME'}"
    )
    print("-" * 80)

    for process in processes:
        print(
            f"{process['name'][:30]:30} "
            f"{process['pid']:<10} "
            f"{process['username']}"
        )

    print("-" * 80)


# -------------------------------------------------------------------
# Create Log File
# -------------------------------------------------------------------

def create_log(directory, processes):
    """Create a process information log file."""

    # Create directory if it does not exist
    os.makedirs(directory, exist_ok=True)

    # Make sure the path is a directory
    if not os.path.isdir(directory):
        raise ValueError(
            "The specified path is not a directory."
        )

    filename = (
        "ProcessInfo_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".log"
    )

    filepath = os.path.join(
        directory,
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Running Process Information\n"
        )

        file.write(
            "=" * 80 + "\n"
        )

        file.write(
            f"{'PROCESS NAME':30} "
            f"{'PID':10} "
            f"{'USERNAME'}\n"
        )

        file.write(
            "=" * 80 + "\n"
        )

        for process in processes:

            file.write(
                f"{process['name'][:30]:30} "
                f"{process['pid']:<10} "
                f"{process['username']}\n"
            )

    return filepath


# -------------------------------------------------------------------
# Validate Email
# -------------------------------------------------------------------

def is_valid_email(email):
    """Perform basic email validation."""

    if not email:
        return False

    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    username, domain = parts

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True


# -------------------------------------------------------------------
# Send Email
# -------------------------------------------------------------------

def send_email(
    sender_email,
    app_password,
    receiver_email,
    log_file
):
    """Send the process information log through Gmail."""

    try:

        message = EmailMessage()

        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = (
            "Running Process Information"
        )

        message.set_content(
            "Hello,\n\n"
            "Please find attached the running "
            "process information log file.\n\n"
            "Regards,\n"
            "Python Automation"
        )

        # Read log file
        with open(
            log_file,
            "rb"
        ) as file:

            file_data = file.read()

        # Attach log file
        message.add_attachment(
            file_data,
            maintype="text",
            subtype="plain",
            filename=os.path.basename(log_file)
        )

        print(
            "Connecting to Gmail SMTP server..."
        )

        # Gmail SMTP SSL connection
        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as server:

            print(
                "Logging into Gmail..."
            )

            server.login(
                sender_email,
                app_password
            )

            print(
                "Sending email..."
            )

            server.send_message(
                message
            )

        print(
            "Email sent successfully!"
        )

        return True

    except smtplib.SMTPAuthenticationError as e:

        print(
            "Gmail authentication failed."
        )

        print(
            "Check your Gmail address and "
            "Google App Password."
        )

        print(
            "Details:",
            e
        )

        return False

    except smtplib.SMTPException as e:

        print(
            "SMTP error occurred:"
        )

        print(
            e
        )

        return False

    except FileNotFoundError:

        print(
            "Log file could not be found."
        )

        return False

    except Exception as e:

        print(
            "Email error:"
        )

        print(
            e
        )

        return False


# -------------------------------------------------------------------
# Show Help
# -------------------------------------------------------------------

def show_help():
    """Display program usage information."""

    print()
    print(
        "Process Information Automation"
    )
    print(
        "=" * 40
    )

    print()
    print("Usage:")
    print()

    print(
        "1. Display all running processes:"
    )

    print(
        "   python ProcInfo.py"
    )

    print()

    print(
        "2. Search for a particular process:"
    )

    print(
        "   python ProcInfo.py notepad.exe"
    )

    print()

    print(
        "3. Create log and send it by email:"
    )

    print(
        '   python ProcInfo.py "C:\\ProcessLogs" receiver@gmail.com'
    )

    print()

    print(
        "Options:"
    )

    print(
        "   -h, --help"
    )

    print(
        "       Display this help message."
    )

    print()

    print(
        "Email credentials:"
    )

    print(
        "   SENDER_EMAIL"
    )

    print(
        "   EMAIL_APP_PASSWORD"
    )

    print()

    print(
        "These should be configured as environment "
        "variables."
    )

    print()


# -------------------------------------------------------------------
# Main Function
# -------------------------------------------------------------------

def main():

    try:

        # -----------------------------------------------------------
        # Help
        # -----------------------------------------------------------

        if len(sys.argv) == 2:

            if sys.argv[1] in (
                "-h",
                "--help"
            ):

                show_help()
                return

        # -----------------------------------------------------------
        # 1. No arguments
        # Display all running processes
        # -----------------------------------------------------------

        if len(sys.argv) == 1:

            processes = get_process_info()

            display_processes(
                processes
            )

            return

        # -----------------------------------------------------------
        # 2. One argument
        # Search particular process
        # -----------------------------------------------------------

        elif len(sys.argv) == 2:

            process_name = sys.argv[1]

            if process_name.strip() == "":
                print(
                    "Process name cannot be empty."
                )
                return

            processes = get_process_info(
                process_name
            )

            if processes:

                display_processes(
                    processes
                )

            else:

                print(
                    f"{process_name} is not running."
                )

            return

        # -----------------------------------------------------------
        # 3. Two arguments
        # Create log and send email
        # -----------------------------------------------------------

        elif len(sys.argv) == 3:

            directory = sys.argv[1]
            receiver_email = sys.argv[2]

            # Validate directory argument
            if directory.strip() == "":
                print(
                    "Directory cannot be empty."
                )
                return

            # Validate receiver email
            if not is_valid_email(
                receiver_email
            ):
                print(
                    "Invalid receiver email address."
                )
                return

            # -------------------------------------------------------
            # Get all running processes
            # -------------------------------------------------------

            processes = get_process_info()

            if not processes:

                print(
                    "No running processes found."
                )

                return

            # -------------------------------------------------------
            # Create log file
            # -------------------------------------------------------

            log_file = create_log(
                directory,
                processes
            )

            print()
            print(
                "Log file created successfully:"
            )

            print(
                log_file
            )

            # -------------------------------------------------------
            # Get Gmail credentials
            # -------------------------------------------------------

            sender_email = os.environ.get(
                "SENDER_EMAIL"
            )

            app_password = os.environ.get(
                "EMAIL_APP_PASSWORD"
            )

            if not sender_email:

                print()
                print(
                    "SENDER_EMAIL environment variable "
                    "is not configured."
                )

                return

            if not app_password:

                print()
                print(
                    "EMAIL_APP_PASSWORD environment variable "
                    "is not configured."
                )

                return

            # Validate sender email
            if not is_valid_email(
                sender_email
            ):

                print(
                    "Invalid sender email address."
                )

                return

            # -------------------------------------------------------
            # Send email
            # -------------------------------------------------------

            email_sent = send_email(
                sender_email,
                app_password,
                receiver_email,
                log_file
            )

            # -------------------------------------------------------
            # Check email result
            # -------------------------------------------------------

            if email_sent:

                print()
                print(
                    "Log file sent successfully."
                )

            else:

                print()
                print(
                    "Log file was created, "
                    "but email could not be sent."
                )

            return

        # -----------------------------------------------------------
        # Invalid arguments
        # -----------------------------------------------------------

        else:

            print(
                "Invalid arguments."
            )

            print(
                "Use --help for help."
            )

            return

    # ---------------------------------------------------------------
    # Exception Handling
    # ---------------------------------------------------------------

    except psutil.Error as e:

        print(
            "Process error:",
            e
        )

    except PermissionError:

        print(
            "Permission denied."
        )

    except FileNotFoundError:

        print(
            "File or directory not found."
        )

    except ValueError as e:

        print(
            "Error:",
            e
        )

    except Exception as e:

        print(
            "Unexpected error:",
            e
        )


# -------------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------------

if __name__ == "__main__":
    main()