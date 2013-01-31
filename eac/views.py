# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pages.models import Page

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['user'] = request.user
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    return render_to_response('home.html', c, context_instance=RequestContext(request))
        
def page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_page_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404('page %s not found' % page_name)
