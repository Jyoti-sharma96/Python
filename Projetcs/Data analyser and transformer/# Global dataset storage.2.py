# Global dataset storage
dataset = []

def main():
    while True:
        print("\n--- Data Analyzer and Transformer ---")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial")
        print("4. Filter Data by Threshold")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Exit Program")
        
        choice = input("Please enter your choice (1-7): ")

        
        if choice == '1':
            def input_data():
                """\n Allows the user to input a 1D list of numbers manually or use sample data."""
                global dataset
                method = input("Choose input method:\n (1) Manual\n (2) Sample data: ")
                if method == '1':
                    data = input("Enter numbers separated by spaces: ")
                    dataset = [float(x) for x in data.split()]
                else:
                    dataset = [34, 12, 56, 78, 43, 21, 90]
                print("Data stored successfully!")
            
            print(f"\n[Documentation]: {input_data.__doc__}")
            input_data()

        
        elif choice == '2':
            def display_summary():
                """Displays basic statistics about the dataset using built-in functions."""
                global dataset
                if not dataset:
                    print("Dataset is empty! Please input data first.")
                    return
                print(f"Total no. of elements: {len(dataset)}")
                print(f"Min: {min(dataset)}")
                print(f"Max: {max(dataset)}")
                print(f"Sum: {sum(dataset)}")
            
            print(f"\n[Documentation]: {display_summary.__doc__}")
            display_summary()

        
        elif choice == '3':
            def calculate_factorial(n):
                """Calculates the factorial of a number using recursion."""
                return 1 if n <= 1 else n * calculate_factorial(n-1)
            
            print(f"\n[Documentation]: {calculate_factorial.__doc__}")
            num = int(input("Enter number: "))
            print(f"Result: {calculate_factorial(num)}")

        
        elif choice == '4':
            def filter_data():
                """Filters data based on a user-specified threshold using lambda."""
                global dataset
                if not dataset:
                    print("Dataset is empty! Please input data first.")
                    return
                threshold = float(input("Enter threshold: "))
                print(list(filter(lambda x: x > threshold, dataset)))
            
            print(f"\n[Documentation]: {filter_data.__doc__}")
            filter_data()

        
        elif choice == '5':
            def sort_data():
                """Demonstrates sort() (in-place) and sorted() (returns new list)."""
                global dataset
                if not dataset:
                    print("Dataset is empty! Please input data first.")
                    return
                print(f"Sorted: {sorted(dataset)}")
            
            print(f"\n[Documentation]: {sort_data.__doc__}")
            sort_data()

        
        elif choice == '6':
            def get_stats():
                """Returns multiple statistics: min, max, and average."""
                global dataset
                if not dataset:
                    return None, None, None
                return min(dataset), max(dataset), sum(dataset)/len(dataset)
            
            print(f"\n[Documentation]: {get_stats.__doc__}")
            mi, ma, avg = get_stats()
            if mi is None:
                print("Dataset is empty! Please input data first.")
            else:
                print(f"Min: {mi}, Max: {ma}, Avg: {avg:.2f}")

        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    