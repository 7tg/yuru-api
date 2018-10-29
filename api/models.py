from django.db import models

# Create your models here.
class User(models.Model):
    """User model for api project"""
    first_name =    models.CharField(max_length=30)
    last_name =     models.CharField(max_length=30)
    mail =          models.EmailField(unique=True)
    birth_date =    models.DateField() # Birthdate field
    sex =           models.CharField(max_length=1) # M: For male, F: For female
    passwd =        models.CharField(max_length=64)
    salt =          models.CharField(max_length=64, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Step(models.Model):
    """Step model for api project"""
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.IntegerField()

    def __str__(self):
        return self.date.__str__()+ " ID:" + self.user.__str__() + " Steps:" + self.step.__str__()

class Company(models.Model):
    """Company model for api project"""
    name =  models.CharField(max_length=255, unique=True)
    mail =  models.EmailField()
    tel =   models.CharField(max_length=12)
    desc =  models.TextField()

    def __str__(self):
        return self.name

class Campaign(models.Model):
    """Campaign model for api project"""
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    desc = models.TextField()
    capacity = models.IntegerField()
    capacity_taken = models.IntegerField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    """Participant model for api project"""
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign.__str__() + " -- " + self.user.__str__()