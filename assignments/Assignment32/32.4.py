import shutil
import os
import time
import schedule

source = input("Enter Source Directory: ").strip()
destination = input("Enter Destination Directory: ").strip()


def task():
    if not os.path.isdir(source):
        print("Invalid Source Directory...")
        return

    if not os.path.isdir(destination):
        print("Invalid Destination Directory...")
        return

    with open("Copy.txt", "a") as fobj:
        for file in os.listdir(source):
            if file.endswith(".txt"):
                src = os.path.join(source, file)
                dest = os.path.join(destination, file)

                try:
                    shutil.copy2(src, dest)
                    print(f"{file} copied successfully.")
                    fobj.write(f"{file} copied.\n")
                except Exception as e:
                    print(f"{file} not copied: {e}")
                    fobj.write(f"{file} not copied: {e}\n")


def main():
    print("Waiting for contents to be copied...")
    schedule.every(1).minutes.do(task)
    task()  

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()



# OUTPUT
# Enter Source Directory: C:\Users\admin\OneDrive\Desktop\Source
# Enter Destination Directory: C:\Users\admin\OneDrive\Desktop\destination
# Waiting for contents to be copied...
# basic.txt.txt copied successfully.
# info.txt copied successfully.    