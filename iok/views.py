from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *

# Create your views here.

def HomeView(request):
    team_objects = TeamPointTable.objects.all()
    
    names = []
    points = []

    for i in team_objects:
        names.append(i.name)
        points.append(i.points)

    merged_list = [(names[i], points[i]) for i in range(0, len(names))] 
    merged_list.sort(key= lambda x: x[1], reverse=True)

    slider_typing_objects = Typing_on_slider.objects.all()
    idare_heyeti_objects = Idare_heyeti.objects.all()
    slider_objects = Slider.objects.all()
    legend_president_objects = Legend_president.objects.all()
    legend_teams_objects = legend_teams.objects.all()
    about_us_objects = About_u.objects.all()
    quiz_objects = Quiz.objects.all()
    media_objects = Media_links.objects.all()

    answers = []

    
    my_dict = {
        'answers':answers,
        'teams': merged_list,
        'typings': slider_typing_objects,
        'idare_heyeti':idare_heyeti_objects,
        'sliders':slider_objects,
        'legend_prezs':legend_president_objects,
        'legent_teams':legend_teams_objects,
        'about_us':about_us_objects,
        'quiz': quiz_objects,
        'media': media_objects
    }
    return render(request, 'index.html', context= my_dict)
