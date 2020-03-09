from django.urls import path
from . import views

urlpatterns = [
    # path('student/list/', views.student_list, name='student_list'),
    path('add/', views.res_add, name='res_add'),
    # path('res/add/', views.res_add, name='res_add'),
    # path('res/update/<int:user_id>/', views.res_update, name='res_update'),
    # path('student/delete/<int:user_id>/', views.student_delete, name='student_delete'),
    # path('class/list/', views.class_list, name='class_list'),
    # path('class/add/', views.class_add, name='class_add'),
    # path('class/update/<int:class_id>/', views.class_update, name='class_update'),
    # path('class/delete/<int:class_id>/', views.class_delete, name='class_delete'),
]