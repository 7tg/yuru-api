from django.urls import path
from .views import current_datetime

urlpatterns = [
    path('time/', current_datetime),

    ## User
    path('user/register/', current_datetime),
    path('user/login', current_datetime),
    path('user/logout', current_datetime),

    ## Steps
    path('step/', current_datetime),

    ## Company
    path('company/', current_datetime),

    ## Campaign
    path('campaign/', current_datetime),

    ## Participant
    path('participant/', current_datetime),

    ## Coupon
    path('coupon/', current_datetime),

    ## Winner
    path('winner/', current_datetime),

    ## Achivement
    path('achivement/', current_datetime),

    ## AchivementList
    path('achivementlist/', current_datetime),



]