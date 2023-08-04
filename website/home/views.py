from django.shortcuts import render, redirect, HttpResponse
from .models import Message
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        msg = Message.objects.create(email=email, subject=subject, message=message)
        msg.save();
        return redirect('success')
    
    else:
        return render(request, 'index.html')
    

def success(request):
    return render(request, 'success.html')