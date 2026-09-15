import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class SaleDataAnalyzer:
    """
    An Object-Oriented comprehensive Sales Data Analysis and Visualization tool
    utilizing Pandas, NumPy, Matplotlib, and Seaborn.
    """
    
    def __init__(self):
        self.data = None

    def __del__(self):
        # Destructor for cleanup if necessary
        pass

    def load_data(self, file_path):
        """Load sales data from a CSV file."""
        try:
            if not os.path.exists(file_path):
                print(f"Error: The file '{file_path}' was not found.")
                return False
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading dataset: {e}")
            return False

    def explore_data(self):
        """Display basic information and rows about the dataset."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        while True:
            print("\n-- Explore Data --")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info (info/describe)")
            print("6. Return to Main Menu")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                print(self.data.head())
            elif choice == '2':
                print(self.data.tail())
            elif choice == '3':
                print(list(self.data.columns))
            elif choice == '4':
                print(self.data.dtypes)
            elif choice == '5':
                print("\n--- DataFrame Info ---")
                print(self.data.info())
                print("\n--- Descriptive Statistics ---")
                print(self.data.describe())
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def clean_data(self):
        """Handle missing values and data cleaning."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        while True:
            print("\n-- Handle Missing Data --")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean (numeric columns)")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Return to Main Menu")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print(missing)
            elif choice == '2':
                numeric_cols = self.data.select_dtypes(include=[np.number]).columns
                self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                print("Missing values filled with column means successfully.")
            elif choice == '3':
                initial_rows = len(self.data)
                self.data.dropna(inplace=True)
                print(f"Dropped rows with missing values. Removed {initial_rows - len(self.data)} rows.")
            elif choice == '4':
                val = input("Enter the value to replace NaNs with: ").strip()
                self.data.fillna(val, inplace=True)
                print(f"Missing values replaced with '{val}'.")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def mathematical_operations(self):
        """Perform mathematical operations on sales data and demonstrate NumPy array conversion."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            print("No numeric columns available for mathematical operations.")
            return

        print(f"Available numeric columns: {numeric_cols}")
        col = input("Enter a numeric column name (e.g., Sales): ").strip()
        if col not in numeric_cols:
            print("Invalid column name.")
            return

        arr = self.data[col].to_numpy()
        print(f"Converted column '{col}' to NumPy array: {arr}")
        
        print("\nChoose operation:")
        print("1. Multiply array by a scalar factor")
        print("2. Add a constant value to array")
        print("3. Element-wise square of array")
        
        op_choice = input("Enter choice: ").strip()
        if op_choice == '1':
            factor = float(input("Enter multiplication factor: "))
            result = np.multiply(arr, factor)
            print(f"Result: {result}")
        elif op_choice == '2':
            const = float(input("Enter constant to add: "))
            result = np.add(arr, const)
            print(f"Result: {result}")
        elif op_choice == '3':
            result = np.square(arr)
            print(f"Result: {result}")
        else:
            print("Invalid choice.")

    def combine_data(self):
        """Combine current DataFrame with another DataFrame or sample data."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        print("\n-- Combine Data --")
        print("1. Concatenate with sample additional sales records vertically")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # Create a sample DataFrame to concatenate
            sample_dict = {}
            for col in self.data.columns:
                if self.data[col].dtype == 'int64' or self.data[col].dtype == 'float64':
                    sample_dict[col] = [0] * len(self.data.columns) # placeholder or sample values
                else:
                    sample_dict[col] = ["Sample"] * len(self.data.columns)
            
            # Simple dummy record based on columns
            sample_data = pd.DataFrame([self.data.iloc[0].to_dict()])
            self.data = pd.concat([self.data, sample_data], ignore_index=True)
            print("Successfully concatenated sample row. New dataset shape:", self.data.shape)
        else:
            print("Invalid choice.")

    def split_data(self):
        """Split data based on criteria (e.g., Region or threshold)."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        cols = list(self.data.columns)
        print(f"Columns available: {cols}")
        col = input("Enter column name to split by (e.g., Region): ").strip()
        if col not in cols:
            print("Column not found.")
            return

        unique_vals = self.data[col].unique()
        print(f"Unique values in '{col}': {unique_vals}")
        val = input(f"Enter one value from {unique_vals} to filter/split: ").strip()
        
        # If numeric, try converting
        try:
            if val.replace('.', '', 1).isdigit():
                val = float(val) if '.' in val else int(val)
        except:
            pass

        split_df = self.data[self.data[col] == val]
        print(f"Split successful! Subset contains {len(split_df)} rows.")
        print(split_df.head())

    def search_sort_filter(self):
        """Search, sort, and filter data."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        while True:
            print("\n-- Search, Sort, and Filter --")
            print("1. Search records by value in a column")
            print("2. Sort dataset by a column")
            print("3. Filter dataset using a condition (e.g., Sales > value)")
            print("4. Return to Main Menu")
            
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                col = input("Enter column name to search in: ").strip()
                if col not in self.data.columns:
                    print("Column not found.")
                    continue
                val = input("Enter value to search for: ").strip()
                try:
                    if val.replace('.', '', 1).isdigit():
                        val = float(val) if '.' in val else int(val)
                except:
                    pass
                result = self.data[self.data[col] == val]
                print(f"Found {len(result)} matching rows:")
                print(result)
            elif choice == '2':
                col = input("Enter column name to sort by: ").strip()
                if col not in self.data.columns:
                    print("Column not found.")
                    continue
                ascending = input("Sort ascending? (y/n): ").strip().lower() == 'y'
                sorted_df = self.data.sort_values(by=col, ascending=ascending)
                print(sorted_df.head())
            elif choice == '3':
                col = input("Enter numeric column name for filtering: ").strip()
                if col not in self.data.columns:
                    print("Column not found.")
                    continue
                threshold = float(input("Enter threshold value: "))
                filtered = self.data[self.data[col] > threshold]
                print(f"Filtered rows (where {col} > {threshold}): {len(filtered)}")
                print(filtered.head())
            elif choice == '4':
                break
            else:
                print("Invalid choice.")

    def aggregate_functions(self):
        """Compute statistical aggregates like sum, mean, count."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        print(f"Numeric columns: {numeric_cols}")
        col = input("Enter numeric column for aggregation: ").strip()
        if col not in numeric_cols:
            print("Invalid column.")
            return

        arr = self.data[col].to_numpy()
        print(f"\n-- Aggregates for {col} --")
        print(f"Sum: {np.sum(arr)}")
        print(f"Mean: {np.mean(arr)}")
        print(f"Median: {np.median(arr)}")
        print(f"Standard Deviation: {np.std(arr)}")
        print(f"Variance: {np.var(arr)}")
        print(f"Min: {np.min(arr)}")
        print(f"Max: {np.max(arr)}")

    def create_pivot_table(self):
        """Generate pivot tables for data summarization."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        print(f"Columns: {list(self.data.columns)}")
        index_col = input("Enter column for pivot index (e.g., Region): ").strip()
        values_col = input("Enter column for values (e.g., Sales): ").strip()
        
        try:
            pivot = pd.pivot_table(self.data, index=index_col, values=values_col, aggfunc=['sum', 'mean', 'count'])
            print("\n--- Pivot Table ---")
            print(pivot)
        except Exception as e:
            print(f"Error creating pivot table: {e}")

    def visualize_data(self):
        """Data visualization with Matplotlib and Seaborn with explicit display/save per option."""
        if self.data is None:
            print("No dataset loaded. Please load a dataset first.")
            return

        while True:
            print("\n-- Data Visualization --")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Seaborn Heatmap (Correlation Matrix)")
            print("7. Return to Main Menu")
            
            choice = input("Enter your choice: ").strip()
            
            if choice in ['1', '2', '3', '4', '5']:
                x_col = input(f"Enter x-axis column name {list(self.data.columns)}: ").strip()
                y_col = input(f"Enter y-axis column name {list(self.data.columns)}: ").strip()
                
                if x_col not in self.data.columns or y_col not in self.data.columns:
                    print("Invalid column names provided. Please check column headers.")
                    continue
                
                plt.figure(figsize=(9, 5))
                
                if choice == '1':
                    plt.bar(self.data[x_col], self.data[y_col], color='skyblue', edgecolor='black')
                    plt.title(f"Bar Plot: {y_col} vs {x_col}", fontsize=12, fontweight='bold')
                    plt.xlabel(x_col, fontsize=10, fontweight='bold')
                    plt.ylabel(y_col, fontsize=10, fontweight='bold')
                    plt.grid(True, linestyle='--', alpha=0.6)
                    plt.tight_layout()
                    
                    if input("Do you want to save this plot? (y/n): ").strip().lower() == 'y':
                        fn = input("Enter filename (e.g., bar_plot.png): ").strip()
                        if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                    plt.show()
                
                elif choice == '2':
                    plt.plot(self.data[x_col], self.data[y_col], marker='o', color='blue', linewidth=2)
                    plt.title(f"Line Plot: {y_col} vs {x_col}", fontsize=12, fontweight='bold')
                    plt.xlabel(x_col, fontsize=10, fontweight='bold')
                    plt.ylabel(y_col, fontsize=10, fontweight='bold')
                    plt.grid(True, linestyle='--', alpha=0.6)
                    plt.tight_layout()
                    
                    if input("Do you want to save this plot? (y/n): ").strip().lower() == 'y':
                        fn = input("Enter filename (e.g., line_plot.png): ").strip()
                        if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                    plt.show()
                
                elif choice == '3':
                    plt.scatter(self.data[x_col], self.data[y_col], color='coral', s=100, edgecolor='black')
                    plt.title(f"Scatter Plot: {y_col} vs {x_col}", fontsize=12, fontweight='bold')
                    plt.xlabel(x_col, fontsize=10, fontweight='bold')
                    plt.ylabel(y_col, fontsize=10, fontweight='bold')
                    plt.grid(True, linestyle='--', alpha=0.6)
                    plt.tight_layout()
                    
                    if input("Do you want to save this plot? (y/n): ").strip().lower() == 'y':
                        fn = input("Enter filename (e.g., scatter_plot.png): ").strip()
                        if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                    plt.show()
                
                elif choice == '4':
                    pie_data = self.data.groupby(x_col)[y_col].sum()
                    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=140, shadow=True)
                    plt.title(f"Pie Chart of {y_col} by {x_col}", fontsize=12, fontweight='bold')
                    plt.tight_layout()
                    
                    if input("Do you want to save this plot? (y/n): ").strip().lower() == 'y':
                        fn = input("Enter filename (e.g., pie_chart.png): ").strip()
                        if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                    plt.show()
                
                elif choice == '5':
                    plt.hist(self.data[y_col], bins=10, color='purple', edgecolor='black', alpha=0.8)
                    plt.title(f"Histogram of {y_col}", fontsize=12, fontweight='bold')
                    plt.xlabel(y_col, fontsize=10, fontweight='bold')
                    plt.ylabel('Frequency', fontsize=10, fontweight='bold')
                    plt.grid(True, linestyle='--', alpha=0.6)
                    plt.tight_layout()
                    
                    if input("Do you want to save this plot? (y/n): ").strip().lower() == 'y':
                        fn = input("Enter filename (e.g., histogram.png): ").strip()
                        if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                    plt.show()
                
            elif choice == '6':
                numeric_df = self.data.select_dtypes(include=[np.number])
                if numeric_df.empty:
                    print("No numeric columns available for correlation heatmap.")
                    continue
                
                plt.figure(figsize=(8, 6))
                sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
                plt.title("Correlation Heatmap", fontsize=12, fontweight='bold')
                plt.tight_layout()
                
                if input("Do you want to save this heatmap? (y/n): ").strip().lower() == 'y':
                    fn = input("Enter filename (e.g., heatmap.png): ").strip()
                    if fn: plt.savefig(fn, dpi=300); print(f"Saved as {fn}")
                plt.show()
                
            elif choice == '7':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please select a valid option between 1 and 7.")

