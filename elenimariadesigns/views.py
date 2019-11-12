from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import JsonResponse
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request):
    posts = Post.objects.all()
    return render(request, 'post_detail.html', {'posts': posts})

def post_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_view.html', {'post': post})    

def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save()
            return redirect('post_detail')
    else:
        form = PostForm()
        return render(request, 'post_form.html', {'form': form})
  
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')

def comment_detail(request, pk):
    comment = Comment.objects.get()
    return render(request, 'comment_detail.html')

def comment_create(request):
    comment = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

def comment_list(request):
    comment = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comment})    

def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list') 

def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            post = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'base.html')

def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail')
    else:
        form = CommentForm()
        return render(request, 'comment_form.html', {'form': form})

def comment_view(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'comment_view.html', {'comment': comment})        