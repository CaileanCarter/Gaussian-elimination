# Gaussian elimination

Gaussian elimination is an algebraic solution to solve the unknown variables from a linear system of equations like:

Row 1: -8x + 5y + 3z = 44
Row 2: -6x + 2y + -8z = -66
Row 3: 6x + -6y + 7z = 64

The equations are solved by using a set of rules to produce a linear system of equations like:

Row 1: 1x + 0y + 0z = -3
Row 2: 0x + 1y + 0z = -2
Row 3: 0x + 0y + 1z = 10

Which has solves our set of equations as x = -3, y = -2 and z = 10. 

The rules are:

- Can multiply any row by a constant (except zero)
- Can switch any two rows
- Can add any two rows together

Gaussian elimination is used in linear algebra to calculate things like null space and column space. This also has relevance to metabolic modelling which use null space analysis.

The reason for writing this Python script to perform Gaussian elimination was less practical and more for the challenge. Although it may have some use in a metabolic modelling software.

The script generates a random set of unknown variables (xyz) and a random set of constants for each equation. The lingering constant is then calculated accordingly. The script goes through the matrix (containing the linear system of equations) in the normal order, creating the row echelon form before solving the rest. The script will talk through all the steps it takes (i.e. "Row 3 was multiplied by -5.65 and added to row 2"). There is also function to print the matrix and equations. Comments are included to explain the majority of the functionality and processing going on in the script