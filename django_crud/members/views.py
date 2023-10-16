from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import  Member
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

# Create your views here.
class MembersView(APIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    def get(self, request, *args, **kwargs):
        '''
        List all the memebers items 
        '''
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        '''
        Create the Member with given memeber data
        '''
        data = {
            'firstname': request.data.get('firstname'), 
            'lastname': request.data.get('lastname'), 
            'email': request.data.get('email'),
            'phone':  request.data.get('phone')
        }
        try:
            serializer = MemberSerializer(data=data)
        except:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            member = Member.objects.get(email=request.data.get('email'))
        except Member.DoesNotExist:
            member = None
        if member:
            return Response([{'email': 'There is a user with this email'}],status=status.HTTP_302_FOUND)
        try:
            member = Member.objects.get(phone=request.data.get('phone'))
        except Member.DoesNotExist:
            member = None
        if member:
            return Response([{'phone': 'There is a user with this phone'}],status=status.HTTP_302_FOUND)

        print("request valid =>", serializer.is_valid())
        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




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
