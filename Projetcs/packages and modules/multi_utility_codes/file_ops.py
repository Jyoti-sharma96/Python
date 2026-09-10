def create_file():
    filename = input("Enter file name: ")
    with open(filename, 'w') as f:
        pass
    print("File created successfully!")

def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(filename, 'w') as f:
        f.write(data)
    print("Data written successfully!")

def read_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, 'r') as f:
            print("File Content:")
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(filename, 'a') as f:
        f.write("\n" + data)
    print("Data appended successfully!")