from django.shortcuts import render, redirect
from .models import Message

# Create your views here.
def board(r):
    messages = Message.objects
    return render(r, 'board.html', {'messages':messages})

def submit(r):
    m = Message()
    m.content = r.GET['content']
    m.date = r.GET['date']
    m.writer = r.GET['writer']
    m.save()
    return redirect('/')

