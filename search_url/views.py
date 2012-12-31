# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from lib import url, html, synology, extension, links
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from search_url.models import synology_conf
import re

class run:
    def __init__(self, url_in, ext=[], forb=[]):
        try:
            self.url = url.url(url_in)
        except url.InvalidProtocol:
            print "Has introducido una URL Incorrecta"
        except url.URLError:
            print "La URL que has introducido no existe"
        self.extensions = extension.extension(ext)
        self.forbbiden = extension.extension(forb)
    def check(self):
        if self.url.isValidURL():
            url_content = self.url.returnUrlContent()

            allLinks = html.html(url_content)
            allLinks = allLinks.findLinks()
            validLinks = self.extensions.searchExtension(allLinks)
            forb = self.forbbiden.getExtension()
            print validLinks
            if forb:
                for f in forb:
                    if f in validLinks:
                        print f
                        print 'borro'
                        validLinks.remove(f)

            validLinks = html.listOfExceptions().check(validLinks, self.url.getURL())
            return validLinks



def home(request):
    result = ''
    if request.method == 'POST':
        form = request.POST
        url = form['url']
        ext = form['ext']
        ext = re.split(',', ext)
        forb = form['forb']
        forb = re.split(',', forb)
        r = run(url, ext, forb)
        result = r.check()
        sy_conf = synology_conf.objects.all()
        t = 'respuesta.html'
        d = {
            'resultado': result,
            'synology': sy_conf
        }
        c = RequestContext(request)
    elif request.method == 'GET':
        if request.GET:
            option = request.GET['synology']
            result = request.GET['links']
            result = re.split('\n', result)
            s = synology_conf.objects.get(pk=option)
            url = 'http://' + str(s.ip_diskstation) + ':' + str(s.port)
            syno = synology.synology(url, s.usuario, s.password)
            toAdd = ''
            for download in result:
                download = download.replace('\r','')
                toAdd += download + ', '
            print toAdd
            if (syno.addDownload(toAdd)):
                d = {
                    'ok': True
                }
            else:
                d = {
                    'ok': False
                }

            t = 'respuesta.html'
            c = RequestContext(request)
        else:
            t = 'index.html'
            d = {}
            c = RequestContext(request)
            
        
    
    return render_to_response(t, d, context_instance=c)
