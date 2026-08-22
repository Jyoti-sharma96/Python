import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# E-LIBRARY DASHBOARD 
# ===================

class LibraryDashboard:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads the original CSV and cleans/transforms it inside the code."""
        try:
            
            self.df = pd.read_csv(self.file_path)
            print(">>> Original CSV file loaded successfully!\n")
            
            # 2. Checking  for missing values 
            if self.df.isnull().sum().sum() > 0:
                print(">>> Notice: Missing data found. Cleaning up empty rows...")
                self.df = self.df.dropna()
            else:
                print(">>> Data is clean. No missing values found.\n")
                
            # 3. Data Transformation 
            
            self.df['Borrowing Duration (Days)'] = (
                pd.to_datetime(self.df['return_date']) - pd.to_datetime(self.df['borrow_date'])
            ).dt.days
            
            # Converting dates for monthly and day-of-week analysis
            self.df['borrow_date'] = pd.to_datetime(self.df['borrow_date'])
            self.df['Month'] = self.df['borrow_date'].dt.strftime('%b')
            self.df['DayOfWeek'] = self.df['borrow_date'].dt.day_name()
            
            print(">>> Data preparation and cleaning complete!\n")
            
        except FileNotFoundError:
            print(f">>> Error: Could not find '{self.file_path}'. Make sure it is in the same folder!")
        except Exception as e:
            print(f">>> An error occurred: {e}")

    def generate_report(self):
        """Prints a summary report of the library data."""
        if self.df is None:
            return
            
        print("==============================")
        print("      LIBRARY SUMMARY REPORT  ")
        print("==============================")
        print(f"Total Transactions Processed: {len(self.df)}")
        print(f"Total Unique Books: {self.df['book_id'].nunique()}")
        print(f"Total Unique Users: {self.df['user_id'].nunique()}")
        print("==============================\n")

    def calculate_statistics(self):
        """Calculates key statistics using Pandas and NumPy."""
        if self.df is None:
            return

        # Finding the most borrowed book ID
        top_book = self.df['book_id'].mode()[0]
        
        # Using NumPy for duration statistics
        durations = self.df['Borrowing Duration (Days)'].values
        avg_duration = np.mean(durations)
        std_duration = np.std(durations)

        print("--- COMPUTED STATISTICS ---")
        print(f"Most Borrowed Book (ID): {top_book}")
        print(f"Average Borrowing Duration: {avg_duration:.2f} days")
        print(f"Standard Deviation of Duration: {std_duration:.2f} days\n")

    def filter_transactions(self, target_genre):
        """Filters records by a specific genre/category."""
        if self.df is None:
            return None
            
        filtered = self.df[self.df['book_category'].str.lower() == target_genre.lower()]
        print(f">>> Filtered: Found {len(filtered)} records in category '{target_genre}'.")
        return filtered

    def visualize_data(self):
        """Creates and shows each required chart one by one."""
        if self.df is None:
            return

        print(">>> Generating charts one by one. Close each window to see the next chart.\n")

        # 1. Bar Chart: Total Borrowings by Book Category 
        plt.figure(figsize=(8, 6))
        category_counts = self.df['book_category'].value_counts()
        sns.barplot(x=category_counts.index, y=category_counts.values, palette="Blues_d", edgecolor='black', linewidth=1.5)
        plt.title("Borrowing Count by Book Category")
        plt.xlabel("Book Category")
        plt.ylabel("Total Borrowings")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig("top_books_chart.png", dpi=300, bbox_inches='tight')
        plt.show()  


        # 2. Line Graph: Borrowing Trends Over Months
        plt.figure(figsize=(8, 6))
        
        # Group by numerical month first 
        self.df['Month_Num'] = self.df['borrow_date'].dt.month
        monthly_counts = self.df.sort_values('Month_Num').groupby(['Month_Num', 'Month']).size().reset_index(name='count')
        
        plt.plot(monthly_counts['Month'], monthly_counts['count'], marker="o", color="green", linestyle="-", linewidth=2, markeredgecolor='black', markeredgewidth=1.5)
        plt.title("Monthly Borrowing Trends")
        plt.xlabel("Months")
        plt.ylabel("Number of Borrowings")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig("monthly_trends_chart.png", dpi=300, bbox_inches='tight')
        plt.show() 


        # 3. Pie Chart: Distribution of Books Borrowed by Genre
        plt.figure(figsize=(8, 6))
        genre_counts = self.df['book_category'].value_counts()
        plt.pie(genre_counts.values, labels=genre_counts.index, autopct="%1.1f%%", colors=sns.color_palette("pastel"), wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
        plt.title("Distribution of Books by Genre")
        plt.tight_layout()
        plt.savefig("genre_distribution_chart.png", dpi=300, bbox_inches='tight')
        plt.show() 

        # 4. Heatmap: Activity by Day of the Week vs Genre
        plt.figure(figsize=(8, 6))
        pivot_table = self.df.pivot_table(index='DayOfWeek', columns='book_category', values='user_id', aggfunc='count', fill_value=0)
        sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d", edgecolor='black', linewidth=1.5
                    )
        plt.title("Borrowing Activity (Day of Week vs Genre)")
        plt.xlabel("Genre")
        plt.ylabel("Day of Week")
        plt.tight_layout()
        plt.savefig("activity_heatmap.png", dpi=300, bbox_inches='tight')
        plt.show() 


if __name__ == "__main__":
    
   
    my_file = "library_transactions.csv"
    
    dashboard = LibraryDashboard(my_file)
    
    
    dashboard.load_data()
    dashboard.generate_report()
    dashboard.calculate_statistics()
    
   
    dashboard.filter_transactions("non-fiction")
    
  
    dashboard.visualize_data()