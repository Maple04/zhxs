from .models import Post
from django.forms import ModelForm, Textarea


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'category', 'tags', 'author']
		widgets = {
			'title': Textarea(attrs={'cols': 65, 'rows': 1}),
			'body': Textarea(attrs={'cols': 95, 'rows': 38}),
		}


class EditForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'category', 'tags', 'author']
		widgets = {
			'title': Textarea(attrs={'cols': 68, 'rows': 1, 'size': 40, 'title': 'nnnn'}),
			'body': Textarea(attrs={'cols': 95, 'rows': 38}),
		}
