## [Project Wiki Page](https://github.com/sandtrick/simple_solver/wiki)

## Dynamic Equation Builder and Solver (DEBS)

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
