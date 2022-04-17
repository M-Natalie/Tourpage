from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

#def homepage(request):
#    return render(request, 'index.html')

#class HomeView(View):
#    def get(self, request, *args, **kwargs):
#        return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'

def profile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'profile.html', {'profile': profile_object}) 