from django.db import migrations

def add_initial_categories(apps, schema_editor):
    Category = apps.get_model('tracker', 'Category')
    categories = ['Food', 'Transportation', 'Housing', 'Utilities', 'Entertainment', 'Healthcare', 'Personal', 'Education', 'Savings', 'Debt']
    for category_name in categories:
        Category.objects.create(name=category_name)

def remove_initial_categories(apps, schema_editor):
    Category = apps.get_model('tracker', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),  # Replace with the name of your last migration file
    ]

    operations = [
        migrations.RunPython(add_initial_categories, remove_initial_categories),
    ]