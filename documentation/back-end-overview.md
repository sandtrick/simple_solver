# Back-End Approaches

## Approach A
notes: does not account for user-define derived-units. all derived
unit conversions must be entered by the programmer in ```dimcon_dict```

##**equation class**
* contains ```dimcon_dict``` {'m': 1, 'ft': 0.3048, etc}, which includes EVERY CONVERSION
* initialize w/ (self, Eq(), eq_dict)
    * ```eq_dict``` is vanilla. ```{'x': (x, 'm'), 'F': (F, 'N'), 'W':  (W, 'J')}```
    * when each eq_dict is made the base units for each var is included
    * *# ```in_dict``` generated from ```eq_dict``` set at ```(eq_dict[i][0],eq_dict[i][1])```
* methods
    * clear input var
        * (self)
        * all (val, 'unit') in ```in_dict``` becomes ```{}```
    * input vars
        * (self)
        * prompt each ```eq_dict``` key. user gives (val, 'unit') items
        * inputed tuples are saved as items in ```in_dict```.
        * ```in_dict``` now looks like {'x': (val1, 'units1'), 'F': (val2, 'units2'), etc}
    * convert input vars
        * (self)
        * compare ```in_dict[key][1]``` to ```dimcon_dict``` keys.
        * when they match ```in_dict[key][0]``` is *multiplied* by ```dimcon_dict[key]```
        * ```in_dict``` becomes ```{'x': (val1*dimcon_dict[key1], 'base unit'), 'F': (val2*etc,etc), etc}```
    * solve for
        * (self, var, units)
        * solves for var in units
        * sympy solve Eq() for var.
        * ```in_dict``` vals are substituted into corresponding symbols in solved Eq()
        * answer is converted to units by *dividing* by ```dimcon_dict[key]```  


### Approach B: A with conversion types


### Approach C

element class
* initialize w/ (self, magnitude, units)
* methods
    * convert units to base
    * convert to base to units
