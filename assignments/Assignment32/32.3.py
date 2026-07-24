import os
import time
import schedule

file = input("Enter File Name: ").strip()

def task():
    try:
        if not os.path.exists(file):
            print("File does not exist...")
        elif os.path.getsize(file) == 0:
            print("File is empty...")
        else:
            with open(file, "r") as fobj:
                print("\nContent of the file:")
                print(fobj.read())

    except PermissionError:
        print("Permission denied...")
    except Exception as e:
        print("Error:", e)

def main():
                                                 
    schedule.every(1).minutes.do(task)           # Run task every minute

  
    task()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()