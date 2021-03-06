from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from short_url.models import Link



class RegisterView(View):
    template_name = 'users/register.html'
    form = UserRegisterForm()

    def get(self,request):
        return render(request,self.template_name,{'form':self.form})

    def post(self,request):
        self.form = UserRegisterForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            username = self.form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has been created!{username}')
            return redirect('login')
        return render(request,self.template_name,{'form':self.form})


@login_required()
def profile(request,*args,**kwargs):
    user1 = request.user
    urls = Link.objects.filter(user=user1)
    return render(request, 'users/profile.html',{'url':urls})

# class SearchView(View):
#     def post(self,request):
#         search_url = request.POST.get('search_item')
#         return redirect('https://www.google.com/'+search_url)










































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































