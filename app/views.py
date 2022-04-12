
from lib2to3.pgen2.token import EQUAL
from django.shortcuts import render
from .models import posts

# Create your views here.
def getAllPosts(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body'):
            if request.POST.get('options') == '1':
                post = posts(title=request.POST.get('title'), body=request.POST.get('body'))
                post.save()
            elif request.POST.get('options')=='2':
                post=posts.objects.filter(title=request.POST.get('old_title')).first()
                post.title=request.POST.get('title')
                post.body=request.POST.get('body')
                post.save()
            
    
    post = posts.objects.all()
    context = {'posts': post}
    return render(request, 'index.html', context)
