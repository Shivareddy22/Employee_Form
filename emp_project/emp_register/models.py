from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE) # Here we are going to specif the position property inside the employee table with the Position table. thus, 'foreignkey' relation. specify it with model and specifying with 'on_delete'--by this whenever we deleted the specific position, the details of that specific employee position records will delete.