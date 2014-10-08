from sympy import *

class Makecalc(object):
    def __init__(self, equation, dictionary):
        self.equation = equation
        self.dictionary = dictionary

    def dimcon(self, dictionary):
        # makes all values dim con
        # returns dimcon_dict
        pass

    def checksym(self, sym):
        # checks if sym is in equation
        # if not return 'this shit wack'
        # else pass
        pass

    def symfor(self, sym):
        # uses sympy magic to solve for sym
        # return symfor equ
        print(self.equation)
        # sym = symbol(str(sym))
        print(solve(self.equation, sym))


    def uni_symfor(self):
        # prints symfor in unicode
        pass

    def solvefor(self, sym, dim):
        # calls symfor
        # sympy sub to substitute dimcon_dict into symfor's eq
        # adjusts final value to requested dim
        # return value and dim
        pass

x, F, T = symbols('x F T')
moment = Eq(x*F, T)
print(moment)
moment_dict = {'x': (x, 'm'), 'F': (F, 'N'), 'T': (T, 'N*m')}
print(moment_dict)

moment_eq = Makecalc(moment, moment_dict)
moment_eq.symfor(x)
