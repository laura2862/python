from StudentClass import Student
class StudentMgmt(object):
    def __init__(self):
        self.students=[]
    def __str__(self):
        return f'{self.students}'


    def add_student(self):
        name=input('please input a student name: ')
        age=int(input('please input the student age: '))
        mobile=input('please input the student mobile: ')
        stu=Student(name,age,mobile)
        self.students.append(stu)
        print(f'{stu.name} is added!!')
        print(self.students)
    def find_student(self):
        name=input('please input a student name: ')
        for i in self.students:
            if i.name ==name:
                print(f'{name} is found, age: {i.age}, mobile: {i.mobile}')
                break
        else:
            print('not found')
    def delete_student(self):
        name = input('please input a student name: ')
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                print(f'{name}, age: {i.age}, mobile: {i.mobile} is deleted')
                break
        else:
            print('not found')
    def edit_student(self):
        name = input('please input a student name: ')
        for i in self.students:
            if i.name == name:
                i.name = input('please input a student name: ')
                i.age = int(input('please input the student age: '))
                i.mobile = input('please input the student mobile: ')
                print(f'{name}, age: {i.age}, mobile: {i.mobile} is changed')
                break
        else:
            print('not found')
    def list_student(self):
        for i in self.students:
            print(i)
    def save_student(self):
        f=open('student.txt','w',encoding='utf-8')
        # for i in self.students:
        #     if i:
        #         f.write(str(i.__dict__))
        self.students = [i.__dict__ for i in self.students]
        f.write(str(self.students))
        print('students info is saved in file student.txt ')
        f.close()
    def load_student(self):
        try:
            f=open('student.txt','r',encoding='utf-8')
        except Exception as e:
            f=open('student.txt', 'w', encoding='utf-8')
        else:
            content=f.read()
            if not content:
                self.students=[]
            # self.students = eval(content)
            else:
                self.students=(eval(content))
                self.students=[Student(i['name'],i['age'],i['mobile']) for i in self.students]
    @staticmethod
    def menu():
        print('-' * 40)
        print('[1] Add a student')
        print('[2] Delete a student')
        print('[3] Modify a student\'s info')
        print('[4] Find a student')
        print('[5] List all students')
        print('[6] Save to a student file')
        print('[0] Exit')
        print('-' * 40)
    def run(self):
        print('Welcome to student management system!')
        self.load_student()
        while True:
            self.menu()
            num=int(input('please select below:'))
            if num ==1:
                self.add_student()
            elif num==2:
                self.delete_student()
            elif num==3:
                self.edit_student()
            elif num==4:
                self.find_student()
            elif num==5:
                self.list_student()
            elif num==6:
                self.save_student()
            elif num==0:
                print('thanks for using our system, exit system')
                break
            else:
                print('please re-enter your option!')






