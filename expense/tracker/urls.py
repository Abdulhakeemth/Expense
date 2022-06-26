from django.urls import path,include
from . import views
from tracker import views
from django.conf import settings
from rest_framework import routers
from .views import *



app_name = 'tracker'

router = routers.DefaultRouter()
router.register('Profile', views.ProfileViewset),
router.register('Expense',views.ExpenseViewset),
router.register('User',views.UserViewSet)
urlpatterns =[

]
urlpatterns += router.urls 
