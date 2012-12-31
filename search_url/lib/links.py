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



class listLinks:
    def __init__(self):
        self.lineList = ''
        self.commaList = ''
        self.setList = []

    def insertElement(self, element):
        if type(element) == str:
            self.lineList += '\n' + element
            self.commaList += ',' + element
            self.setList.insert(element)
        if type(element) == list:
            self.setList = element
            for e in element:
                self.lineList += '\n' + e
                self.commaList += ',' + e

    def getLineList(self):
        return self.lineList[1:]

    def getCommaList(self):
        return self.commaList[1:]

    def getSetList(self):
        return self.setList
