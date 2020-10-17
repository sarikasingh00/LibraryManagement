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
    else:
        member = Member.objects.get(user = user)
        transactions_of_member = Transaction.objects.all(member =member)
        fines = Fine.objects.all(transaction = transactions_of_member)
    return render(request, 'Fine/view_fines.html',{'fines' : fines})
    # page where all/users fines

#  function will be called from Transactions.views.return_book()
def calculate_fines(transaction):
    if  transaction.retrun_date - transaction.issue_date > 7:
        amount = (transaction.retrun_date -transaction.issue_date)*5
        fine = Fine(transaction, amount)
        fine.save()

# only librarian access
@user_passes_test(librarian_check, login_url='unauthorized-access')
def pay_fine(request, id):
    fine = Fine.objects.get(id = id)
    fine.date_paid = timezone.now()
    fine.save()
    return render(request, 'Fine/fine_paid.html')
    # page for entering uid to mark fine as paid
