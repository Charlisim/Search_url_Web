# -*- coding: utf-8 -*-

'''

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Created on 09/12/2012

    @author: Carlos Simón <jcarlosimonv@gmail.com>
'''
import re
from bs4 import BeautifulSoup
from url import *


class html:
    def __init__(self, content):
        self.content = BeautifulSoup(content)


    ''' return valid links '''
    def findLinks(self):
        allLinks = self.content.findAll('a')
        validLinks = []
        for link in allLinks:
            try:
                validLinks.append(link['href'])
            except KeyError:
                pass

        return validLinks

    ''' return links that contain extensions'''
    def findLinksExtension(self, links, extensions):
        linksExtension = []
        for link in links:
            for ext in extensions:
                if ext in link:
                    linksExtension.insert(link)
        return linksExtension


class listOfExceptions:
    def __init__(self):
        ''' Not move order, in check method use this order '''
        self.WEBS = ["cs50.tv", "/descargar.php"]

    def fix_CS50(self, url_toFix):
        ''' Search links of this page and look out for valid url
            Return only one URL. '''
        validURL = ''
        if '2012' in url_toFix:
            validURL = re.sub('http://cs50.tv', 'http://downloads.cs50.net', url_toFix)
        else:
            DOWNLOADS_VALUES = ['#download', '?download']
            try:
                ''' Call to url class and return HTML code of page '''
                cs50 = url(url_toFix).returnUrlContent()
                ''' Store all links '''
                links = html(cs50).findLinks()
                ''' Search all valid links '''
                for link in links:
                    for value in DOWNLOADS_VALUES:
                        if value in link:
                            validURL = link
            except:
                pass
        return validURL

    def fixMejorEnVo(self, url_toFix, origin):
        fixUrl = ''
        if 'mejorenvo.com' in origin:
            fixUrl = 'http://www.mejorenvo.com' + url_toFix
        return fixUrl

    def check(self, urls, origin):
        self.url = []
        for url in urls:
            if self.WEBS[0] in url:
                self.url.append(self.fix_CS50(url))
            if self.WEBS[1] in url:
                if 'descargar' in url:
                    self.url.append(self.fixMejorEnVo(url, origin))
            else:
                self.url.append(url)
        return self.url




