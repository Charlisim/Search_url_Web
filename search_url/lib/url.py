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
import requests


class InvalidProtocol(Exception):
    pass


class URLError(Exception):
    pass


class url:
    ''' All necesary to send a request to server and return content of webpage '''
    def __init__(self, url=''):
        self.VALID_PROTOCOLS = ['http://', 'https://']
        self.url = self.checkURL(url)

    ''' Check if url is in the valid protcols.
        Check if url starts with www and add http protocol
        If is not a valid protocol raise an InvalidProtocol Exception
     '''
    def checkURL(self, url=''):
        url_fixed = ''
        if not url:
            url = self.url
        for protocol in self.VALID_PROTOCOLS:
            if not url.startswith(protocol):
                if url.startswith('www'):
                    url_fixed = self.VALID_PROTOCOLS[0] + url
                    break
            else:
                url_fixed = url
                break
        if not url_fixed:
            raise InvalidProtocol()
        else:
            return url_fixed

    def returnUrlContent(self, url=''):
        if not url:
            url = self.url

        try:
            r = requests.get(url)
            if r.status_code == requests.codes.ok:
                return r.content
            else:
                raise URLError()
        except:
            raise URLError()

    def isValidURL(self, url=''):
        if not url and self.url:
            url = self.url
        try:
            if self.checkURL(url):
                return True
            else:
                return False
        except:
            return False

    def getURL(self):
        return self.url

