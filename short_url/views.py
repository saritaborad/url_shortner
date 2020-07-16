from django.shortcuts import render,get_object_or_404,redirect
from .models import Link
from django.views.generic import View
from .utils import get_shortcode
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
# from short_url.decorator import login_check


@method_decorator(login_required, name='post')
class ShortUrlView(View):
    template_name = 'home.html'

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
            url_input = request.POST.get('url')
            user1 = request.user
            url_exists = Link.objects.filter(long_url=url_input,user=user1).exists()
            shortcode = get_shortcode(request,url_exists,url_input)
            shorten_url = request.build_absolute_uri(shortcode)
            context = {'l_url': url_input,'short_code': shortcode}
            return render(request, self.template_name,context)

class UrlRedirectView(View):
    def get(self,request,shortcode = None,*args,**kwargs):
        obj = get_object_or_404(Link,shortcode=shortcode)
        obj.visits = obj.visits + 1
        obj.save()
        return HttpResponseRedirect(obj.long_url)


