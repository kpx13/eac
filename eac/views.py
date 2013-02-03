# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from pages.models import Page
from news.models import Article
from slideshow.models import Slider
from projects.models import Project
from experts.models import Expert
from partners.models import Partner

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['user'] = request.user
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slideshow'] = Slider.objects.all()
    c['content'] = Page.get_by_slug('home')['content']
    c['news'] = Article.recent_some(5)
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def news_page(request, page_name=None):
    c = get_common_context(request)
    if (request.method == 'GET') or not request.POST.get('search_value', None):
        try:
            if page_name:
                c['recent'] = Article.get_by_slug(page_name)
            else:
                c['recent'] = Article.recent_some(1)[0]
            c['news'] = Article.recent_some(5)
            return render_to_response('news.html', c, context_instance=RequestContext(request))
        except:
            raise Http404('page %s not found' % page_name)
    else: # POST
        c['search_value'] = request.POST['search_value']
        c['news'] = Article.find(c['search_value'])
        if len(c['news']) > 0:
            c['recent'] = c['news'][0]
        else:
            c['not_found'] = True
        return render_to_response('news.html', c, context_instance=RequestContext(request))

def projects_page(request, page_name=None):
    c = get_common_context(request)
    if page_name is None:
        c['projects'] = Project.objects.all()
        return render_to_response('projects.html', c, context_instance=RequestContext(request))
    else:
        try:
            c['project'] = Project.get_by_slug(page_name)
            return render_to_response('project_details.html', c, context_instance=RequestContext(request))
        except:
            raise Http404('page %s not found' % page_name)
        
def experts_page(request, page_name=None):
    c = get_common_context(request)
    c['experts'] = Expert.objects.all()
    return render_to_response('experts.html', c, context_instance=RequestContext(request))

def partners_page(request, page_name=None):
    c = get_common_context(request)
    c['partners'] = Partner.objects.all()
    return render_to_response('partners.html', c, context_instance=RequestContext(request))

def leaders_page(request, page_name=None):
    c = get_common_context(request)
    c['f'] = Page.get_by_slug('leader_f')
    c['s'] = Page.get_by_slug('leader_s')
    return render_to_response('leaders.html', c, context_instance=RequestContext(request))

def page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404('page %s not found' % page_name)
