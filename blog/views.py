from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    return render(request, "blog/post_list.html",{})

def lesson_plan(request):
    return render(request, 'blog/lesson_plan.html')

def drug_interactions(request):
    return render(request, 'blog/drug_interactions.html')

def overdose_risks(request):
    return render(request, 'blog/overdose_risks.html')

def signs_of_overdose(request):
    return render(request, 'blog/signs_of_overdose.html')

def main(request):
    return render(request, 'blog/main.html' )

def overview_stages(request):
    return render(request, 'blog/overview_stages.html')

def ethics_regulatory(request):
    return render(request, 'blog/ethics_regulatory.html')

def advances_resources(request):
    return render(request, 'blog/advances_resources.html')

def substance_abuse(request):
    return render(request, 'blog/substance_abuse.html')

def overdose_prevention(request):
    return render(request, 'blog/overdose_prevention.html')

def game_view(request):
    return render(request, 'blog/game.html')
