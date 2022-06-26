from rest_framework import serializers
from .models import Profile,Expense
# from tracker.functions import get_auto_id

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile

        fields = ['user','income','expenses','balance']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense

        fields = ['id','user','name','monthly_amount','expense_type',]  

        