from django.shortcuts import render

def login_view(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        errors = {}

        # Email validation
        if not email or '@' not in email or '.' not in email:
            errors['email'] = 'Please enter a valid email address.'
        elif email.lower().endswith('@gmail.com'):
            errors['email'] = 'Gmail addresses are not allowed.'

        # Password validation
        if len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'

        # If all valid → show thank you message
        if not errors:
            return render(request, 'loginapp/welcome.html', {'email': email})

        # If invalid → send errors back
        context['errors'] = errors
        context['email'] = email
        context['password'] = password

    return render(request, 'loginapp/login.html', context)
