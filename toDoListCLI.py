from token import tok_name

details = []
while True:
    print('******************************')
    print('         To_Do_List')
    print('******************************')
    # print('Chose An Option')
    # print('==================')
    print('1. Add Task')
    print('2. View Task')
    print('3. Edit Details')
    print('4. Delete Task')
    print('5. Exit')




    choice1 = input('Select One option : ')
    if choice1 == '1':
        print('===============================')
        print('    !!ADD YOUR TASK HERE!!    ')
        print('===============================')
        tname = input('Enter Your Task : ')
        details.append(tname)
        print('Task Added Successfully!!')


    elif choice1 == '2':
        print('================================')
        print('           YOUR TASKS')
        print('================================')
        if not details:
            print('No Task Aded!!')

        else:
            for i,task in enumerate(details, 1):
                print(f"{i}.{task}")

    elif choice1 == '3':
        print('===============================')
        print('        EDIT YOUR TASK')
        print('===============================')
        if not details:
            print('No Task To Edit')

        else:
            for i, task in enumerate(details, 1):
                print(f"{i}.{task}")
            num = int(input('Enter Task Number To Edit : '))
            if 1 <= num <= len(details):
                new_task = input('Enter New Task : ')
                details[num -1] = new_task
                print('Task Updated Successfully')
            else:
                print('Enter Correct Task Number!!')

    elif choice1 == '4':
        print('================================')
        print('           DELETE TASK')
        print('================================')
        if not details:
            print("Not Deleted any Task")
        else:
            for i, task in enumerate(details,1):
                print(f'{i}.{task}')
                if 1 <= num <= len(details):
                    deleted = details.pop(num -1)
                    print(f"Task '{deleted}' Deleted Successfully")
                else:
                    print('Invaled Task Number')

    elif choice1 == '5':
        print('Bye..')
        break
    else:
        print('Enter Correct Number!!!')







