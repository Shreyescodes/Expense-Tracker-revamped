from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction, Category, Budget
from .forms import TransactionForm, CategoryForm, DateRangeForm
from django.contrib import messages
from django.db.models.functions import TruncMonth


@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]
    income = Transaction.objects.filter(user=request.user, transaction_type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expenses = Transaction.objects.filter(user=request.user, transaction_type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expenses
    
    context = {
        'transactions': transactions,
        'income': income,
        'expenses': expenses,
        'balance': balance,
    }
    return render(request, 'tracker/dashboard.html', context)

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'testapp/transaction_list.html', {'transactions': transactions})


@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, 'Transaction added successfully.')
            return redirect('dashboard')
    else:
        form = TransactionForm()
    
    return render(request, 'tracker/add_transaction.html', {'form': form})

@login_required
def expense_summary(request):
    form = DateRangeForm(request.GET or None)
    transactions = Transaction.objects.filter(user=request.user)
    
    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        transactions = transactions.filter(date__range=[start_date, end_date])
    
    expenses_by_category = transactions.filter(transaction_type='expense').values('category__name').annotate(total=Sum('amount'))
    
    context = {
        'form': form,
        'expenses_by_category': expenses_by_category,
    }
    return render(request, 'tracker/expense_summary.html', context)

@login_required
def budget_tracking(request):
    budget, created = Budget.objects.get_or_create(user=request.user)
    expenses = Transaction.objects.filter(user=request.user, transaction_type='expense')
    expenses_by_month = expenses.annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
    
    context = {
        'budget': budget,
        'expenses_by_month': expenses_by_month,
    }
    return render(request, 'tracker/budget_tracking.html', context)