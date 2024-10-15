from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Category(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class Transaction(models.Model):
#     TRANSACTION_TYPES = (
#         ('income', 'Income'),
#         ('expense', 'Expense'),
#     )
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     description = models.CharField(max_length=255)
#     date = models.DateField()
#     transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    
#     def __str__(self):
#         return f"{self.user.username} - {self.amount} - {self.category}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    description = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.date} - {self.description} - ${self.amount}"


class Budget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

@receiver(post_save, sender=Transaction)
def update_budget(sender, instance, created, **kwargs):
    if created:
        budget, _ = Budget.objects.get_or_create(user=instance.user)
        if instance.transaction_type == 'income':
            budget.total_budget += instance.amount
        else:
            budget.total_budget -= instance.amount
        budget.save()
