#path: jSchool/jSchool
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    pid = models.CharField(unique=True, max_length=12)
    grade = models.IntegerField(unique=False)

    class Meta(object):
        ordering = ('pid', 'name')

    def __str__(self):
        return U'%s %s' %(self.name, self.pid)


#note: the name field should not be unique but this is to demenstrate an error and how to handle it with real data.
#note2: grade field should have null=True, this is for demo purpose.

# same models.py, below the first model.
class Course(models.Model):
    name = models.CharField(max_length=50)
    call_number = models.CharField(unique=False, max_length=4)
    instructor = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    term = models.CharField(max_length=200)
    date = models.DateField()
    students = models.ManyToManyField(Student)

    class Meta(object):
        verbose_name_plural = "Courses"
        ordering = ('-date', 'name')

    def __str__(self):
        return U'%s %s' %(self.call_number, self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Course, self).save(*args, **kwargs)
