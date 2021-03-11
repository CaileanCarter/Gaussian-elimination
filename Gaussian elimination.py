#! /usr/bin/python3

"""
Perform Gaussian elimination on a randomly generated linear system of equations.
The workings are printed.

Rules:
- Can multiply any row by a constanant (other than zero)
- Can switch any two rows
- Can add any two rows together

"""

from random import randint

LSE = {} #keys are equation index and values are a list containing constanants and last value being the lingering constant
number_of_equations = 3

# Create randomised equations:

xyz = [randint(-10, 10) for _ in range(number_of_equations)] #creates xyz "unknown variables"

for index in range(1, number_of_equations + 1):

    LSE[index] = [randint(-10, 10) for _ in range(number_of_equations)] #created randomised constants
    LSE[index].append(0) 

    for num in range(number_of_equations):
        LSE[index][3] += (LSE[index][num] * xyz[num])  #calculates the lingering constant


def print_equations():
    for equation in LSE.keys():
        Row = "Row {row} : {a}x + {b}y + {c}z = {lingering_constant}"
        print(
            Row.format(
            row = equation,
            a= round(LSE[equation][0]),
            b= round(LSE[equation][1]), 
            c= round(LSE[equation][2]),
            lingering_constant= round(LSE[equation][3])
            ))
    print("")


def print_matrix():
    for equation in LSE.keys():
        matrix = "{a} {b} {c} : {lingering_constant}"
        print(
            matrix.format(
            a = LSE[equation][0],
            b = LSE[equation][1],
            c = LSE[equation][2],
            lingering_constant = LSE[equation][3]
            ))
    print("")


def output():
    SolvedEquations = "The equations have been solved for: x = {x}, y = {y} and z = {z}."
    print(SolvedEquations.format(
        x = round(LSE[1][3]),
        y = round(LSE[2][3]),
        z = round(LSE[3][3])
    ))
    print_equations()


def main(column, row, value=0):
    
    eq_row = LSE[row] # eq_row means equation row

    if eq_row[column-1] == value: #if the value is already what is wanted, the script moves on to next number.
        print("No action required - number already " + str(value))
        

    elif value == 1 and eq_row[column-1] != 0:
        #checks all numbers in the equation that aren't zero can be times by 1 / number of interest
        if all(number % eq_row[column-1] == 0 for number in eq_row if number != 0) or column == row: 
            LSE[row] = []
            for number in eq_row:
                LSE[row].append(number / eq_row[column-1] if number!= 0 else 0)
            
            statement = "Row {row} was multiplied by 1 over " + str(eq_row[column-1]) + " from column {column}, row {row}"
            print(statement.format_map(vars()))
            
    else:
        for equation in LSE.keys(): 
            # checks if can swap rows/equations
            if equation != row:
        
                # checks if can multiply another row and add
                if all(number == 0  for number in LSE[equation][:column-1]) or LSE[equation][column-1] == 1:
                    LSE[row] = [eq_row[number] - (LSE[equation][number] * ((eq_row[column-1] - value) / LSE[equation][column-1])) for number in range(len(eq_row))]
                    statement = "Row {equation} was multiplied by " + str(-round((eq_row[column-1] - value) / LSE[equation][column-1], 2)) + " and added to row {row}"
                    print(statement.format_map(vars()))
                    
                elif LSE[equation][equation-1] != 1 and LSE[equation][column-1] == value: #the first part is checking that it doesn't have a 1 as to not disturb the diaganol 1 trend
                    LSE[row] = LSE[equation] # current row is swapped with a suitable row
                    LSE[equation] = eq_row # old row is swapped with current row
                        
                    statement = "Swapped rows {row} and {equation}"
                    print(statement.format_map(vars()))
                    

def start():

    print("Starting Gaussian elimination...\n")
    print_equations()
    
    post_row_echelon_form_queue = [] 

    for column in range(1, number_of_equations + 1):
        for row in range(1, number_of_equations + 1):

            if row == column:
                main(column, row, 1)
                print_matrix()
            elif row > column:
                main(column, row)
                print_matrix()
            elif row < column: 
                post_row_echelon_form_queue.append([column, row])
    
    for remainder in post_row_echelon_form_queue:
        column, row = remainder
        main(column, row)
        print_matrix()
    
    output()


if __name__ == "__main__":   
    start()