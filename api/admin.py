from django.contrib import admin
from api.models import User, Step, Company, Campaign, Participant

# Register your models here.
admin.site.register(User)
admin.site.register(Step)
admin.site.register(Company)
admin.site.register(Campaign)
admin.site.register(Participant)