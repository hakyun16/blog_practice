from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title=request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.datetime.now()
    new_post.save()
    return redirect('home')

def edit(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request, post_id):
    update_post = Post.objects.get(id=post_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('home')

def delete(request, post_id):
    delete_post=Post.objects.get(id=post_id)
    delete_post.delete()
    return redirect('home')

    