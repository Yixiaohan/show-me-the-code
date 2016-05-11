# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect
from models import MessageBoard
from django.views.decorators.csrf import csrf_exempt
import json
from django import forms


# Create your views here.
def message_board(request):
    message_list = MessageBoard.objects.all().order_by('-pk')
    return render(request, 'message_board.html', {'message_list': message_list})


class MessageForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200)


@csrf_exempt
def message_submit(request):
    if request.method == 'POST':
        f = MessageForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            message = f.cleaned_data['message']
        else:
            return message_board(request)

    if message != '':
        save_message = MessageBoard()
        save_message.name = name
        save_message.message = message
        save_message.save()
        return redirect(r'http://127.0.0.1:8080/message_board')
    else:
        return json.dumps({
            'status': 400001,  # null message
            'message': "null message can't save",
        })


# @login_required
@csrf_exempt
def test(request):
    if request.user.is_authenticated():
        resp = {
            'status': 200,
            'message': 'ok',
        }
    else:
        resp = {
            'status': 400001,
            'message': 'not ok',
        }

    return json.dumps(resp)
