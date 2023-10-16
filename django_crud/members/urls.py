from django.urls import path, include
from . import views
from .views import MembersView
from rest_framework import routers

#router = routers.DefaultRouter()
#router.register(r'member', views.MembersViewSet)

urlpatterns = [
   # path('', include(router.urls)),
    path('', views.index, name="index"),
    path('member/', MembersView.as_view()),
    #path('members/', views.members, name='members'),
    #path('members/details/<int:id>', views.details, name="details"),
    path('testing/',views.testing, name="testing")
]
