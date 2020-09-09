from django.shortcuts import render,redirect
from users.models import Librarian,Member
from lib.models import Books
from lib.forms import AddBooks,AddUsers
from django.contrib.auth.models import User
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
		form = AddBooks(request.POST)
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
	form = AddUsers(request.POST)
	if(form.is_valid()):
		user = User(username = form['username'], password = form['password'])
	return render(request,"lib/add_users.html",{'form':form})

def view_users(request):
	member = Member.objects.all()
	return render(request,"lib/view_users.html",{'member':member})

def delete_users(request,par1):
	# books = Books.objects.filter(id=par1).first()
	# books.delete()
	return redirect('view-books')

def update_users(request,par1):
	# books = Books.objects.get(id=par1)
	# if (request.method == 'POST'):
	# 	update_form = AddBooks(request.POST,instance=books)
	# 	if (update_form.is_valid()):
	# 		update_form.save()
	# 		return redirect('view-books')
	# else:
	# 	update_form = AddBooks(instance=books)
	# return render(request,"lib/update_books.html",{'update_form':update_form})
	return redirect('view-books')