class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []
        self.average_grade = []
        self.sum_of_grades = 0
        self.number_of_grades = 0
        all_students.append(self)

    def lecturer_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
            else:
                lecturer.grades_for_lectures[course] = [grade]
                lecturer.sum_of_grades += grade
                lecturer.number_of_grades += 1
        elif grade > 10:
            return 'can not be bigger than 10'
        else:
            return 'Ошибка'

    def same_grades(self):
        for grade in self.grades.values():
            result = sum(grade) // len(grade)
            self.average_grade.append(result)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'He (she) is not a Student!'
        else:
            return self.sum_of_grades / self.number_of_grades < other.sum_of_grades / other.number_of_grades





    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade}, \nКурсы в процессе изучения: {self.courses_in_progress}, \nЗавершенные курсы: {self.finished_courses}'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_for_lectures = {}
        self.class_being_mentored = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
            else:
                student.grades[course] = [grade]
                student.sum_of_grades += grade
                student.number_of_grades += 1
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grade = {}
        self.grades_for_lectures = {}
        self.average_grade = []
        self.courses_in_progress = []
        self.sum_of_grades = 0
        self.number_of_grades = 0
        all_lectures.append(self)



    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade}'


    def __lt__(self, other):
      if not isinstance(other, Lecturer):
        print('Not a lecturer')
        return
      return self.average_grade < other.average_grade


    def same_grade_lec(self):
        for grade in self.grades_for_lectures.values():
            result = sum(grade) // len(grade)
            self.average_grade.append(result)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)


    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'

all_students = []
all_lectures = []

def all_grade_of_students(list, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for student in list:
        for course, grades in student.grades.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Average grade = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')

def all_grade_of_lecturers(list, course_name):
    sum_of_grades = 0
    number_of_grades = 0
    for lecturer in list:
        for course, grades in lecturer.grades_for_lectures.items():
            if course == course_name:
                for mark in grades:
                    sum_of_grades += mark
                    number_of_grades += 1
    if number_of_grades != 0:
        print(f'Average grade = {sum_of_grades / number_of_grades}')
        return
    else:
        print('Not enough data')




one_student = Student('Oleg', 'Zas', '26')
one_student.courses_in_progress += ['Python']
one_student.courses_attached += ['Git']
one_student.finished_courses += ['Java']



two_student = Student('Misha', 'Aralov', '30')
two_student.courses_in_progress += ['Python']
two_student.courses_in_progress += ['Git']
two_student.finished_courses += ['Java']

one_lecturer = Lecturer('Anastasia', 'Zhurbina')
one_lecturer.courses_attached += ['Python']

one_mentor = Reviewer('Andrey', 'Chernicov')
two_mentor = Reviewer('Ivan', 'Pangurban')


two_lecturer = Lecturer('Vsevolod', 'Ivanovich')
two_lecturer.courses_attached += ['Python']
two_lecturer.courses_attached += ['Git']

one_lecturer.rate_hw(one_student, 'Python', 9)
one_lecturer.rate_hw(one_student, 'Python', 7)
one_lecturer.rate_hw(one_student, 'Python', 10)

two_lecturer.rate_hw(two_student, 'Git', 6)
two_lecturer.rate_hw(two_student, 'Git', 10)
two_lecturer.rate_hw(two_student, 'Git', 6)

one_student.lecturer_grades(one_lecturer, 'Python', 9)
one_student.lecturer_grades(one_lecturer, 'Python', 10)
two_student.lecturer_grades(two_lecturer, 'Git', 10)
two_student.lecturer_grades(two_lecturer, 'Git', 9)

one_student.same_grades()
two_student.same_grades()
one_lecturer.same_grade_lec()
two_lecturer.same_grade_lec()



# print(one_student.__dict__)
# print(one_lecturer.__dict__)
# print(two_student.__dict__)
# print(two_lecturer.__dict__)
print('')
print(one_student)
print('')
print(two_student)
print('')
print(one_lecturer)
print('')
print(two_lecturer)
print('')
print(one_mentor)
print('')
print(two_mentor)
print('')
print(one_student < two_student)
print(one_lecturer < two_lecturer)
print()
all_grade_of_students(all_students, 'Python')
all_grade_of_lecturers(all_lectures, 'Python')