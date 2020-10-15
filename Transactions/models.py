from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from lib.models import Books

# class Transaction(models.Model):
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	book = models.ForeignKey(Books, on_delete = models.CASCADE)
# 	issue_date = models.DateTimeField(default=timezone.now())
# 	return_date = models.DateTimeField()
