# Dynamic Equation Builder and Solver (DEBS)

## Fast Equation Generation & Manipulation

### Goal

The goal is to create a system that enables the speedy
creation of solvable equations (variables contain dimensions)
that solve for any variable without the need for the
programmer to write each equation arrangement per independent
variable.

### Requirements

1. Minimize steps needed to add a new equation
2. Solves equation without programming arrangements
3. Functions with non-uniform input dimensions
4. Outputs solved-variable with requested dimensions
5. Accounts for SI and imperial unit systems

Optional:
* Prints solution in unicode

### Method
#### User Flow

| Front-End | Back-End |
| :-------: | :------: |
| select an equation to use | retrieve relevant cached equation object |
| select variable to solve for | prompt for input of independent vars and dims |
| input vals and dims | substitute vals and dims into equation |
| select desired dims | convert dims |

#### Back-End Flow Breakdown
##### Equation Retrieval
After an equation object is made it will be stored in a
repository to be recalled when needed. The end goal is
to have a data base of equations that can easily be manipulated
with descriptions of their proper use and individual elements.

##### Prompt for Independent Variable Data
After the user selects the element they wish to solve for the
back-end will use SymPy to rearrange the equation automatically.
Then the symbols in needed for substitution will be detected
and the back-end will prompt the user for the symbols' corresponding
magnitudes and dimensions. The magnitudes and dimensions must
be made consistent before the vals are substituted into the equation.

##### Substitute Vals and Dims
After the user inputs the independent variable information the
back-end will substitute the adjusted vals into the equation using SymPy.
Currently, the team is investigating the best way to contain
the vals and dims data to comply with the project goals.

It may be best to simply use a list or dictionary to contain
the variable data since it will be only temporary and will not
interfere with other equations that use the same variables.

However, if this is the approach taken the team must discern
how to relate the data to their corresponding symbols in the
SymPy equation.


##### Convert Dims

Finally, the val is adjusted to reflect the desired dims. This
can be done by dividing the val by the conversion dictionary value
as opposed to multiplying.

#### Back-End Structure
##### Approach 1: Intro

```
def foo(arg1, arg2, *args):
```
or
```
def bar(arg1, arg2, **kwargs):
```

where args1 & 2 are the dependent variable and its
desired dimensional output and *args are all other
variables and their given dimensions.

May use kwargs. The team is exploring the possibility
of each equation being built into a dictionary. Each
equation dictionary would contain the variable names
as keys and their magnitude and dimension as values.

The dictionaries with then be fed to a class or function
that makes the dimensions uniform and solves for the
dependent variable.


##### Approach 2: Element class (branch varclass)

Unlike Approach 1 where the dimension changing is handled by the
equation class, each equation dictionary will contain values that
are Element objects. it will look something like

eq_dict = {str(sym1): ele1, str(sym2): ele2, etc...}

The element objects will contain a symbol for sympy manipulations,
a value to be substituted, and a dimension that when modified
adds a multiplier to the value to keep it consistent

this may be better than Approach 1 because it allows for the element
class objects to be manipulated in other types of tools. by containing
the dimensional consistency functions to an element the equation
class will not need to contain the large amount of code needed
to identify a variable's base dimension. The base dimension
can be contained in the subclass of any element class.

##### Super: Element(object)
The Element superclass will contain a symbol, a value.
It will it also contain all of the conversion dictionaries.
Derived units (e.g.  N/m) will be inserted into the class
as they are needed. The inclusion of this class will make


##### Sub: [dim]  (e.g. Length(Element), Density(Element))
The [dim] subclasses will contain



### Questions to Answer

* Can a dictionary be passed to a function?  
* Can a dictionary be passed to a class?  
> yes.
* Can a SymPy Eq() be passed to a class?
> yes.
* Should there be a module with "completed" objects (equations)?  
> This would be nice. A module of equation objects would relieve
> the need to create them every time. It would also prove useful
> in an off-line app.
* What is NumPy and would it provide any tools to simplify this
project? If so, how?
* If a file is moved with "git mv" in one branch does git have
any conflicts if that branch is then merged with the master?


### Thoughts

* It would be nice to have each equation as in instance
of a class (object). Then each object can be cataloged
for future use.
* I need to learn how to create and use my own modules
