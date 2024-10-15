from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category")

    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'description', 'date', 'transaction_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
