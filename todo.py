todo = []

# Task add kre
def taskadd(todo):
    task = input("Add your task : ")

    if task == "":
        print("Task cann't be empty.Please enter a task!!")
        return
    
    todo.append({
        "task": task,
        "done": False        # naya task = incomplete
    })

    print(f"Task {task} added 👍")

# Task print krwao
def taskprint(todo):
    if len(todo) == 0:
        print("There is no task, please add you task first!!")
        return
    
    print("\n ------ YOUR TASK ------")
    for i, item in enumerate(todo, 1):
        #done True hai ya False
        if item["done"] == True:
            status = "[DONE]"
        else:
            status = "[    ]"

        print(f"{i} . {status} {item["task"]}")

    print("--------------------------------")

#task complete mark karo
def taskdone(todo):
    taskprint(todo)        #pehle list dikhao

    if len(todo)==0:
        return
    
    while True:
        try:
            num = int(input("Which task complted? (number) : "))
            if 1 <= num <= len(todo):
                break 
            print("Enter correct number.")
        except ValueError:
            print("Only enter number!")

    #index = num - 1  (list 0 se start hoti hai)
    todo[num - 1]["done"] = True
    
    task_name = todo[num - 1]["task"]
    print("Complete mark ho gayi:", task_name)

#task delete kra
def deletetask(todo):
    taskprint(todo)

    if len(todo) == 0:
        return
    
    while True:
        try:
            num = int(input("Which task do you want to delete? (number): "))
            if 1 <= num <= len(todo):
                break
            print("Enter correct number.")
        except ValueError:
            print("Only enter number!")

    # Confirm karo — galti se delete na ho
    task_name = todo[num - 1]["task"]
    confirm = input(f"'{task_name}' delete karein? (y/n): ")

    if confirm.lower() == "y":
        todo.pop(num - 1)         # list se hata do
        print("Task delete ho gayi!")
    else:
        print("Delete cancel.")

def show_menu():
    print("--------------------------------------")
    print("       TO-DO APP — MENU")
    print("--------------------------------------")
    print("  1. Add new task")
    print("  2. Print all task")
    print("  3. Mark task completed")
    print("  4. Delete the task")
    print("  5. Quit")
    print("--------------------------------------")
 
 
def main():
    print("\n  WELCOME IN TO-DO APP !")
 
    while True:
        show_menu()
        choice = input("Enter your choice(1-5): ").strip()
 
        if choice == "1":
            taskadd(todo)
        elif choice == "2":
            taskprint(todo)
        elif choice == "3":
            taskdone(todo)
        elif choice == "4":
            deletetask(todo)
        elif choice == "5":
            break
        else:
            print("Wrong choice! Select between 1-5.")
 
 
# --- Program yahan se shuru hota hai ---
if __name__ == "__main__":
    main()   
    