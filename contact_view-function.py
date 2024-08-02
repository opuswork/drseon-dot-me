"""
contact_view function : sending email
"""


def contact_view(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        sender_phone = request.POST.get('sender_phone')
        message = request.POST.get('sender_message')  # Updated to 'message'

        subject = f'email from {sender_name}, {sender_email}'
        body = f'Name: {sender_name}\nEmail: {sender_email}\nPhone: {sender_phone}\n\nMessage:\n{message}'

        print('Form submitted')
        print(f'Sender Name: {sender_name}')
        print(f'Sender Email: {sender_email}')
        print(f'Sender Phone: {sender_phone}')
        print(f'Message: {message}')

        try:
            send_mail(subject, body, sender_email, [settings.DEFAULT_FROM_EMAIL])
            return HttpResponse('Thank you for your message. We will get back to you soon.')
        except Exception as e:
            print(f'Error sending email: {e}')
            return HttpResponse('Error sending email. Please try again later.')
    return render(request, 'contact.html')
