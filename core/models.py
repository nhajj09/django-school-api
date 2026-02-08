from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    units = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=50)
    grade = models.CharField(max_length=5)
