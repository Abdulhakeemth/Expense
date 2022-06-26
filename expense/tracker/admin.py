from django.contrib import admin

# Register your models here.
from tracker.models import *
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','income','expenses','balance']
admin.site.register(Profile,ProfileAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user','name','monthly_amount','expense_type',]
admin.site.register(Expense,ExpenseAdmin)

