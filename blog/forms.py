from django import forms
from .models import Post, Comment, Project


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = {'title', 'text'}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = {'title', 'text'}
