from django.db import models

# Create your models here.


class Colleges(models.Model):
    Name=models.CharField(max_length=128)
    Acronym = models.CharField(max_length=128)
    Location = models.CharField(max_length=128)
    Contact = models.CharField(max_length=128)

    def __str__(self):
        return self.Acronym



class Student(models.Model):
    Name = models.CharField(max_length=128)
    dob=models.DateField(null=True,blank=True)
    Email_id = models.EmailField()
    Dbnames = models.CharField(max_length=128)
    dropped_out = models.BooleanField(default=False)

    Colleges = models.ForeignKey(Colleges, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Marks(models.Model):

    problem1 = models.IntegerField(default=0)
    problem2 =models.IntegerField(default=0)
    problem3 = models.IntegerField(default=0)
    problem4 = models.IntegerField(default=0)
    Total = models.IntegerField(default=0)

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    def __str__(self):
        return f"Student{self.Student.Name}marks"








