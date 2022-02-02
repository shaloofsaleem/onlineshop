from django.shortcuts import redirect, render
from .models import UserCreateForm
from django.contrib.auth import authenticate,login
# Create your views here.
 


def signup(request):
    if request.method =='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            new_user=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('shop')
    else:
        form=UserCreateForm()
    context={
        'form':form,
        }    
    return render(request,'registration/signup.html',context)

