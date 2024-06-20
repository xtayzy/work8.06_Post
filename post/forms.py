from django import forms

from post.models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'author', 'category',


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'author', 'content',


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = 'name',

