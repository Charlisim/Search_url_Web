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


class extension:

    ''' Constructor of extension.
        @param extension is optional
    '''
    def __init__(self, extension=[]):
        self.extension = extension

    ''' Returns Extension '''
    def getExtension(self):
        return self.extension

    ''' Set Extension '''
    def setExtension(self, extension):
        self.extension = extension

    ''' Search if passed url contains some of the extensions
        Returns urls that contains extension
    '''
    def searchExtension(self, urls):
        urlExt = []
        for url in urls:
            for extension in self.extension:
                if extension in url:
                    urlExt.append(url)
        return urlExt

    def restExtensions(self, ext):
        for e1 in self.extension:
            if e1 in ext:
                self.extension.remove(e1)


