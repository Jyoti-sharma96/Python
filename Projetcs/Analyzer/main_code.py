import numpy as np

class DataAnalytics:
    def __init__(self):
        # Private instance variable to encapsulate the array
        self.__array = None

    def create_array(self):
        print("\nArray Creation:")
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            elements = list(map(float, input("Enter elements separated by space: ").split()))
            self.__array = np.array(elements)
        elif choice == '2':
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            print(f"Enter {rows * cols} elements for the array separated by space: ")
            elements = list(map(float, input().split()))
            self.__array = np.array(elements).reshape(rows, cols)
        elif choice == '3':
            d = int(input("Enter depth: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            print(f"Enter {d * rows * cols} elements for the array separated by space: ")
            elements = list(map(float, input().split()))
            self.__array = np.array(elements).reshape(d, rows, cols)
        else:
            print("Invalid choice!")
            return
        
        print("Array created successfully:")
        print(self.__array)

    def mathematical_operations(self):
        print("\nMathematical Operations:")
        print("Choose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ")
        
        # Get dimensions for the arrays
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        
        # Input First Array
        print(f"Enter {rows * cols} elements for the First Array separated by space: ")
        elements1 = list(map(float, input().split()))
        arr1 = np.array(elements1).reshape(rows, cols)
        
        # Input Second Array
        print(f"Enter {rows * cols} elements for the Second Array separated by space: ")
        elements2 = list(map(float, input().split()))
        arr2 = np.array(elements2).reshape(rows, cols)
        
        print("\nFirst Array:")
        print(arr1)
        print("Second Array:")
        print(arr2)
        
        if choice == '1':
            res = np.add(arr1, arr2)
            print("Result of Addition:")
        elif choice == '2':
            res = np.subtract(arr1, arr2)
            print("Result of Subtraction:")
        elif choice == '3':
            res = np.multiply(arr1, arr2)
            print("Result of Multiplication:")
        elif choice == '4':
            res = np.divide(arr1, arr2)
            print("Result of Division:")
        else:
            print("Invalid choice!")
            return
        print(res)

    def combine_or_split_arrays(self):
        if self.__array is None:
            print("Please create an array first.")
            return
        print("\nCombine or Split Arrays:")
        print("Choose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            elements = list(map(float, input(f"Enter the elements of another array to combine ({self.__array.size} elements separated by space): ").split()))
            other_array = np.array(elements).reshape(self.__array.shape)
            print("Original Array:")
            print(self.__array)
            print("Second Array:")
            print(other_array)
            combined = np.vstack((self.__array, other_array))
            print("Combined Array (Vertical Stack):")
            print(combined)
        elif choice == '2':
            if self.__array.ndim == 1:
                res = np.array_split(self.__array, 2)
                print("Split Arrays:", res)
            else:
                res = np.array_split(self.__array, 2, axis=0)
                print("Split Arrays along axis 0:", res)
        else:
            print("Invalid choice!")

    def search_sort_filter(self):
        if self.__array is None:
            print("Please create an array first.")
            return
        print("\nSearch, Sort, and Filter:")
        print("Choose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            val = float(input("Enter value to search: "))
            indices = np.where(self.__array == val)
            print("Found at indices:", indices)
        elif choice == '2':
            sorted_arr = np.sort(self.__array, axis=None)
            print("Original Array:")
            print(self.__array)
            print("Sorted Array:")
            print(sorted_arr.reshape(self.__array.shape))
        elif choice == '3':
            cond = float(input("Filter elements greater than: "))
            filtered = self.__array[self.__array > cond]
            print("Filtered values:", filtered)

    def aggregates_and_statistics(self):
        if self.__array is None:
            print("Please create an array first.")
            return
        print("\nAggregates and Statistics:")
        print("Choose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = input("Enter your choice: ")
        
        print("Original Array:")
        print(self.__array)
        
        if choice == '1':
            print("Sum of Array:", np.sum(self.__array))
        elif choice == '2':
            print("Mean of Array:", np.mean(self.__array))
        elif choice == '3':
            print("Median of Array:", np.median(self.__array))
        elif choice == '4':
            print("Standard Deviation:", np.std(self.__array))
        elif choice == '5':
            print("Variance:", np.var(self.__array))
        else:
            print("Invalid choice!")

    @classmethod
    def project_info(cls):
        return "Class-level utility: NumPy Data Analytics Toolkit"

    @staticmethod
    def validation_helper(val):
        return val is not None

    def menu(self):
        while True:
            print("\nWelcome to the NumPy Analyzer!")
            print("---------------------------------------")
            print("Choose an option:")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.create_array()
            elif choice == '2':
                self.mathematical_operations()
            elif choice == '3':
                self.combine_or_split_arrays()
            elif choice == '4':
                self.search_sort_filter()
            elif choice == '5':
                self.aggregates_and_statistics()
            elif choice == '6':
                print("Thank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.menu()