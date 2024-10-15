from django.contrib import admin
from .models import Category, Transaction, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'description', 'date', 'transaction_type')
    list_filter = ('user', 'category', 'transaction_type', 'date')
    search_fields = ('description', 'user__username')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_budget')
