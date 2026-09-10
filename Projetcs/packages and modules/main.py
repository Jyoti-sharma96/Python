from multi_utility_codes import datetime_ops, math_ops, random_ops, uuid_ops, file_ops, explore_ops

def main():
    while True:
        print("\n" + "=" * 30)
        print("Welcome to Multi-Utility codes")
        print("=" * 30)
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("\n--- Datetime and Time Operations ---")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1': datetime_ops.display_current_datetime()
            elif sub_choice == '2': datetime_ops.calculate_date_difference()
            elif sub_choice == '3': datetime_ops.format_custom_date()
            elif sub_choice == '4': datetime_ops.run_stopwatch()
            elif sub_choice == '5': datetime_ops.run_countdown_timer()
            
        elif choice == '2':
            print("\n--- Mathematical Operations ---")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1': math_ops.calculate_factorial()
            elif sub_choice == '2': math_ops.calculate_compound_interest()
            elif sub_choice == '3': math_ops.trigonometric_calculations()
            elif sub_choice == '4': math_ops.area_geometric_shapes()
            
        elif choice == '3':
            print("\n--- Random Data Generation ---")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1': random_ops.generate_random_number()
            elif sub_choice == '2': random_ops.generate_random_list()
            elif sub_choice == '3': random_ops.generate_random_password()
            elif sub_choice == '4': random_ops.generate_random_otp()
            
        elif choice == '4':
            uuid_ops.generate_uuid()
            
        elif choice == '5':
            print("\n--- File Operations ---")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            sub_choice = input("Enter your choice: ")
            if sub_choice == '1': file_ops.create_file()
            elif sub_choice == '2': file_ops.write_file()
            elif sub_choice == '3': file_ops.read_file()
            elif sub_choice == '4': file_ops.append_file()
            
        elif choice == '6':
            explore_ops.explore_attributes()
            
        elif choice == '7':
            print("\nThank you for using the Multi-Utility Codes!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()