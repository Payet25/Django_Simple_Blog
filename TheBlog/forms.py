from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Title'}),
		'title_tag': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Title Tag'}),
		'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
		#'author': forms.Select(attrs={'class': 'form-control', 'Placeholder': 'Enter Author'}),
		'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'Placeholder': 'Enter Category'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Speak Your Mind'}),
		'snippet': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Enter Snippet'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body', 'snippet')

		widgets = {
		'title': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Title'}),
		'title_tag': forms.TextInput(attrs={'class': 'form-control', 'Placeholder': 'Enter Title Tag'}),
		#'author': forms.Select(attrs={'class': 'form-control', 'Placeholder': 'Enter Author'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Speak Your Mind'}),
		'snippet': forms.Textarea(attrs={'class': 'form-control', 'Placeholder': 'Enter Snippet'}),
		}