tasks = []

while True:
    command = input("MANJULA TRANSACTION :  \nOptions: [add ] [view ] [remove ] [exit ]\nEnter command: ").strip().lower()

    if command == "add":
        tasks.append(input("Enter task: ").strip())
    elif command == "view":
        print("\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks)) or "No tasks available.")
    elif command == "remove":
        try:
            tasks.pop(int(input("ENGA TASK NUMBER KODU : ")) - 1)
        except (ValueError, IndexError):
            print("ERROR.")
    elif command == "exit":
        break
    else:
        print("VERA LEVEL NEE POOO...\nCommandayy thappu maaa....\nCorrect aanna command thattu...")
