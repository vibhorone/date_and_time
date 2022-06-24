from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    date = str(datetime.now().date())
    time = str(datetime.now().time())
    html = f'''
    <html>
        <body>
            <h1>Current date and time is as below</h1>
            <h3>Date: {date}</h3>
            <h3>Time: {time}</h3>
        </body>
    </html>
    '''
    return HttpResponse(html)

