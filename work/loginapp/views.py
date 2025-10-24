from django.shortcuts import render

def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        errors = {}

        
        if not username:
            errors['username'] = 'Please enter your username.'

        
        if not email or '@' not in email or '.' not in email:
            errors['email'] = 'Please enter a valid email address.'
        elif email.lower().endswith('@gmail.com'):
            errors['email'] = 'Gmail addresses are not allowed.'

        
        if len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'


        if not errors:
            return render(request, 'loginapp/welcome.html', {
                'username': username,
                'email': email
            })

        
        context['errors'] = errors
        context['username'] = username
        context['email'] = email
        context['password'] = password

    return render(request, 'loginapp/login.html', context)
