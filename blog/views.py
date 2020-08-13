from django.shortcuts import render
from .models import Post, Project, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404


def Home(request):
    contents = {
        'posts': Post.objects.all().order_by('-created_date')
    }
    return render(request, 'blog/Home.html', contents)


def About(request):

    return render(request, 'blog/About.html')


def Contact(request):

    return render(request, 'blog/Contact.html')


def Project_page(request):
    contents = {
        'projects': Project.objects.all().order_by('-created_date')
    }
    return render(request, 'blog/Project.html', contents)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'blog/project_detail.html', {'project': project})
