from django.shortcuts import render, redirect
from .models import Entry
from django.utils import timezone

# Create your views here.

def index(request):
    entries = Entry.objects.all()
    context = { 'entries': entries }
    return render(request, 'diary/index.html', context)

def viewdiary(request, diary_id):
    entry = Entry.objects.get(pk=diary_id)
    context = { 'entry': entry}
    return render(request, 'diary/viewdiary.html', context)

def save(request):
    subject = request.POST['subject']
    body = request.POST['body']

    if request.POST['new_flag'] == '1':
        e = Entry(subject=subject, body=body, pub_date=timezone.now())  
        e.save()
    elif request.POST['new_flag'] == '0':
        e = Entry.objects.get(pk=int(request.POST['entry_id']))
        e.subject = subject
        e.body = body
        e.pub_date = timezone.now()
        e.save()

    return redirect('index')

def amend(request, diary_id):
    entry = Entry.objects.get(pk=diary_id)
    context = { 'entry' : entry }
    return render(request, 'diary/amend.html', context)

def delete(request, diary_id):
    entry = Entry.objects.get(pk=diary_id)
    entry.delete()

    return redirect('index')


