# Task: Build a Student Management System
# Problem: You need to implement a system that manages students and their courses.
# Details:
# Create a class Student with attributes like name, student_id, and list_of_courses.
# Create a class Course with attributes like course_name, course_code, and credits.
# Students should be able to enroll in and drop courses. The system should track the courses a student is enrolled in and the total credits.
# Implement methods like enroll_in_course(), drop_course(), and calculate_total_credits().



class Student:
    def __init__(self):
        self.name = []
        self.roll_no = []
        self.maths_marks = []
        self.science_marks = []

    def add_stu(self):
        roll_no_data = int(input("enter the roll_no:"))
        if roll_no_data not in self.roll_no:
            name = input("enter the name:")
            maths_marks = int(input("enter the maths_marks:"))
            science_marks = int(input("enter the science_marks:"))
            self.roll_no.append(roll_no_data)
            self.name.append(name)
            self.maths_marks.append(maths_marks)
            self.science_marks.append(science_marks)

        else:
            print("this roll no allready exist")

    def show_stu(self):
        if not self.roll_no:
            print("No students available.")
            return
        for i in range(len(self.roll_no)):
            print(f"  Roll No: {self.roll_no[i]}")
            print(f"  Name: {self.name[i]}")
            print(f"  Maths Marks: {self.maths_marks[i]}")
            print(f"  Science Marks: {self.science_marks[i]}")


    def search_stu(self):
        roll_no_data = int(input("enter the roll_no for search student :"))
        index = self.roll_no.index(roll_no_data)
        # print(index)
        print(f"name is :{self.name[index]}")
        print(f"roll_no is :{self.roll_no[index]}")
        print(f"maths_marks is : {self.maths_marks[index]}")
        print(f"science_marks is :{self.science_marks[index]}")
        # for roll_no_data in self.roll_no:
        #
        #     if roll_no_data in self.roll_no:
        #         print(f"name is :{self.name}")
        #         print(f"roll_no is :{self.roll_no}")
        #         print(f"maths_marks is : {self.maths_marks}")
        #         print(f"science_marks is :{self.science_marks}")
        #     else:
        #         print("no student existing...")

    def del_stu(self):
        roll_no_data = int(input("enter the roll_no to delete the student: "))
        if roll_no_data in self.roll_no:
            index = self.roll_no.index(roll_no_data)
            self.roll_no.pop(index)
            self.name.pop(index)
            self.maths_marks.pop(index)
            self.science_marks.pop(index)
            print("Student record deleted successfully.")
        else:
            print("No student exists with this roll number.")

    def update_stu(self):
        roll_no_data = int(input("enter the roll_no:"))
        index = self.roll_no.index(roll_no_data)
        choice = input("\n1.Change name \n2.Change maths mark \n3.Change Science mark.\nEnter your choice...")
        match choice:
            case '1':
                print(f"name is {self.name[index]}")
                new_name = input("Enter name: ")
                self.name[index] = new_name
            case '2':
                print(f"Maths mark is {self.maths_marks[index]}")
                new_m1 = input("Enter Maths mark : ")
                self.maths_marks[index] = new_m1
            case '3':
                print(f"Science mark is {self.science_marks[index]}")
                new_m2 = input("Enter Science mark : ")
                self.science_marks[index] = new_m2


        # if roll_no_new not in self.roll_no:
        #     name = input("enter the name:")
        #     maths_marks = int(input("enter the maths_marks:"))
        #     science_marks = int(input("enter the science_marks:"))
        #     self.roll_no.append(roll_no_new)
        #     self.name.append(name)
        #     self.maths_marks.append(maths_marks)
        #     self.science_marks.append(science_marks)

s1 = Student()

while True:
    print("1.add the student:")
    print("2.show the student:")
    print("3.search the student:")
    print("4.delete the student:")
    print("5.update the student:")
    print("6.exit the code......")
    try:
        choice = int(input("enter the choice:"))
        if choice == 1:
            s1.add_stu()
        elif choice == 2:
            s1.show_stu()
        elif choice == 3:
            s1.search_stu()
        elif choice == 4:
            s1.del_stu()
        elif choice == 5:
            s1.update_stu()
        elif choice == 6:
            print("exit the code:")
            break
        else:
            print("please enter the valid choise:")
    except ValueError:
        print("please enter the valid number:")

# from operator import indexOf
#
# a  = ['1','2','3','4','5','6','7','8','9','10']
#
# print(a.index('5'))