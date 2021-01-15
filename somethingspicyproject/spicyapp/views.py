from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    print(request.POST)
    # code for  registration
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        hash_browns = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hash_browns)
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            user_name=request.POST['user_name'],
            email = request.POST['email'],
            password = hash_browns
        )
        # redirect to a success route
        request.session['uuid'] = user.id
        return redirect('/main')

def login(request):
    print(request.POST)
    # code for  registration
    errors = User.objects.login_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        user = User.objects.get(email=request.POST['email'])
        print(user)
        # redirect to a success route
        request.session['uuid'] = user.id
        return redirect('/main')

def main_page(request):
    context = {
        'user': User.objects.get(id=request.session['uuid']),
        'sug': Suggestion.objects.all()
    }
    return render(request, 'main.html', context)

def videos(request):
    context = {
        'user': User.objects.get(id=request.session['uuid']),
        'video1' : Videoone.objects.all(),
        'video2' : Videotwo.objects.all(),
        'video3' : Videothree.objects.all(),
        'comments' : Comment.objects.all(),
    }
    return render(request, 'video.html', context)

def commentvideo1(request, id):
    Videoone.objects.create(
        username = User.objects.get(id=id),
        video1 = request.POST['video1']
    )
    return redirect('/videos')
def like(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videoone.objects.get(id=id)
    paper.likes.add(logged_user)
    paper.save()
    return redirect('/videos')

def unlike(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videoone.objects.get(id=id)
    paper.likes.remove(logged_user)
    paper.save()
    return redirect('/videos')

def commentvideo2(request, id):
    Videotwo.objects.create(
        username = User.objects.get(id=id),
        video2 = request.POST['video2']
    )
    return redirect('/videos')

def like2(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videotwo.objects.get(id=id)
    paper.likes.add(logged_user)
    paper.save()
    return redirect('/videos')

def unlike2(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videotwo.objects.get(id=id)
    paper.likes.remove(logged_user)
    paper.save()
    return redirect('/videos')

def commentvideo3(request, id):
    Videothree.objects.create(
        username = User.objects.get(id=id),
        video3 = request.POST['video3']
    )
    return redirect('/videos')

def like3(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videothree.objects.get(id=id)
    paper.likes.add(logged_user)
    paper.save()
    return redirect('/videos')

def unlike3(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Videothree.objects.get(id=id)
    paper.likes.remove(logged_user)
    paper.save()
    return redirect('/videos')

def suggest(request, id):
    Suggestion.objects.create(
        member = User.objects.get(id=id),
        video_game=request.POST['video_game'],
        description = request.POST['description']
    )
    return redirect('/main')

def like_suggest(request, id):
    sug = Suggestion.objects.get(id=id)
    user = User.objects.get(id=request.session['uuid'])
    sug.like.add(user)
    sug.save()
    return redirect('/main')

def delete_suggest(request, id):
    sug=Suggestion.objects.get(id=id)
    sug.delete()
    return redirect('/main')

def logout(request):
    request.session.flush()
    return redirect('/')

def forum(request):
    context = {
        'user': User.objects.get(id=request.session['uuid']),
        'comments' : Comment.objects.all(),
    }
    return render(request, 'forum.html', context)

def forumpost(request, id):
    Comment.objects.create(
        user = User.objects.get(id=id),
        description = request.POST['description']
    )
    return redirect('/forum')

def forumlike(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Comment.objects.get(id=id)
    paper.likes.add(logged_user)
    paper.save()
    return redirect('/forum')

def forumunlike(request, id, done):
    logged_user = User.objects.get(id=done) 
    paper = Comment.objects.get(id=id)
    paper.likes.remove(logged_user)
    paper.save()
    return redirect('/forum')