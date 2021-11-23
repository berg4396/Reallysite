from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.contrib.auth.views import LoginView
from mysite.forms import UserCreationForm

def index(request):
    objs = Article.objects.all()[:3]
    context={
        'title':'Really Site',
        'articles': objs,
    }
    return render(request, 'mysite/index.html', context)


class Login(LoginView):
    template_name =  'mysite/auth.html'

def signup(request):
    context = {}
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.is_active = False
            user.save()
    return render(request, 'mysite/auth.html', context)
