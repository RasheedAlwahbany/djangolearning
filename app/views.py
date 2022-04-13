
from lib2to3.pgen2.token import EQUAL
from django.shortcuts import render
from .models import Posts
from django.db import transaction


@transaction.atomic()  # or
# Create your views here.
def getAllPosts(request):
    """_summary_

    Args:
      ==>  request (_type_): _description_
      ==>
    Returns:
        _type_: _description_
    """
    with transaction.atomic():
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('body'):
                if request.POST.get('options') == '1':
                    post = Posts(title=request.POST.get('title'),
                                 body=request.POST.get('body'))
                    post.save()
                elif request.POST.get('options') == '2':
                    post = Posts.objects.filter(
                        title=request.POST.get('old_title')).first()
                    post.title = request.POST.get('title')
                    post.body = request.POST.get('body')
                    post.save()
                else:
                    # to delete:
                    # posts = Posts.objects.all()
                    # Posts.delete() #or
                    Posts.objects.filter(pk=request.POST.get('old_title')).delete()
                    post.save()

    context = {'posts': post}
    return render(request, 'index.html', context)
