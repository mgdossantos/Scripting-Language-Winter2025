# Student Management System

# Dictionary to store student details
students = {}


def add_student(name, id_number, courses):
    students[id_number] = {
        'name': name,
        'courses': courses
    }
    print(f"Student {name} added successfully.")


def update_courses(id_number, new_courses):

    if id_number in students:
        students[id_number]['courses'] = new_courses
        print(f"Courses for student {students[id_number]['name']} updated successfully.")
    else:
        print("Student not found.")


def get_student_details(id_number):

    if id_number in students:
        return students[id_number]
    else:
        print("Student not found.")
        return None


# Sample usage
if __name__ == "__main__":
    # Add students
    add_student("Marcela dos Santos", "001", ["Math", "Science", "History"])
    add_student("Benicio Goncalves", "002", ["Art", "Math", "Physics"])
    add_student("Francisco dos Santos", "003", ["Art", "Science", "Math"])

    # Update courses
    update_courses("001", ["Physics", "Math", "Chemistry"])

    # Retrieve student details
    print(get_student_details("001"))
    print(get_student_details("002"))
    print(get_student_details("003"))  # This student does not exist