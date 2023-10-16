from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import  Member
from rest_framework import viewsets
from .serializers import MemberSerializer


# Create your views here.
class MembersViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer 




def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
            'members' : members
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
            'member': member
            } 
    return HttpResponse(template.render(context,request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
            'fruits': [ 'Apple', 'Banana','Cherry']
            }
    return HttpResponse(template.render(context,request))
