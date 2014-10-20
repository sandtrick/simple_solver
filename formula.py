from sympy import *
from math import ceil
import dimcon

class Formula(object):
    no_inst = 0     # number of instances of the Equation class
    in_dict = {}    # in_dict starts empty
    def __init__(self, streq, strdict):
        self.equation = self.mkeq(streq)
        self.eq_dict = self.mkdict(strdict)
        Formula.no_inst = Formula.no_inst + 1

    def mkeq(self, astr):
        expr = sympify(astr)    # turns streq into Sympy Eq()
        return expr

    def mkdict(self, adict):
        for i in adict:         # turns the first string of each dict value into a Symbol
            adict[i][0] = Symbol(adict[i][0])
        return adict

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

    def check_dimcon(self, key):
        # pass a key to to method and it checks the dimcon.dimcon_dict to see if it exists
        # a class method?
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
            if self.in_dict[key][1] in dimcon.dimconlib:
                self.in_dict[key][0] = self.in_dict[key][0]*dimcon.dimconlib[self.in_dict[key][1]]
                self.in_dict[key][1] = self.eq_dict[key][1]
            else:
                print('Conversion not stored')
        return self.in_dict

    def solvefor(self, get, get_units):
        if get_units not in dimcon.dimconlib:
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
            subd_eq = self.equation.subs(sub_vals)
            base_sol = solve(subd_eq, get)
            answer = ceil(1000*base_sol[0]/dimcon.dimconlib[get_units])/1000 # need to convert base_sol's list output to correct units
            print(answer)
            return answer

# work
work_dict = {'x': ['x', 'm'], 'F': ['F', 'N'],
 'W': ['W', 'N*m']}
work = Formula('W-x*F', work_dict)

work.solvefor('W', 'N-m')
