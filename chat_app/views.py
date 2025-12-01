from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from .models import Chat
import json

# Create your views here.

@csrf_exempt
def chat_view(request):
    if request.method == "GET":
        chats = list(Chat.objects.values())
        return JsonResponse(chats, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)
        chat = Chat.objects.create(
            name=data.get("name"),
            message=data.get("message"),
            created_at=now()
        )
        return JsonResponse({"id": chat.id, "name": chat.name, "message": chat.message})