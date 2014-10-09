from sympy import *

class Equation(object):
    # dimcon_dict items convert keys to base units when multiplied
    dimcon_dict = {'ft': 0.3048, 'lbs': 4.4482, 'ft*lbs': 1.3558}
    in_dict = {}
    def __init__(self, equation, eq_dict):
        self.equation = equation
        self.eq_dict = eq_dict

    def clear_inputs(self):
        # makes in_dict = {}
        self.in_dict = {}
        print(self.in_dict)
        return self.in_dict

    def input_vars(self, get):
        # input all known_data but data for get
        # prompts user the keys of eq_dict
        # user inputs go in as in_dict
        get = str(get)
        for key in self.eq_dict:
            if key is not get:
                known_val = int(input("Value of {}: ".format(key)))
                known_units = input("Units of {}: ".format(key))
                known_data = [known_val, known_units]
                self.in_dict[key]= known_data
        #print(self.in_dict)
        return self.in_dict

    def dimcon(self):
        # all units made dimensionally consistent
        # checks if unit is in dimcon_dict. if not prints "Conversion not Stored"
        # compares in_dict[key][0] ro dimcon_dict[key]
        for key in self.in_dict:
            if self.in_dict[key][1] in self.dimcon_dict:
                self.in_dict[key][0] = self.in_dict[key][0]*self.dimcon_dict[self.in_dict[key][1]]
            else:
                print('Conversion not stored')
                # need to change units to base units somehow
                # elements need way to auto-recognize their base unit type
                # perhaps dimcon method can just activate an element method
                # that tells ele's to change value to correspond to a unittobase conversion
                # self.in_dict[key][1] = self.dimcon_dict[self.in_dict[key][1]]
        # print(self.in_dict)
        # print(self.equation)
        # sym = symbol(str(sym))

    def uni_symfor(self):
        # prints symfor in unicode
        pass

    def solvefor(self, sym):
        # calls symfor
        self.symfor(sym)
        # sympy sub to substitute dimcon_dict into symfor's eq
        print(solve(self.equation, sym))
        return solve(self.equation, sym)
        # adjusts final value to requested dim
        # return value and dim


x, F, T = symbols('x F T')
work_eq = Eq(x*F, T)
# this works print(moment)
work_dict = {'x': (x, 'm'), 'F': (F, 'N'), 'T': (T, 'N*m')}
# this works print(moment_dict)

work = Equation(work_eq, work_dict)
#for i in work_dict:
#    print(work_dict[i])
# clear inputs functions
# work.clear_inputs()

# input all vars but x
work.input_vars(x)
work.dimcon()
