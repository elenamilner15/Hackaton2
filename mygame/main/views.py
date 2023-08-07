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


# def show_verb2(request, part_of_speech):
#     users = verbs.objects.filter(part_of_speech=part_of_speech)[:15]
    
#     paginator = Paginator(users, 1)  # Each page will contain one item
#     page_number = request.GET.get('page')
#     page_users = paginator.get_page(page_number)

#     return render(request, 'main/show_verb2.html', {'page_users': page_users})


def show_verb2(request, part_of_speech):
    users = verbs.objects.filter(part_of_speech=part_of_speech)[:15]  # Use your Verb model
    paginator = Paginator(users, 1)  # Each page will contain one item
    page_number = request.GET.get('page')
    page_users = paginator.get_page(page_number)

    feedback = None  # Initialize feedback to None

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        correct_answer = page_users.object_list[0].niqqud_stripped_word

        if user_input.lower() == correct_answer:
            # user = request.user  # Get the current user
            # user.increase_score()  # Increase the user's score
            feedback = "Correct!"
        else:
            feedback = "Incorrect. Try again."

    context = {
        'page_users': page_users,
        'feedback': feedback,
    }

    return render(request, 'main/show_verb2.html', context)

 

def home(response):
	return render(response, "main/home.html", {})

def account(response):
	return render(response, "main/account.html", {})

def round1(response):
	return render(response, "main/round1.html", {})

def round2(response):
	return render(response, "main/round2.html", {})






    
    


