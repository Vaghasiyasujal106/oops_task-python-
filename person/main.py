#Create a class Person with private attributes and define  methods to get and set the values of those attributes.
class Person:
    def __init__(self):
        self.name = {}
        self.gmail = {}
        self.phone_no = {}

    def set_attributes(self):
        name = input("enter the name:")
        if name not in self.name:
            gmail = input("enter the gmail:")
            phone_no = input("enter the phone no:")
            self.name = name
            self.gmail = gmail
            self.phone_no = phone_no
        else:
            print("name already exists.")

    def get_attributes(self):
        name = input("enter the name:")
        if name in self.name:
            print(f"name is :{name}")
            print(f"email_id is: {self.gmail}")
            print(f"phone_no is :{self.phone_no}")
        else:
            print("note data.....")
p1 = Person()

while True:
    try:
        print("1.add personal attributes:")
        print("2.show the personal attributes:")
        print("3.exit the code")

        choice = int(input("enter the choice:"))
        if choice == 1:
            p1.set_attributes()
        elif choice == 2:
            p1.get_attributes()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
        continue




