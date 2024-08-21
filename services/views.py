from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Prepare the email content
            subject = f"Contact Form Submission from {form.cleaned_data['name']}"
            message = f"Message:\n{form.cleaned_data['message']}\n\nFrom: {form.cleaned_data['name']} ({form.cleaned_data['email']})"
         #   email = form.cleaned_data['email']

            # Send the email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Using your Mailgun user as the sender
                ['jenntech23@gmail.com'],  # Replace with your recipient email(s)
                fail_silently=False,
            )
            # Redirect after successful submission
            return redirect('contactSubmitted')  # Use the view name instead of a template
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form})  # Include the correct template name


def contactSubmitted(request):
    return render(request, 'contact_submitted.html')


def privacyPolicy(request):
    return render(request, 'privacyPolicy.html')