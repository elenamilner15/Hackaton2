# views.py
from gc import get_objects
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, verbs
from django.views.generic import DetailView


from django.core.paginator import Paginator

def show_verb(request, part_of_speech):
    users = verbs.objects.filter(part_of_speech=part_of_speech)[:15]
    
    paginator = Paginator(users, 1)  # Each page will contain one item
    page_number = request.GET.get('page')
    page_users = paginator.get_page(page_number)

    return render(request, 'main/show_verb.html', {'page_users': page_users})


def show_verb2(request, part_of_speech):
    users = verbs.objects.filter(part_of_speech=part_of_speech)[:15]
    
    paginator = Paginator(users, 1)  # Each page will contain one item
    page_number = request.GET.get('page')
    page_users = paginator.get_page(page_number)

    return render(request, 'main/show_verb2.html', {'page_users': page_users})




# def show_next_user(request, specific_name, user_id):
#     users = User.objects.filter(username=specific_name)
#     user = get_object_or_404(users, id=user_id)
#     next_user = users.filter(id__gt=user.id).first()
#     return render(request, 'show_user.html', {'user': user, 'next_user': next_user, 'specific_name': specific_name})


# def show_next_user(request, specific_name):
#     user_ids = request.session.get('specific_name_users', [])
#     index = request.session.get('specific_name_index', 0)

  

def home(response):
	return render(response, "main/home.html", {})

def account(response):
	return render(response, "main/account.html", {})

def round1(response):
	return render(response, "main/round1.html", {})

def round2(response):
	return render(response, "main/round2.html", {})






    
    


