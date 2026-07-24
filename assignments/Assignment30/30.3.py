# write a programto print coding kr after 30min
import time
import schedule


def display():
    print("Coding krr...")

def main():
    schedule.every(30).minutes.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()        



