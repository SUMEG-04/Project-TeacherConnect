from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('teacher/', views.teacher, name='teacher'),
    path('subadmin/', views.subadmin, name='subadmin'),
    path('search/', views.search, name='search'),
    path('takeinput',views.take_input, name = "takeinput" ),
    path("show_teachers",views.show_teachers, name = "show_teachers"),
    path('search_teachers',views.search_teachers,name = 'search_teachers'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name = "delete")
    
]