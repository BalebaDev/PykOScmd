import subprocess


def show_active_tasks():
    subprocess.run(["tasklist"])


def kill_task():
    task_name = input("Enter the name of the task to kill: ")
    subprocess.run(["taskkill", "/F", "/IM", task_name])


def show_host_ip():
    subprocess.run(["ipconfig"])


def main():
    while True:
        command = input("Enter a command: ")
        if command == "ktoybilpistoletom":
            show_active_tasks()
        elif command == "ybilipistoletom":
            kill_task()
        elif command == "doxxer":
            show_host_ip()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
