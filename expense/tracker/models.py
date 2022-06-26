from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    income = models.FloatField()
    expenses = models.FloatField(default=0)
    balance = models.FloatField(null=True,blank=True)


    class Meta:
        db_table = 'Profile'
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')
        # ordering = ('-date_added',)

    def __str__(self):
        return str(self.user)




    
class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length= 120)
    monthly_amount = models.FloatField()
    TYPE = (
        ('Housing','Housing'),
        ('Transportation','Transportation'),
        ('Inurance','Inurance'),
        ('Food','Food'),
        ('Entertainment','Enterainment'),
        ('Loan','Loan'),
        ('Taxes','Taxes'),
        ('Saving or Investments','Saving or Investments'),
        ('Gifts and Donations','Gifts and Donations'),
        ('Personal Care','Personal Care'),
        ('Legal','Legal')
    )
    expense_type = models.CharField(max_length=120, choices=TYPE)
    


    class Meta:
        db_table = 'Expense'
        verbose_name = ('Expense')
        verbose_name_plural = ('Expenses')

    def __str__(self):
        return str(self.name)

