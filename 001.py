def add_task(task):
    todolist.append(task)
    return todolist

def remove_task(task):
    todolist.remove(task)
    return todolist

def show_list(todolist):
    if not todolist:
        print("Your ToDoList is empty, do what you want!")
    else:
        print(f"In you ToDoList are following tasks:")
        for n, task in enumerate(todolist, 1):
            print(f"{n} : {task["name"]}; {task["date"]}; {task["duration"]}")
    
    
todolist = []

while True:
    try:
        v1 = int(input("What you want to do? Write 1 to add task, 2 to delete task, 3 to print the list or 4 to exit:\n"))
    except ValueError:
        print("Enter a valid number")
        continue
    
    if v1 == 1:
        task_name = input("Write task name to add...\n")
        task_date = input("Write due date of this task...\n")
        task_duration = input("Write task duration...\n")
        task = {"name" : task_name, "date" : task_date, "duration" : task_duration}
        if task in todolist:
            print("This task is in To Do List already.")
        else:
            add_task(task)



    elif v1 == 2:
        task_name = input("Write task name to delete...\n")
        task_date = input("Write due date of this task...\n")
        task_duration = input("Write task duration...\n")
        task = {"name" : task_name, "date" : task_date, "duration" : task_duration}
        if task not in todolist:
            print("This task is not in To Do List.")
        else:
            remove_task(task)
    elif v1 == 3:
        show_list(todolist)
    elif v1 == 4:
        break
    else:
        print("Enter a valid number")






