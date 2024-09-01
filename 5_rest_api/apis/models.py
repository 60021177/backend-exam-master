from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    abbrev = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name


class Classroom(models.Model):
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)
    grade = models.CharField(max_length=20)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.grade} {self.section}"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