def main():
    analyzer = SaleDataAnalyzer()
    
    while True:
        print("\n========= Sales Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Clean Data & Handle Missing Values")
        print("4. Mathematical Operations & NumPy Arrays")
        print("5. Combine / Split Data")
        print("6. Search, Sort, Filter & Aggregates")
        print("7. Create Pivot Table")
        print("8. Data Visualization (Matplotlib & Seaborn)")
        print("9. Exit")
        print("================================================================")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            path = input("Enter the path of the dataset (CSV file, e.g., data/sales_data.csv): ").strip()
            analyzer.load_data(path)
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
            analyzer.clean_data()
        elif choice == '4':
            analyzer.mathematical_operations()
        elif choice == '5':
            print("\n1. Combine Data")
            print("2. Split Data")
            sub = input("Enter choice: ").strip()
            if sub == '1':
                analyzer.combine_data()
            elif sub == '2':
                analyzer.split_data()
        elif choice == '6':
            print("\n1. Search, Sort, Filter")
            print("2. Aggregate Functions & Statistics")
            sub = input("Enter choice: ").strip()
            if sub == '1':
                analyzer.search_sort_filter()
            elif sub == '2':
                analyzer.aggregate_functions()
        elif choice == '7':
            analyzer.create_pivot_table()
        elif choice == '8':
            analyzer.visualize_data()
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()