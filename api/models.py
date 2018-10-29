from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    """User model for api project"""
    id =       models.BigAutoField(primary_key=True)
    first_name =    models.CharField(max_length=30, null=False)
    last_name =     models.CharField(max_length=30, null=False)
    mail =          models.EmailField(unique=True, null=False)
    birth_date =    models.DateField(null=False) # Birthdate field
    sex =           models.CharField(max_length=1, null=False) # M: For male, F: For female
    passwd =        models.CharField(max_length=64, null=False)
    salt =          models.CharField(max_length=64, default="")


    def get_age(self):
        """Function for getting users age"""
        today = date.today()
        born = self.birth_date
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    get_age.short_description = 'AGE'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Step(models.Model):
    """Step model for api project"""
    date = models.DateField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.IntegerField(default=0)

    def __str__(self):
        return self.date.__str__()+ " ID:" + self.user.__str__() + " Steps:" + self.step.__str__()

class Company(models.Model):
    """Company model for api project"""
    name =  models.CharField(max_length=255, unique=True, null=False)
    mail =  models.EmailField()
    tel =   models.CharField(max_length=12)
    desc =  models.TextField()

    def __str__(self):
        return self.name

class Campaign(models.Model):
    """Campaign model for api project"""
    name =          models.CharField(max_length=255, null=False)
    company =       models.ForeignKey(Company, on_delete=models.CASCADE)
    desc =          models.TextField()
    capacity =      models.IntegerField(null=False)
    capacity_taken =models.IntegerField(default=0, null=False)
    is_closed =     models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Participant(models.Model):
    """Participant model for api project"""
    campaign =  models.ForeignKey(Campaign, null=False, on_delete=models.CASCADE)
    user =      models.ForeignKey(User, null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign.__str__() + " -- " + self.user.__str__()

class Coupon(models.Model):
    """Coupon model for api project"""
    code =      models.CharField(max_length=255, unique=True)
    campaign =  models.ForeignKey(Campaign, on_delete=models.CASCADE, unique=False)
    is_used =      models.BooleanField(default=False)

    def __str__(self):
        return self.code

class Winner(models.Model):
    """Winner model for api project"""
    participant=models.ForeignKey(Participant, on_delete=models.CASCADE)
    coupon =    models.ForeignKey(Coupon, on_delete=models.CASCADE)

    def __str__(self):
        return self.participant.__str__() + " -- " + self.coupon.__str__()

class Achivement(models.Model):
    """Achivement model for api project"""
    name =      models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AchivementList(models.Model):
    """AchivementList model for api project"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achivement = models.ForeignKey(Achivement, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__() + " -- " + self.achivement.__str__()
