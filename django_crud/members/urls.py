from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name="details"),
#    path('members/add', views.add_member,name="add-member"),
    path('testing/',views.testing, name="testing")
]
