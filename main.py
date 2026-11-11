import shutil

# File names
STUDENT_FILE = "students.txt"
BACKUP_FILE = "students_backup.txt"
NAMES_COURSES_FILE = "names_and_courses.txt"


# Register a new student
def register_student():

    print("\nEnter Student Details")

    student_id = input("Student ID: ")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    course = input("Course: ")
    city = input("City: ")

    student_record = f"{student_id},{name},{email},{phone},{course},{city}"

    with open(STUDENT_FILE, "a+", encoding="utf-8") as file:

        file.seek(0, 2)

        file.seek(file.tell() - 1 if file.tell() > 0 else 0)

        last_character = file.read(1)

        if last_character != "\n" and last_character != "":
            file.write("\n")

        file.write(student_record + "\n")

    print("\nStudent registered successfully!")


# Read all student records
def read_all_students():

    print("\n===== ALL STUDENT RECORDS =====")

    with open(STUDENT_FILE, "r", encoding="utf-8") as file:
        records = file.readlines()

    for record in records:
        print(record.strip())


# Read individual lines
def read_individual_lines():

    print("\n===== INDIVIDUAL STUDENT RECORDS =====")

    with open(STUDENT_FILE, "r", encoding="utf-8") as file:

        for line_number, record in enumerate(file, start=1):
            print(f"Line {line_number}: {record.strip()}")


# Count student records
def count_students():

    with open(STUDENT_FILE, "r", encoding="utf-8") as file:
        total_records = sum(1 for line in file if line.strip())

    print("\nTotal student records:", total_records)


# Create backup file
def create_backup():

    shutil.copyfile(STUDENT_FILE, BACKUP_FILE)

    print("\nBackup created successfully!")


# Create file containing only names and courses
def create_names_and_courses_file():

    with open(STUDENT_FILE, "r", encoding="utf-8") as source_file:
        records = source_file.readlines()

    with open(NAMES_COURSES_FILE, "w", encoding="utf-8") as output_file:

        output_file.write("Name,Course\n")

        for record in records:

            fields = record.strip().split(",")

            if len(fields) == 6:

                name = fields[1]
                course = fields[4]

                output_file.write(f"{name},{course}\n")

    print("\nNames and courses file created successfully!")


# Main application menu
def main():

    while True:

        print("\n===== STUDENT REGISTRATION APPLICATION =====")

        print("1. Register a new student")
        print("2. Read all student records")
        print("3. Read individual lines")
        print("4. Count student records")
        print("5. Create backup file")
        print("6. Create names and courses file")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            register_student()

        elif choice == "2":
            read_all_students()

        elif choice == "3":
            read_individual_lines()

        elif choice == "4":
            count_students()

        elif choice == "5":
            create_backup()

        elif choice == "6":
            create_names_and_courses_file()

        elif choice == "7":
            print("\nThank you for using the application!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# Execute the application
if __name__ == "__main__":
    main()