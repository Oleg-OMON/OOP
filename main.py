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

    def lecturer_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_for_lectures:
                lecturer.grades_for_lectures[course] += [grade]
            else:
                lecturer.grades_for_lectures[course] = [grade]
        elif grade > 10:
            return 'can not be bigger than 10'
        else:
            return 'Ошибка'

    def same_grades(self):
        for key, grade in self.grades.items():
            result = sum(grade) // len(grade)
            self.average_grade.append(result)
            return

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
            else:
                student.grades[course] = [grade]
        else:
            return


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grade = {}
        self.grades_for_lectures = {}
        self.average_grade = []
        self.courses_in_progress = []



    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции:{self.average_grade}'


    def __lt__(self, other):
      if not isinstance(other, Lecturer):
        print('Not a lecturer')
        return
      return self.average_grade < other.average_grade


    def same_grade_lec(self, subject, lecturer):
        for key, grade in self.grades_for_lectures.items():
            result = sum(grade) // len(grade)
            self.average_grade.append(result)
        return

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)


    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}'


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
two_student.lecturer_grades(two_lecturer, 'Git', 10)




print(one_student.__dict__)
print(one_lecturer.__dict__)
print(two_student.__dict__)
print(two_lecturer.__dict__)
print('')
print(one_student)
print('')
print(two_student)
print('')
print(one_lecturer)
print('')
print(two_lecturer)