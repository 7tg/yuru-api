from django.contrib import admin
from api.models import (
    User,
    Step,
    Company,
    Campaign,
    Participant,
    Winner,
    Coupon,
    )

# Register your models here.
admin.site.register(User)
admin.site.register(Step)
admin.site.register(Company)
admin.site.register(Campaign)
admin.site.register(Participant)
admin.site.register(Winner)
admin.site.register(Coupon)