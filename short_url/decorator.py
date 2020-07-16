from django.contrib import messages
from django.shortcuts import redirect

def login_check(func):
    def wrapper(request, *args, **kwargs):
        try:
            if request.user==None or request.user==AnonymousUser:
                print(request.user)
                messages.error(request, f'Login required to access Url service')
                return func(request, *args, **kwargs).as_view()
            else:
                print(request.user)
                return redirect('profile')
        except Exception as e:
            print(e)
    return wrapper

