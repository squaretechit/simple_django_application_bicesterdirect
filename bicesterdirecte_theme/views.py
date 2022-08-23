from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import information


class BicesterdirectTheme:

    def home(request):
        return render(request, 'home.html')

    def privacy_policy(request):
        return render(request, 'privacy-policy.html')

    def contact(request):
        if request.method == 'POST':
            full_name = request.POST['name']
            Email_Address = request.POST['email']
            Message = request.POST['text']
            
            mail = ('My name is ' + full_name + ',' + ' My Email is ' + Email_Address + ',' + ' My message is ' + Message)
            
            send_mail('Message from bicesterdirect.com', mail, 'admin@bicesterdirect.com', ['gyruapp@gmail.com'], fail_silently=False,)
            client_info = information(Name=full_name, Email=Email_Address, Message=Message)
            client_info.save()
            
            messages.info(request, 'Thank you! We will contact you soon.')
            return redirect('contact')
            
        else:
            return render(request, 'contact.html')
