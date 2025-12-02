def load_task():
    try:
        file= open("task.txt","r")
        lines=file.readlines()
        file.close()

        cleaned=[]
        for line in lines:
            cleaned.append(line.strip())

        return[]

    except FileNotFoundError:
        return[]    


def save_task(task):
    file = open("task.txt","w")
    for t in task:
        file.write(t+"\n")
    file.close()    


task=load_task()

while True:
    print("1.add a task")
    print("2.view a task")
    print("3.delete a task")
    print("4.exit")
    print("5.edit a task")

    choice= input("what's your choice?")
    if choice=="4":
        break
    if choice=="1":
        print("what you wanna add")
        new_task =input("add:")
        task.append(new_task)
        save_task(task)
        print("task added")

    if choice=="2":      #if not task:print("no task yet")
        if len(task)==0: 
            print("no task yet")
        else:
            i=1
            for t in task:
                print(i,t)
                i=i+1                    
    
    if choice=="3":
        if not task:
            print("No task yet to delete")
        else:
            i=1
            for t in task:
                print(i,t)
                i=i+1

            task_num = int(input("which task number you wanna delete?")) 
            if task_num<1:
                print("invalid task number")
            elif task_num>len(task):
                print("invalid task number")
            else:
                del task[task_num-1]
                save_task(task)
                print("task deleted")

    if choice =="5":
        if not task:
            print("no task to edit")
        else:
            i=1
            for t in task:
                print(i,t) 
                i=i+1

            task_edit= int(input("which task number you wanna edit ?")) 
            if task_edit<1:
                print("invalid task number") 
            elif task_edit>len(task): 
                print("invalid task number") 
            else:
                index=task_edit-1
                new_name=input("enter the new task")
                task[index]=new_name
                save_task(task)
                print("task updated") 
 

    
