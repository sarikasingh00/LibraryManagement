from django import forms
from .models import Books
from django.contrib.auth.models import User
from users.models import Member

class AddBooks(forms.ModelForm):
	class Meta:
		model = Books
		fields = ['book_title','author_name','book_description','book_subject','book_quantity']

class AddUsers(forms.ModelForm):
	class Meta:
		model = Member
		fields = ['username','password','member_name','member_department','is_type']
