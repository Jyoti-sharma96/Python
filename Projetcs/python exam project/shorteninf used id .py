import pandas as pd

# 1. Load your original CSV file
file_name = "library_transactions.csv"
df = pd.read_csv(file_name)

# 2. Shorten user_id to U1, U2, U3, etc.
unique_users = df['user_id'].unique()
user_mapping = {old_id: f"U{i+1}" for i, old_id in enumerate(unique_users)}
df['user_id'] = df['user_id'].map(user_mapping)

# 3. Shorten book_id to B1, B2, B3, etc.
unique_books = df['book_id'].unique()
book_mapping = {old_id: f"B{i+1}" for i, old_id in enumerate(unique_books)}
df['book_id'] = df['book_id'].map(book_mapping)

# 4. Save the updated data back into the same file
df.to_csv(file_name, index=False)

print(">>> Success! User IDs and Book IDs have been shortened.")