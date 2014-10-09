# Back-End Approaches
---
## Approach A

###**equation class**
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
    * dimcon
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

### Draw Backs of Approach A

##### 1. Does not account for user-define derived-units.

> All derived unit conversions (eg 'ft\*lbs' to 'N\*m') must be
> entered by the programmer manually. This approach does not
> allow a user to use whatever silly dimensions that may fit
> their needs (whether they are 'in*kips' or 'slugs') and all
> sorts of derived-unit conversions must be entered entered
> by the programmer.

##### 2. ~~Dimensions do not identify their own common base dimension.~~

> _**This issue has been resolved by use of ```eq_dict```. When the ```eq_dict``` is
> entered its items list base units for each key**_

> The ```dimcon``` method can use the dimcon_dict to change the values
> of variable, but it currently has no way to tell the variable
> what its base units are. For example, if x = 5 feet the dimcon
> method can currently convert x to x = 1.524 feet when it should
> read x = 1.524 meters. This is technically not an issue because
> when the ```solvefor``` method calls ```in_dict``` for values it will
> assumes that all of the values have been converted to base units.
> This allows the ```solvefor``` method to convert the value to the
> be consistent with the desired dimensions by simply dividing the
> value by the item of the key in ```in_dict``` that shares the same
> name.

> This is mainly considered a problem for the class in general as
> it hinders the flexibility of the class in other applications. If
> the system ever required a simple conversion tool an equation and dictionary
> must be entered. This begs the question:

> 1. If a simple conversion tool was made would we want to use this class?
> 2. If not, would it be better to build a conversion class that could be easily
> integrated into/work with this one?
> 3. Would it be a better use of time to build an class that deals
> directly with the short comings of the equation class?

##### 3. Difficulty Managing dimcon_dict

> _**For the moment this will be tolerated and some sort of ```dimcon_dict```
> key check will be implemented to allow the programmer to easily
> check if ```dimcon_dict``` already contains a conversion.**_

> As more equations are added the dimcon_dict will need to accommodate
> the conversion factors for an ever increasing number of dimensions.
> Most generic equations share the same types dimensions; this should
> allow the number of dimcon_dict keys to 'level off' at some point.
>
> In the future it may be possible to break ```dimcon_dict```
> into ```dimcon_dicts``` which would be a list of conversion dictionaries
> divided into dimensional types (eg. length, temperature, mass, etc).
> This also presents its challenges as dimensions of an esoteric nature
> would be difficult to categorize. 


## Approach A: A with conversion types


---

## Approach C

element class
* initialize w/ (self, magnitude, units)
* methods
    * convert units to base
    * convert to base to units
