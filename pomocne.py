def remove_task(task):
    todolist.remove(task)
    return todolist

todolist = [{"name" : "shopping", "date" : "3/5/25", "duration" : "30min"}, 
            {"name" : "run", "date" : "3/5/25", "duration" : "60min"}, 
            {"name" : "cook", "date" : "3/5/25", "duration" : "40min"},
            {"name" : "run", "date" : "3/5/25", "duration" : "30min"} ]
for n, task in enumerate(todolist, 1):
    print(f"{n} : {task["name"]}")

task_name = input("Write task name to delete...\n")
if sum(1 for task in todolist if task["name"] == task_name) == 1:
    for task in todolist:
        if task["name"] == task_name:
            todolist.remove(task)
elif sum(1 for task in todolist if task["name"] == task_name) > 1:
    task_date = input("Write task due date...\n")
    for task in todolist:
        if sum(1 for task in todolist if task["name"] == task_name and task["date"] == task_date) == 1:
            todolist.remove(task)
        elif sum(1 for task in todolist if task["name"] == task_name and task["date"] == task_date) > 1:
            task_duration = input("Write task duration...\n")
            todolist.remove(task)
               

