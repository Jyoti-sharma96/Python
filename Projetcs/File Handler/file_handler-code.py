from datetime import datetime
import os


class JournalManager:
    """A class to encapsulate journal file handling operations,

    file modes (r, w, a, x), and exception handling.
    """

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        print("\n--- Add a New Entry ---")
        entry_text = input("Enter your journal entry: ")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"[{timestamp}]\n{entry_text}\n\n"

        try:
            # File Mode 'a' (Append): Opens file for appending.
            # Creates the file if it does not exist, and preserves existing content.
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(formatted_entry)
            print("Entry added successfully!")
        except PermissionError:
            print("Error: Permission denied to write to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_entries(self):
        print("\n--- View All Entries ---")
        try:
            # File Mode 'r' (Read): Opens file for reading. Raises FileNotFoundError if missing.
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()
                if content:
                    print("Your Journal Entries:")
                    print("-" * 45)
                    print(content)
                else:
                    print(
                        "No journal entries found. Start by adding a new entry!"
                    )
        except FileNotFoundError:
            print(
                "No journal entries found. Start by adding a new entry!"
            )  # Matches exact document sample output
        except PermissionError:
            print("Error: Permission denied to read the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_entry(self):
        print("\n--- Search for an Entry ---")
        keyword = input("Enter a keyword or date to search: ").strip()

        try:
            # File Mode 'r' used to read and search through journal contents
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
                entries = content.split("\n\n")
                matching_entries = [
                    entry for entry in entries if keyword.lower() in entry.lower()
                ]

                if matching_entries:
                    print("\nMatching Entries:")
                    print("-" * 45)
                    for entry in matching_entries:
                        if entry.strip():
                            print(entry.strip() + "\n")
                else:
                    print(
                        f"No entries were found for the keyword: {keyword}."
                    )
        except FileNotFoundError:
            print("No journal file found to search.")
        except PermissionError:
            print("Error: Permission denied to access the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_entries(self):
        print("\n--- Delete All Entries ---")
        confirm = (
            input(
                "Are you sure you want to delete all entries? (yes/no): "
            )
            .strip()
            .lower()
        )
        if confirm == "yes":
            try:
                if os.path.exists(self.filename):
                    os.remove(self.filename)
                    print("All journal entries have been deleted.")
                else:
                    print("No journal file exists to delete.")
            except PermissionError:
                print("Error: Permission denied to delete the file.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Deletion cancelled.")

    def demonstrate_exclusive_creation(self):
        """Demonstrates file mode 'x' (Exclusive Creation):

        Creates a new file. Fails with FileExistsError if the file already exists.
        """
        try:
            with open("test_exclusive.txt", "x") as f:
                f.write("Test exclusive mode.")
            print(
                "Mode 'x': File 'test_exclusive.txt' created successfully."
            )
        except FileExistsError:
            print(
                "Mode 'x': File already exists! (Demonstrating FileExistsError handling)"
            )


def main():
    manager = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input:   \n")

        if choice == "1":
            manager.add_entry()
        elif choice == "2":
            manager.view_entries()
        elif choice == "3":
            manager.search_entry()
        elif choice == "4":
            manager.delete_entries()
        elif choice == "5":
            print("Exiting Personal Journal Manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1 and 5.")


if __name__ == "__main__":
    main()