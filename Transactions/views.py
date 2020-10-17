from django.shortcuts import render, redirect
from django.contrib import messages
from lib.models import Books
from users.models import Member
from Fine.models import Fine
from Transactions.models import Transaction
from django.contrib.auth.decorators import login_required


@login_required
def issue_book(request,id):
    book = Books.objects.filter(id=id).first()
    fine = 0
    if book.book_quantity > 0:
    	member = Member.objects.get(user=request.user)
    	transaction = Transaction.objects.filter(member = member.uid).all()
    	for trans in transaction:
    		fines = Fine.objects.filter(transaction=trans).first()
    		if fines != None:
    			fine += fines.amount

    	if fine == 0:
    		issue_status = True

    	else: 
    		issue_status = False

    else:
    	issue_status = False


    if issue_status:
    	book.book_quantity = book.book_quantity - 1
    	book.save()
    	transaction = Transaction(member = member, book= book)
    	transaction.save()

    else:
    	messages.warning(request, f'Please visit the reception to pay fines. Your total fines is {fine}')


    return redirect('home')

def return_book(request,id):
    pass