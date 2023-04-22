# ToDo List

file_name = "data.txt"

def add_task():
    with open(file_name,"r") as f:
        count = f.read().count("\n")

    with open(file_name,"a") as f:
        task = input("Enter new task")
        f.write(str(count)+" "+task + "\n")

def print_tasks():
    with open(file_name,"r") as f:
        print(f.read())

def status():
    print_tasks()
    task = int(input("Enter task - "))
    status = int(input("Select status 1 - completed\n0 - nocompleted"))
    with open(file_name,"r") as f:
        tasks = f.read().split("\n")

    if status == 1:
        tasks[task] += " completed"
    elif status == 0:
        tasks[task] += " nocompleted"
    else:
        print("nocoman")

    with open(file_name,"w") as f:
        for i in tasks:
            f.write(i + "\n")


def task_dell():
    print_tasks()
    select = int(input("select delete task number - "))
    with open(file_name,"r+") as f:
        tasks = f.read().split("\n")

        tasks.pop(select)

        new_tasks = []
        for i in range(len(tasks)-1):
            new_tasks.append(str(i)+" "+tasks[i][2:])


        with open(file_name,"w") as f:
            for i in new_tasks:
                f.write(i+"\n")



select = int(input("""Select coamn 
1) add task
2) dell task
3) print tasks
4) ststus task
------ """))

if select == 1:
    add_task()
elif select == 2:
    task_dell()
elif select == 3:
    print_tasks()
elif select == 4:
    status()
else:
    print("no comand")

