from django.urls import path
from . import views
app_name = 'get_student'

urlpatterns = [
  path('', views.register, name='student_new'),
  path('all', views.index, name='student_list'),
]
