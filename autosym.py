from formula import Formula
from sympy import *

# create a way for the symbols to be auto initiated
def mkeq(streq):
    expr = sympify(streq)
    print(expr)
    return expr

def mkdict(adict):
    for i in adict:
        adict[i][0] = Symbol(adict[i][0])
    print(adict)
    return adict

def mksymlist(symlist):
    for i in range(len(symlist)):
        symlist[i] = Symbol(symlist[i])
    return symlist


symlist = ['x',' K', 'm', 'v', 'F', 'W']
allsyms = mksymlist(symlist)
'''print(allsyms)
#K, m , v = symbols('K m v')
'''
kin_eq = mkeq('K-0.5*m*v**2')
#kin_eq = Eq(K, 0.5*m*v**2)
kin_dict = {'K': ['K', 'J'], 'm': ['m', 'kg'], 'v': ['v', 'm/s']}
mkdict(kin_dict)
kin = Formula(kin_eq, kin_dict)

kin.solvefor('m', 'lbm')





'''
# initialize new formula
a, b, c, A = symbols('a b c A')
law_of_cos_eq = Eq(a**2, (b**2)+(c**2)-(2*b*c*cos(A)))
#pprint(law_of_cos_eq, use_unicode=True)
law_of_cos_dict = {'a': (a, 'm'), 'b': (b, 'm'),
 'c': (c,'m'), 'A': (A, 'radians')}
law_of_cos = Formula(law_of_cos_eq, law_of_cos_dict)

# solve it
law_of_cos.solvefor(a, 'm')
'''

'''
##### Soon these will be function to speed process further
# creates symbols for equation
x, F, W = symbols('x F W')
# makes equation
work_eq = Eq(x*F, W)
# dictionary attaches base-units to symbols
work_dict = {'x': (x, 'm'), 'F': (F, 'N'), 'W': (W, 'N*m')}
# equation and units linked together in Equation class
work = Formula(work_eq, work_dict)
# solves equation for specified variable in desired units
#work.solvefor(x, 'yard')
'''

'''
K, m , v = symbols('K m v')
kin_eq = Eq(K, 0.5*m*v**2)
kin_dict = {'K': (K, 'J'), 'm': (m, 'kg'), 'v': (v, 'm/s')}
kin = Formula(kin_eq, kin_dict)

kin.solvefor(m, 'kg')
'''
'''
work_eq = 'W-F*x'
work_dict = {'x': ['x', 'm'], 'F': ['F', 'N'], 'W': ['W', 'N*m']}

work = Formula(mksym(work_eq), mkdict(work_dict))
work.solvefor(x, 'm')
'''
