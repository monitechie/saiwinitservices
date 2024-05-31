from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


# Corrected function definition
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        mobile = request.POST['mobile']
        msg = f"Message from {name}\nEmail: {email}\nMobile: {mobile}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,  # Subject of the email
                msg,  # Message body
                email,  # From email
                ['smonicse@gmail.com'],  # Recipient list
                fail_silently=False
            )
            return render(request, 'contact.html', {'success_msg': 'Thank you for your message. We will get back to you shortly.'})
            # return HttpResponse('Thank you for your message. We will get back to you shortly.')
        except Exception as e:
            # return HttpResponse(f'An error occurred: {e}')
            return render(request, 'contact.html', {'error_msg': f'An error occurred: {e}'})
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')
