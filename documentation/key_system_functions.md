# Key System Functions

Table 1 shows a basic summary of the flow of functions of the
system.


| Front-End | Back-End |
| :-------: | :------: |
| select an equation to use | retrieve relevant cached equation object |
| select variable to solve for | prompt for input of independent vars and dims |
| input vals and dims | substitute vals and dims into equation |
| select desired dims | convert dims |
Table 1

Back-End Flow Breakdown
--
The Flow Breakdown is an exploration into *what* the back-end
does. Additional documentation will provide *how*.

#### Equation Retrieval
After an equation object is made it will be stored in a
repository to be recalled when needed. The end goal is
to have a data base of equations that can easily be manipulated
with descriptions of their proper use and individual elements.

#### Prompt for Independent Variable Data
After the user selects the element they wish to solve for the
back-end will use SymPy to rearrange the equation automatically.
Then the symbols in needed for substitution will be detected
and the back-end will prompt the user for the symbols' corresponding
magnitudes and dimensions. The magnitudes and dimensions must
be made consistent before the vals are substituted into the equation.

#### Substitute Vals and Dims
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

#### Convert Dims

Finally, the val is adjusted to reflect the desired dims. This
can be done by dividing the val by the conversion dictionary value
as opposed to multiplying.

[The Vision]()  
[Getting Started]()  
