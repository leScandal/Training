# -*- coding: utf-8 -*-
from sys import maxsize
class Contacts:


    def __init__(self, name=None, middleN=None, lastN=None, nickN=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None, HP=None, address2=None, address3=None, notes=None, id=None):
        self.name = name
        self.middleN = middleN
        self.lastN = lastN
        self.nickN = nickN
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.HP = HP
        self.address2 = address2
        self.address3 = address3
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.lastN, self.id) #self.address,


    def __eq__(self, other):
        return self.name == other.name and self.lastN == other.lastN and (self.id is None or other.id is None or self.id == other.id) and (self.address == other.address or self.address is None or other.address is None)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize