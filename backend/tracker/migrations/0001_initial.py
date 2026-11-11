from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(name="Project", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=120)), ("description", models.TextField(blank=True, max_length=2000)), ("status", models.CharField(choices=[("planning", "Planning"), ("active", "Active"), ("blocked", "Blocked"), ("complete", "Complete")], default="planning", max_length=12)), ("due_date", models.DateField(blank=True, null=True)), ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True))], options={"ordering":["due_date","-updated_at"]})]
