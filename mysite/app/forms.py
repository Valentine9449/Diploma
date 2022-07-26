from django.forms import ModelForm, TextInput, Textarea, ChoiceField, RadioSelect, Select
from authentication.models import User

from .models import Service, Comment

class ImageForm(ModelForm):
	class Meta:
		model = User
		fields = ('image',)
		labels = {
		'image': '',
		}


class ServiceForm(ModelForm):
	class Meta:
		CHOICES = [('1', 'First'), ('2', 'Second')]
		model = Service
		fields = ['first_name', 'last_name', 'number', 'full_text', 'services']

		widgets = {
			'first_name': TextInput(attrs={
				'class':'form-control',
				'placeholder': 'Ім`я'
				}),
			'last_name': TextInput(attrs={
				'class':'form-control',
				'placeholder': 'Прізвище'
				}),
			'number': TextInput(attrs={
				'class':'form-control',
				'placeholder': 'Номер телефону',
				'type': 'number'
				}),
			'full_text': Textarea(attrs={
				'class':'form-control',
				'placeholder': 'Ваше повідомлення'
				}),
			'services': Select(attrs={
			'class':'form-control'})
		}


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text',]


		widgets = {
			'comment_text': Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Ваш коментарій'
				})
		}
