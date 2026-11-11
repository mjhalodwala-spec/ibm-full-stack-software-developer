from django.db import models
class Project(models.Model):
    class Status(models.TextChoices):
        PLANNING = "planning", "Planning"
        ACTIVE = "active", "Active"
        BLOCKED = "blocked", "Blocked"
        COMPLETE = "complete", "Complete"
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, max_length=2000)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PLANNING)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["due_date", "-updated_at"]
    def __str__(self): return self.title
