#Group3 
# School Club Verification System

print("Please input the coressponding number to continue!")
students = {}

while True:
    print("\n1. Register\n2. Verify\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        sid = input("Student ID: ")

        while len(sid) != 6 or not sid.isdigit():
            print("Incorrect! ID must be exactly 6 digits!")
            sid = input("Student ID: ")

        name = input("Student Name: ").title()
        club = input("Club: ").title()
        students[sid] = {"name": name, "club": club}
        print("Registered!.")

    elif choice == "2":
        sid = input("Enter Student ID to Verify: ")
        if sid in students:
            info = students[sid]
            print(f"{info['name']} is registered in {info['club']} Club.")
        else:
            print("Student not verified or found.")

    elif choice == "3":
        print("Come back again!")
        break

    else:
        print("Invalid Input.")