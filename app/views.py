from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    template = loader.get_template('app/index.html')
    context = { 'user' : request.user }
    return HttpResponse(template.render(context, request))

@login_required
def about(request):
    template = loader.get_template('app/about.html')
    context = { 'user' : request.user, 'userinfo': request.session['userinfo'] if 'userinfo' in request.session.keys() else None }
    return HttpResponse(template.render(context, request))
