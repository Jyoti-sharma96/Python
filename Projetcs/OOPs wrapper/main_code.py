class Person:
    """Base class representing a general Person."""

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print(f"Person created with name: {self.name} and age: {self.age}.")


class Employee(Person):
    """Employee Class (Base Class for specialized employees)."""

    # Method overloading simulated via default arguments in constructor
    def __init__(self, name="", age=0, employee_id="", salary=0.0):
        super().__init__(name, age)
        # Encapsulation: Private attributes
        self.__employee_id = employee_id
        self.__salary = float(salary)

    # Getter and Setter for employee_id
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    # Overriding display method
    def display(self):
        print(
            f"Employee created with name: {self.name}, age: {self.age}, ID: {self.__employee_id}, and salary: ${self.__salary}."
        )

    def __del__(self):
        """Destructor to clean up resources."""
        pass


class Manager(Employee):
    """Manager Class (Derived Class from Employee)."""

    def __init__(
        self, name="", age=0, employee_id="", salary=0.0, department=""
    ):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    # Override display() to include department information
    def display(self):
        print(
            f"Manager created with name: {self.name}, age: {self.age}, ID: {self.get_employee_id()}, salary: ${self.get_salary()}, and department: {self.department}."
        )


class Developer(Employee):
    """Developer Class (Derived Class from Employee)."""

    def __init__(
        self, name="", age=0, employee_id="", salary=0.0, programming_language=""
    ):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    # Override display() to include programming language information
    def display(self):
        print(
            f"Developer created with name: {self.name}, age: {self.age}, ID: {self.get_employee_id()}, salary: ${self.get_salary()}, and programming language: {self.programming_language}."
        )


def main():
    persons = []
    employees = []
    managers = []
    developers = []

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Verify Subclasses (issubclass)")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            p = Person(name, age)
            persons.append(p)
            print()
            p.display()

        elif choice == "2":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            e = Employee(name, age, emp_id, salary)
            employees.append(e)
            print()
            e.display()

        elif choice == "3":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            m = Manager(name, age, emp_id, salary, dept)
            managers.append(m)
            print()
            m.display()

        elif choice == "4":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            lang = input("Enter Programming Language: ")
            d = Developer(name, age, emp_id, salary, lang)
            developers.append(d)
            print()
            d.display()

        elif choice == "5":
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Developer")
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                print("\nPerson Details:")
                if not persons:
                    print("No persons found.")
                for p in persons:
                    print(f"Name: {p.name}, Age: {p.age}")
            elif sub_choice == "2":
                print("\nEmployee Details:")
                if not employees:
                    print("No employees found.")
                for e in employees:
                    print(
                        f"Name: {e.name}, Age: {e.age}, ID: {e.get_employee_id()}, Salary: ${e.get_salary()}"
                    )
            elif sub_choice == "3":
                print("\nManager Details:")
                if not managers:
                    print("No managers found.")
                for m in managers:
                    print(
                        f"Name: {m.name}, Age: {m.age}, ID: {m.get_employee_id()}, Salary: ${m.get_salary()}, Dept: {m.department}"
                    )
            elif sub_choice == "4":
                print("\nDeveloper Details:")
                if not developers:
                    print("No developers found.")
                for d in developers:
                    print(
                        f"Name: {d.name}, Age: {d.age}, ID: {d.get_employee_id()}, Salary: ${d.get_salary()}, Language: {d.programming_language}"
                    )
            else:
                print("Invalid choice!")

        elif choice == "6":
            print("\n--- Subclass Verification (issubclass) ---")
            print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")
            print(f"Is Developer a subclass of Employee? {issubclass(Developer, Employee)}")
            print(f"Is Employee a subclass of Person? {issubclass(Employee, Person)}")

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()