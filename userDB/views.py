from django.shortcuts import render, redirect
from django.urls import reverse
from userDB.forms import UserForm
from userDB.models import user

# Create your views here.

def home(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('home'))
    users = user.objects.all()
    return render(request, 'home.html', {'form':form, 'users':users})

def view_user(request, pk):
    view_user = user.objects.get(pk=pk)
    return render(request, 'user.html', {'user':view_user})