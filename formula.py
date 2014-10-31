from sympy import *
import math
from conversions.dimensions import acceleration, angle, area, energy, force, \
    length, mass, pressure, time, velocity, volume

class Formula(object):
    no_inst = 0     # number of instances of the Equation class
    in_dict = {}    # in_dict starts empty
    def __init__(self, streq, strdict):
        self.equation = self.mkeq(streq)
        self.eq_dict = self.mkdict(strdict)
        self.libs = self.mklibs()
        self.baselist = self.mkbaselist()
        Formula.no_inst = Formula.no_inst + 1

    def mkeq(self, astr):
        expr = sympify(astr)    # turns streq into Sympy Eq()
        return expr

    def mkdict(self, adict):
        for i in adict:         # turns the first string of each dict value into a Symbol
            adict[i][0] = Symbol(adict[i][0])
        return adict

    def mklibs(self):
        dictlist = []
        for i in self.eq_dict:
            dictlist.append(self.eq_dict[i][1].dimdict)
        dimconlib = {k:v for d in dictlist for k, v in d.items()}
        return dimconlib

    def mkbaselist(self):
        baselist = []
        for i in self.eq_dict:
            baselist.append(self.eq_dict[i][1].base)
        return baselist

    @classmethod
    def get_no_equations(cls):
        # number of instances of the Equation class
        return cls.no_inst

    @staticmethod
    def round_to_thousandth(num):
        num = ceil(num*1000)/1000
        return num

    def check_typo(self):
        # it typo on dimensions give user another try to enter
        # not needed for dropdown tabs
        pass

    def clear_inputs(self):
        self.in_dict = {}   # clears in_dict
        return self.in_dict

    def input_vars(self, get):
        get = str(get)
        for key in self.eq_dict:
            if key is not get:
                known_val = float(input("Value of {}: ".format(key)))
                known_units = input("Units of {}: ".format(key))
                known_data = [known_val, known_units]
                self.in_dict[key]= known_data
        return self.in_dict

    def get_vars(self, get):
        # retreives info for all vars except the get var
        # builds in_dict like input_vars
        # use on a website
        pass

    def dimcon(self):
        for key in self.in_dict:
            if self.in_dict[key][1] in self.libs:
                self.in_dict[key][0] = self.in_dict[key][0]*self.eq_dict[key][1].dimdict[self.in_dict[key][1]]
                self.in_dict[key][1] = self.eq_dict[key][1].base
            else:
                print('Conversion not stored')
        return self.in_dict

    def solvefor(self, get, get_units):
        if get_units not in self.libs:
            print('Equati does not currently support the dimension: {}'.format(get_units))
        else:
            self.clear_inputs()
            self.input_vars(get)
            self.dimcon()
            get = Symbol(get)
            # get_units = str(get_units)
            arrange = solve(self.equation, get) # solve for get
            get = str(get)
            # sympy sub to substitute dimcon.dimcon_dict into symfor's eq
            sub_vals = []
            for key in self.eq_dict:
                if key is not get:
                    sub_vals.append((self.eq_dict[key][0], self.in_dict[key][0]))
            subd_eq = self.equation.subs(sub_vals) # substituted all values for keys in in_dict
            base_sol = solve(subd_eq, get)
            answer = math.ceil(1000*base_sol[0]/self.libs[get_units])/1000 # convert base_sol's list output to correct units
            print(answer)
            return answer
'''
work_dict = {'x': ['x', length], 'F': ['F', force], 'W': ['W', energy]}
work = Formula('W-F*x', work_dict)
work.solvefor('W', 'kJ')
'''
