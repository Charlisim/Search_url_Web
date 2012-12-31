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

Created on 25/11/2012

@author: Carlos Simon <jcarlosimonv@gmail.com>
'''


import requests
import json
import base64

class synology():
    def __init__(self, ip, account, password):
        self.ip = ip
        self.account = account
        self.password = password
        self.session = requests.session()
        
    def login(self):
              
        def log():           
            return self.session.post(self.ip + '/webapi/auth.cgi', data={"api": "SYNO.API.Auth", "version": "2", "method": "login", "account": self.account, "passwd": base64.b64decode(self.password), "session": "DownloadStation", "format": "cookie"})

        try:
            login = log()
        except requests.exceptions.MissingSchema:
            # If not start with 'http protocol' add http and try login again
            # TODO: Add support for https
            print 'MissingSchema'     
            self.ip = 'http://' + self.ip
            login = log()
        except requests.exceptions.ConnectionError:
            print 'Network problem'
        except requests.exceptions.HTTPError:
            print 'Invalid HTTP Response'

        if login.status_code == 404:
            # If 404 error try adding default port.
            try:            
                if self.ip.startswith('http://'):
                    print 'Only add port'
                    self.ip += ':5000'
                else:
                    print 'Add port and http'
                    self.ip = 'http://' + self.ip + ':5000'
                print 'try login....'
                login = log()
            except:
                print "URL not found. If you have a custom port you must provide it"

        if login.status_code == 200:
            print 'pasa por 200'
            try:
                o = json.loads(login.text)
                if o["success"]:
                    return True
                else:
                    error = o['error']['code']
                    if error == 400:
                        print 'No such account or incorrect password'
                    elif error == 401:
                        print 'Guest account disabled'
                    elif error == 402:
                        print 'Account disabled'
                    elif error == 403:
                        print 'Wrong password'
                    elif error == 404:
                        print 'Permission denied'
                    return False
            except ValueError:
                print 'Error with JSON'        
        
    def logout(self):
        logout = self.session.post(self.ip + '/webapi/auth.cgi', data={"api": "SYNO.API.Auth", "version": "1", "method": "logout", "session": "DownloadStation"})
        o = json.loads(logout.text)
        if o["success"]:
            return True
        else:
            print o
            return False
    def addDownload(self, url):
        if self.login():
            request = self.session.post(self.ip + '/webapi/DownloadStation/task.cgi', data={"api": "SYNO.DownloadStation.Task", "version": "1", "method": "create", "uri": url})
            o = json.loads(request.text)
            if o["success"]:
                print 'Add download/s successfully'
                return True
            else:
                error = o['error']['code']
                if error == 100:
                    print 'Unknown error'
                elif error == 101:
                    print 'Invalid parameter'
                elif error == 102:
                    print 'The requested API does not exist'
                elif error == 103:
                    print 'The requested method does not exist'
                elif error == 104:
                    print 'The requested version does not support the functionality'
                elif error == 105:
                    print 'The logged in session does not have permission'
                elif error == 106:
                    print 'Session timeout'
                elif error == 107:
                    print 'Session interrupted by duplicate login'
                print 'Could\'t add download list'
                return False
            self.logout()
            
      
            
    