students=[]


def menu():
    print('-' * 40)
    print('welcom to the student management system')
    print('1. add student info')
    print('2. delete student info')
    print('3. modify student info')
    print('4. search student info')
    print('5. list student info')
    print('6. save student info to a file')
    print('0: exit')
    print('-' * 40)

# add a student
def add_student():
    student={}
    student['name']=input('please input a student name:')
    print(student['name'])
    student['age'] = int(input('please input a student age:'))
    print(student['name'])
    student['phone'] = input('please input a student phone number:')
    print(student['phone'])
    students.append(student)
    print(f'added {student["name"]}')
# delete a student
def delete_student():
    name=input('please input an student name you want to delete: ')
    print(name)
    for i in students:
        if i['name']==name:
            students.remove(i)
            print(f'{i["name"]} is deleted!!')
            break
    else:
        print('student not found!!!')
  # find a student
def search_student():
    name=input('please input a student name: ')
    print(name)
    for i in students:
        if i['name']==name:
            print(i)
            break
    else:
        print('student not found!!')

        # modify a student

def modify_student():
    name=input('please input the student name you want to modify: ')
    print(name)
    for i in students:
        if i['name']==name:
            i['age']== int(input('please input the age your want to change to: '))
            print(i['age'])
            i['phone'] == int(input('please input phone number your want to change to: '))
            print(i['phone'])
            print('modified successfully!!!')
            break
    else:
        print('not found')
# list students info
def list_students():
    file=open('student.txt','r',encoding='utf-8')
     
    content=str(file.read())
    if not content:
        return
    global students
    students = eval(content)
    print(students)
    file.close()

# save_students info
def save_students():
    file=open('student.txt','w',encoding='utf-8')
    file.write(str(students))
    print('saved a file as "student.txt"')
    file.close()

if __name__ == '__main__':
    while True:
        menu()
        option=int(input('please select: '))
        print(option)
        if option== 1:
            add_student()
        elif option==2:
            delete_student()
        elif option==3:
            modify_student()
        elif option==4:
            search_student()
        elif option==5:
            list_students()
        elif option == 6:
            save_students()
        elif option==0:
            print('thanks for using our system, see you next time!!')
            break
        else:
            print('please reenter your option:')
            continue

