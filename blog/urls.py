from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name ="post_list"),
    path('lesson-plan/', views.lesson_plan, name='lesson_plan'),
    path('drug-interactions/', views.drug_interactions, name='drug_interactions'),
    path('overdose-risks/', views.overdose_risks, name='overdose_risks'),
    path('signs-of-overdose/', views.signs_of_overdose, name='signs_of_overdose'),
    path('main/', views.main, name='main'),
    path('overview-stages/', views.overview_stages, name='overview_stages'),
    path('ethics-regulatory/', views.ethics_regulatory, name='ethics_regulatory'),
    path('advances-resources/', views.advances_resources, name='advances_resources'),
    path('substance-abuse/', views.substance_abuse, name='substance_abuse'),
    path('overdose-prevention/', views.overdose_prevention, name='overdose_prevention'),
]
