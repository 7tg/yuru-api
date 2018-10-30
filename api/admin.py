from django.contrib import admin
from api.models import (
    User,
    Step,
    Company,
    Campaign,
    Participant,
    Winner,
    Coupon,
    Achivement,
    AchivementList,
    )

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mail', 'birth_date', 'get_age', 'gender', 'id')
    search_fields = ('first_name', 'last_name', 'mail')
    list_filter = ('birth_date','gender')

class StepAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'step')
    list_filter = ('date',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'tel', 'id')
    search_fields = ('name', 'mail')

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'capacity', 'capacity_taken', 'is_closed', 'id')
    search_fields = ('name', 'company')
    list_filter = ('is_closed',)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'campaign')

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'campaign', 'is_used')
    list_filter = ('is_used',)

class WinnerAdmin(admin.ModelAdmin):
    list_display = ('participant', 'coupon')

class AchivementListAdmin(admin.ModelAdmin):
    list_display = ('user', 'achivement')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Winner, WinnerAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Achivement)
admin.site.register(AchivementList, AchivementListAdmin)

