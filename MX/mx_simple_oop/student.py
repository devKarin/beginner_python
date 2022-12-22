"""
MX - Simple OOP.

This program creates class Student.

"""


class Student:
    """
    Student class.

    Student has name and finished status, which is by default false.
    """

    def __init__(self, name):
        """
        Initialize the Student class.

        Student has name and finished status, which is by default false.
        """
        self.name = name
        self.finished = False


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False
