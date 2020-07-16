import string,secrets
from .models import Link
from django.contrib import messages


#rgeeksforgeeks
# returns random string of 7 char
def build_short():
    build_string = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(7))
    return build_string



# #  return corresponding shortcode to that url
def code_gen():
    new_short_code = build_short()
    qs_exists = Link.objects.filter(shortcode=new_short_code).exists()
    if qs_exists:
        return code_gen()
    return new_short_code

def get_shortcode(request,user_exists,url_input):
    if user_exists:
        messages.info(request,f'URL Already Exists!!')
        url_obj = Link.objects.get(long_url=url_input)
        return url_obj.shortcode
    else:
        user2 = request.user
        print(user2)
        shortcode_new = code_gen()
        new_url = Link.objects.create(long_url=url_input,shortcode=shortcode_new,user=user2)
        print('user created')
        new_url.save()
        messages.success(request,f'Your URL Is Shorted Successfully!')
        return new_url.shortcode






































































































































