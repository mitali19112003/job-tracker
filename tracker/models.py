from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self): 
        return self.name

class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=[
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ])
    applied_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.company}"