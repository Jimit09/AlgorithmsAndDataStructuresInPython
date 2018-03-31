import re
from decimal import Decimal

def filer(file):
    f = open(file, 'r')
    lines = []
    for line in f.readlines():
        lines.append(line.strip())
    return lines

def parse_lines(lines, **kwargs):
    compilers = kwargs.get('keys', ['money', 'name', 'bill'])
    parses = []
    for line in lines:
        l1 = Parser(line, keys=compilers)
        parses.append(l1.get_dict())
    return parses


class Parser(object):
    patterns    = {'name_pattern':'^([\w\-]+)','money_pattern':'(\d+.?\d*)','bill_pattern':"[\w'-]+\.$"}
    keys        = ['money', 'name', 'bill']

    def __init__(self, line, **kwargs):
        if 'patterns' in kwargs:
            self.patterns.update(kwargs.get('patterns'))
            del kwargs['patterns']

        self.__dict__.update(kwargs)

        for key in self.keys:
            key_str = key+'_pattern'
            parser  = re.compile(self.patterns[key_str])
            value   = parser.search(line)
            setattr(self, key, value.group(0))

    def get_dict(self):
        rtn = {}
        for key in self.keys:
            rtn[key] = getattr(self, key)
        return rtn

class Payments(object):

    def __init__(self, **kwargs):
        self.people         = {}
        self.formatter  = "{from} ​pays​ {currency}{amount} ​to​ {to}."
        self.currency   = '$'
        self.__dict__.update(kwargs)

    def add_person(self, person):
        self.people[str(person.name)] = person

    def add_payment(self, payment):
        person = self.people[payment['name']]
        person.add_to(payment)

    def get_liabilities(self):
        liabilities     = []
        for name, person in self.people.items():
            person.set_share(len(self.people.items()))

        for name, person in self.people.items():
            """gets share & sets it against each person in the group"""
            person.set_liability(self.people, self.currency)
            liabilities += person.liabilities

        return liabilities

    def print_liabilities(self):
        liabilities = []
        for liability in self.get_liabilities():
            liabilities.append(self.formatter.format(**liability))
        return liabilities

class Person(object):
    def __init__(self, **kwargs):
        self.name   = ""
        self.items  = []
        self.paid   = 0
        self.share  = 0
        self.liabilities = []
        self.__dict__.update(kwargs)

    def add_to(self, payment):
        """ payment must have keys: 'name', 'money'"""
        if payment['name'] == self.name:
            self.items.append(payment)

    def _get_paid(self):
        balance = 0
        for item in self.items:
            amount  = Decimal(item['money'],2)
            balance += amount
        return Decimal(balance, 2)

    def set_share(self, total_people):
        """total amount paid is divided by the number of 
        people to get the liabilities of each person"""
        self.paid   = self._get_paid()
        self.share  = round(self.paid/Decimal(total_people), 2)

    def _set_extras(self, liability, keys):
        """sets extra properties"""
        for key in keys:
            if hasattr(self, key):
                liab_dict[key] = getattr(self, key)

    def set_liability(self, people, currency):
        """if owed is share is greater than owed, name needs to pay this"""
        for name, person in people.items():
            if self.name != name:
                """if owed is greater than what I have paid then add to liabilities"""
                diff = self.share - person.share
                if diff < 0:
                    liab_dict = {'from':self.name,'to': name,'amount':-diff, 'currency':currency }
                    self.liabilities.append(liab_dict)

class PaymentBuilder(object):
    people  = []
    def __init__(self, **kwargs):
        transactions    = kwargs.get('transaction_file','./transactions.txt')
        names           = kwargs.get('names_file','./names.txt')
        self.payments   = Payments()
        self.trans      = parse_lines(filer(transactions))
        self.names      = filer(names)

        for name in self.names:
            self.payments.add_person(Person(name=name))
        for tran in self.trans:
            self.payments.add_payment(tran)

    def liabilities(self):
        return [ liability for liability in self.payments.print_liabilities()]
