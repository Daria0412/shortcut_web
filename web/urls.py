from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.show_list, name = 'show_list'),
    path('list/', views.show_list_1, name = 'show_list_1'),
    path('list/delete/', views.delete, name = 'delete'),
    path('list/<int:no>/<int:page>', views.show_list, name = 'show_list'),
    path('register/',views.register, name = 'register'),
    path('test/',views.test, name='test')
]