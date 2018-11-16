from django.shortcuts import render
from .models import UserModel

def homePageView(request):
    context = {'content': UserModel.objects.all()} # pylint: disable=no-member
    return render(request, 'home.html', context)
