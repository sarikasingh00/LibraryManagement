from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
is_type = (
	('Students','Students'),
	('Teachers','Teachers'),
	)
class Librarian(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE)
	# librarian_id = models.CharField(primary_key='True',max_length=60)
	librarian_name = models.CharField(max_length=100)
	librarian_dob = models.DateField(default=timezone.now().strftime('%Y-%m-%d'))

	def __str__(self):
		return self.librarian_name

class Member(models.Model):
	# hi yug
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	is_type = models.CharField(max_length=50,choices=is_type,default='Students')
	# member_id = models.CharField(primary_key='True',max_length=55)
	member_name = models.CharField(max_length=100)
	member_department = models.CharField(max_length=50)
	# member_number = models.CharField()

	def __str__(self):
		return self.member_name
