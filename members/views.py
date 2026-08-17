from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.utils.translation import gettext as _

def main(request):
  message = _("Welcom to the site")
  return render(request, 'details.html', {"message": message})
  
def my_view(request):
  return render(request, 'members/all_members.html')

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember' : mymember,
  }
  return HttpResponse(template.render(context, request))



# Create your views here.





