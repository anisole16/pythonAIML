# delete empty file after hour


import schedule
import os
import time

source = input("Enter Folder path: ")


def delete_empty_files():
    current_time = time.time()

    for file in os.listdir(source):
        if file.endswith(".txt"):
            filepath = os.path.join(source, file)

            
            if os.path.getsize(filepath) == 0:
                file_age = current_time - os.path.getmtime(filepath)

                if file_age >= 3600:
                    try:
                        os.remove(filepath)
                        print(f"{file} deleted (empty and older than 1 hour).")
                    except Exception as e:
                        print(f"Could not delete {file}: {e}")

def main():
    print("Removing Unnecessary file....")
    schedule.every(1).hours.do(delete_empty_files)

    while True:

        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()        

