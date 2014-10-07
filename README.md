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

#### Idea 1: Intro

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

The team will be using SymPy to facilitate equation
solving.

#### Idea 1: Process Breakdown

1. Build equation dictionary
2. Feed dictionary to Function or class
  1. uniform dimensions
  2. make equation
  3. solve for desired variable
  4. convert variable value to desire units
  5. output requested-variable's magnitude and dimension
3. ???


### Questions to Answer

Can a class be __init__ with a function?
Can "   "     "    "      "  a dictionary?
Should there be a module with "completed" objects (equations)?


### Thoughts

It would be nice to have each equation as in instance
of a class (object). Then each object can be cataloged
for future use.
