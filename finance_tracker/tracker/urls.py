# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('add-transaction/', views.add_transaction, name='add_transaction'),
#     path('expense-summary/', views.expense_summary, name='expense_summary'),
#     path('budget-tracking/', views.budget_tracking, name='budget_tracking'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('add-transaction/', views.add_transaction, name='add_transaction'),
#     path('expense-summary/', views.expense_summary, name='expense_summary'),
#     path('budget-tracking/', views.budget_tracking, name='budget_tracking'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),  # Changed this line
    path('dashboard/', views.dashboard, name='dashboard'),  # Added this line
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('expense-summary/', views.expense_summary, name='expense_summary'),
    path('budget-tracking/', views.budget_tracking, name='budget_tracking'),
    # path('api/', views.api_hello, name='api_hello'),
    path('transactions/', views.transaction_list, name='transaction_list'),

]