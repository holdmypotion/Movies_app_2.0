from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

def signup_page(request):
    form = UserCreationForm()
    return render(request, 'login/form.html', {'form': form})
    # return render(request, 'about.html')
