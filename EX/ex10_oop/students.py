"""
EX10 - Students.

This program organizes students.

Available classes:
Student; Student class

Functions in Student class:
__init__; Student constructor. Every student has: a name, list of courses by title and an average overall grade.
__repr__; Student representation. Returns student name.

Available functions:
filter_by_course(student_list: list, course: str) -> list;
    -> Returns a filtered list of students who are taking a certain course.
is_failing(student: Student) -> bool;
    -> Returns true if the student is failing school.
succeeding_students(student_list: list) -> list;
    -> Returns a list of students who are not failing school.
failing_students(student_list: list) -> list;
    -> Return a list of students that are failing school.
sort_by_best_grade(student_list: list) -> list;
    -> Returns a sorted list of students by their average grade in descending order.
sort_by_worst_grade(student_list: list) -> list;
    -> Returns a sorted list of students by their average grade in ascending order.

"""


class Student:
    """
    Class for students.

    Every student has:
    a name,
    list of courses by title and
    an average overall grade.
    """

    def __init__(self, name: str, courses: list, average_grade: float):
        """
        Student constructor.

        Every student has a name, courses list.
        """
        self.name = name
        self.courses = courses
        self.average_grade = average_grade

    def __repr__(self):
        """
        Student representation.

        Returns student name.
        """
        return self.name


def filter_by_course(student_list: list, course: str) -> list:
    """
    Return a filtered list of students who are taking a certain course.

    The name of the course is in the list of courses for the student.

    :param student_list: a list of Students
    :param course: the title of the course
    :return: a filtered list of students taking the course
    """
    # Assuming there is a student list to filter, create a list of students who have given course in their course list
    # using built-in filter function.
    if student_list:
        return list(filter(lambda student: course in student.courses, student_list))
    else:
        return []


def is_failing(student: Student) -> bool:
    """
    Return true if the student is failing school.

    They are failing if their average grade is below 1.0.

    :param student: a Student object
    :return: if student is failing
    """
    return student.average_grade < 1.0


def succeeding_students(student_list: list) -> list:
    """
    Return a list of students who are not failing school.

    :param student_list: a list of students
    :return: filtered list of students that are not failing
    """
    # Assuming there is a student list to filter, create a list of students who are not failing (whose average grade
    # is greater than or equal to 1.0) by filtering student list and using predefined function is_failing.
    if student_list:
        return list(filter(lambda student: not is_failing(student), student_list))


def failing_students(student_list: list) -> list:
    """
    Return a list of students who are failing school.

    :param student_list: a list of students
    :return: filtered list of students that are failing
    """
    # Assuming there is a student list to filter, create a list of students who are failing (whose average grade
    # is lower than 1.0) by using previously defined function is_failing.
    if student_list:
        return list(filter(lambda student: is_failing(student), student_list))


def sort_by_best_grade(student_list: list) -> list:
    """
    Return a sorted list of students by their average grade in descending order.

    Highest average grade students first.
    If a student is failing school (average grade less than 1.0) then do not return them in the list.
    If students have the same grade, then sort them alphabetically.

    :param student_list: a list of students
    :return: sorted list of succeeding students by average grade in descending order
    """
    if not student_list:
        return []
    # First, sort the student list descending by students average grade, then ascending (alphabetically) by name
    # using built-in sorted method and "-" to reverse the sorting order.
    sorted_list = sorted(student_list, key=lambda student: (-student.average_grade, student.name.casefold()))
    # Then, create list of students who are not failing by filtering them from previously sorted list using
    # previously defined function is_failing.
    return list(filter(lambda student: not is_failing(student), sorted_list))


def sort_by_worst_grade(student_list: list) -> list:
    """
    Return a sorted list of students by their average grade in ascending order.

    Lowest average grade students first.
    If a student is failing school (average grade less than 1.0) then do not return them in the list.
    If students have the same grade, then sort them alphabetically.

    :param student_list: a list of students
    :return: sorted list of succeeding students by average grade in ascending order
    """
    if not student_list:
        return []
    # First, sort the student list by students average grade, then by name ascending.
    sorted_list = sorted(student_list, key=lambda student: (student.average_grade, student.name.casefold()))
    # Then, create list of students who are not failing by filtering them from previously sorted list and using
    # previously defined function is_failing.
    return list(filter(lambda student: not is_failing(student), sorted_list))


if __name__ == '__main__':
    student1 = Student("Ann", ["Programming", "Maths", "Lithology"], 3.2)
    student2 = Student("Josh", ["Maths", "English", "Politics"], 2.0)
    student3 = Student("Bush", ["Politics"], 0.5)
    student4 = Student("Marcus", ["Web application", "Computers", "Artificial Intelligence"], 4.2)
    students = [student1, student2, student3, student4]

    print("student repr: ", student1)  # -> Ann
    print("filter_by_course: ", filter_by_course(students, "Maths"))  # -> [Ann, Josh]

    print("is_failing: ", is_failing(student3))  # -> True
    print("is_failing: ", is_failing(student1))  # -> False

    print("succeeding_students: ", succeeding_students(students))  # -> [Ann, Josh, Marcus]

    print("failing_students: ", failing_students(students))  # -> [Bush]

    print("sort_by_best_grade: ", sort_by_best_grade(students))  # -> [Marcus, Ann, Josh]

    print("sort_by_worst_grade: ", sort_by_worst_grade(students))  # -> [Josh, Ann, Marcus]
