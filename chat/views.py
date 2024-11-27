from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from groq import Groq
from .models import Chat

os.environ["GROQ_API_KEY"] = "api-key-here"
client = Groq(api_key=os.environ["GROQ_API_KEY"])

def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message','')
        completion = client.chat.completions.create(
            messages = [
                {'role':'system','content':'You are a helpful assistant named cat.You should act like a friendly cat like saying purr or moew at end of osme of the sentences.'},
                {'role':'user','content':message},
            
            ]
            ,model="llama3-8b-8192"
        )
        answer = completion.choices[0].message.content
        new_chat = Chat(message=message,response=answer)
        new_chat.save()
        return JsonResponse({'response':answer})
    return JsonResponse({'response':'Cat out of the nine lives x_x...(invalid response)'},status=400)
