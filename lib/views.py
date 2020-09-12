from django.shortcuts import render,redirect
from users.models import Librarian,Member
from lib.models import Books
from lib.forms import AddBooks, MemberForm, UserForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def welcome(request):
	return render(request,"lib/welcome.html")

def home(request):
	if Librarian.objects.filter(user=request.user).first():
		return render(request,"lib/librarian_home.html")
	if Member.objects.filter(user=request.user).first():
		return render(request,"lib/member_home.html")

def manage_books(request):
	return render(request,"lib/manage_books.html")

def manage_users(request):
	return render(request,"lib/manage_users.html")

def add_books(request):
	if(request.method=='POST'):
		form = AddBooks(request.POST, request.FILES)
		if(form.is_valid()):
			form.save()
			return redirect('manage-books')
	else:
		form = AddBooks()
	return render(request,"lib/add_books.html",{'form':form})

def view_books(request):
	books = Books.objects.all()
	return render(request,"lib/view_books.html",{'books':books})

def delete_books(request,par1):
	books = Books.objects.filter(id=par1).first()
	books.delete()
	return redirect('view-books')


def update_books(request,par1):
	books = Books.objects.get(id=par1)
	if (request.method == 'POST'):
		update_form = AddBooks(request.POST,instance=books)
		if (update_form.is_valid()):
			update_form.save()
			return redirect('view-books')
	else:
		update_form = AddBooks(instance=books)
	return render(request,"lib/update_books.html",{'update_form':update_form})

def add_users(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		member_form = MemberForm(request.POST)
		if member_form.is_valid() and user_form.is_valid():
			user = user_form.save()
			member =  member_form.save(commit=False)
			member.user = user
			member.save()
			messages.success(request, f'Registration complete! You may log in!')
			return redirect('manage-users')
	else:
		user_form = UserForm(request.POST)
		member_form = MemberForm(request.POST)
	return render(request, 'lib/add_users.html', {'user_form': user_form, 'member_form': member_form})
		
	# return render(request,"lib/add_users.html",{'form':form})

def view_users(request):
	members = Member.objects.all()
	return render(request,"lib/view_users.html",{'members':members})

def delete_users(request,id):
	member = Member.objects.filter(uid=id).first()
	member.delete()
	return redirect('view-users')

def update_users(request,id):
	members = Member.objects.get(uid=id)
	if (request.method == 'POST'):
		user_update_form = UserForm(request.POST,instance = members.user)
		member_update_form =  MemberForm(request.POST,instance=members)
		if (user_update_form.is_valid() and member_update_form.is_valid()):
			user  =user_update_form.save()
			member = member_update_form.save(commit=False)
			member.user =  user
			messages.success(request, f'Update complete!')
			return redirect('view-users')
		else:
			messages.error(request, f'Update unsucessful')
	else:
		user_update_form = UserForm(instance = members.user)
		member_update_form =  MemberForm(instance=members)
	return render(request,"lib/update_books.html",{'user_update_form':user_update_form,"member_update_form" : member_update_form})
	# return redirect('view-books')