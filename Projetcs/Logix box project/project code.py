#-----------------------------------------------------------------------Welcome Messeage and Menu code-------------------------------------------------------------
print("WELCOME TO THE PATTERN GENERATOR AND NUMBER ANALYZER PROGRAM")
print("*" * 60)
print(" ")
print("This is simple program where we generate patterns and analyze the numbers based on the user input ")
print("=" * 98)
print(" ")
while True:
    print("\nPlease select the option from the menu below")
    print("1. Pattern Generator")
    print("2. Number Analyzer")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")
#-----------------------------------------------------------------------Pattern Generator-------------------------------------------------------------

    if choice == "1":
        row = int(input("\n Enter the number of rows for the pattern: "))

        if row <= 0:
            print("Please enter a number greater than 0 for the number of rows.")
        else:
            print("\nPattern for given number of rows is:")
            for i in range(1, row + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()
#-----------------------------------------------------------------------Number Analyzer and sum display-------------------------------------------------------------

    elif choice == "2":
        while True:
            start = int(input("\nEnter the starting number for analysis: "))
            end = int(input("Enter the ending number for analysis: "))

            if start < 0 or end < 0:
                print("Please enter non-negative integers for the range.")
                continue
            elif start > end:
                print("Starting number should be less than or equal to ending number.")
                continue
            else:
                break

        total = 0

        print("\nNumber Analysis for the given range:")

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"{num} is Even")
            else:
                print(f"{num} is Odd")

            total += num

        print(f"\nThe sum of numbers from {start} to {end} is: {total}")
#-----------------------------------------------------------------------Exit code-------------------------------------------------------------

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")                
      
                    
