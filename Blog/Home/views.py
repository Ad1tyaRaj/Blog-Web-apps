from django.shortcuts import render
from .models import Blog

# Create your views here.

def Home(request):

    # if request.method == 'POST':
    #     Post = request.POST['Post-title']
    #     disc = request.POST['description']
    #     new_register = Blog(Post_title = Post , discription = disc)
    #     new_register.save()

    data = Blog.objects.all()
    return render(request,'Home/Home.html',{'Data':data})


