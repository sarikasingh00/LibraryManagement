from django.shortcuts import render
from .models import Fine
from Transactions.models import Transaction
# from django.contrib.auth.models import User
from users.models import Member
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from lib.views import librarian_check

# Create your views here.
@login_required
def check_fines(request):
    user = request.user
    if user.is_superuser:
        fines = Fine.objects.all() 
        print(fines)
    else:
        print(user)
        member = Member.objects.get(user = user)
        transactions_of_member = Transaction.objects.filter(member =member).all()
        fines = Fine.objects.filter(transaction__in = transactions_of_member).all()
        # print("jud", fines)
    return render(request, 'Fine/view_fines.html',{'fines' : fines})
    # page where all/users fines

#  function will be called from Transactions.views.return_book()
def calculate_fines(transaction):
    print("1",transaction.return_date - transaction.issue_date)
    # if  transaction.return_date - transaction.issue_date >= timezone.timedelta(0):
    amount = (transaction.return_date -transaction.issue_date).days*5
    print(amount, transaction)
        # fine = Fine(transaction, amount)
        # print("2", fine.transaction, fine.amount)
        # fine.save()

# only librarian access
@user_passes_test(librarian_check, login_url='unauthorized-access')
def pay_fine(request, id):
    fine = Fine.objects.get(id = id)
    fine.date_paid = timezone.localdate()
    fine.save()
    return render(request, 'Fine/fine_paid.html')
    # page for entering uid to mark fine as paid
