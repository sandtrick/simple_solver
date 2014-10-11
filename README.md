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

## Table of contents

| In No Particular Order |
| ----------------- |
| [Read Me](https://github.com/sandtrick/simple_solver)|
| [Introduction](https://github.com/sandtrick/simple_solver/blob/master/documentation/introduction.md) |
| [Getting Started](https://github.com/sandtrick/simple_solver/blob/master/documentation/getting_started.md) |
| [Key System Functions](https://github.com/sandtrick/simple_solver/blob/master/documentation/key_system_functions.md) |
| [Back-End Overview](https://github.com/sandtrick/simple_solver/blob/master/documentation/back-end-overview.md) |
| [Project Resources](https://github.com/sandtrick/simple_solver/blob/master/documentation/back-end-overview.md) |
