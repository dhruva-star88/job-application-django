from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    # To fetch data from webpage
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)
            # To store in database
            Form.objects.create(first_name=first_name, last_name=last_name, email=email,
                                date=date, occupation=occupation)
            # To send mail
            message_body = f"Thank you for your Submission, {first_name}"
            email_msg = EmailMessage("Email Confirmation",
                                      message_body,to=["dhruvatej6565@gmail.com"])
            email_msg.send()
            # To display a message
            messages.success(request=request, message="Form Submitted Successfully")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")