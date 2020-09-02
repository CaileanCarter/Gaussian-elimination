#Performs Gaussian elimination of a linear system of equations

#Rules:
# - Can multiply any row by a constanant (other than zero)
# - Can switch any two rows
# - Can add any two rows together

from random import randint

Linear_system_of_equations = {} #keys are equation index and values are a list containing constanants and last value being the lingering constant

number_of_equations = 3

#Create randomised equations:

xyz = [randint(-10, 10) for _ in range(number_of_equations)] #creates xyz "unknown variables"

for index in range(1, number_of_equations + 1):

    Linear_system_of_equations[index] = [randint(-10, 10) for _ in range(number_of_equations)] #created randomised constants
    Linear_system_of_equations[index].append(0) 

    for num in range(number_of_equations):
        Linear_system_of_equations[index][3] += (Linear_system_of_equations[index][num] * xyz[num])  #calculates the lingering constant

########

def Print_equations():
    for equation in Linear_system_of_equations.keys():
        Row = "Row {row} : {a}x + {b}y + {c}z = {lingering_constant}"
        print(
            Row.format(
            row = equation,
            a= round(Linear_system_of_equations[equation][0]),
            b= round(Linear_system_of_equations[equation][1]), 
            c= round(Linear_system_of_equations[equation][2]),
            lingering_constant= round(Linear_system_of_equations[equation][3])
            ))
    print("")
            
def Print_matrix():
    for equation in Linear_system_of_equations.keys():
        matrix = "{a} {b} {c} : {lingering_constant}"
        print(
            matrix.format(
            a = Linear_system_of_equations[equation][0],
            b = Linear_system_of_equations[equation][1],
            c = Linear_system_of_equations[equation][2],
            lingering_constant = Linear_system_of_equations[equation][3]
            ))
    print("")

def Output():
    SolvedEquations = "The equations have been solved for: x = {x}, y = {y} and z = {z}."
    print(SolvedEquations.format(
        x = round(Linear_system_of_equations[1][3]),
        y = round(Linear_system_of_equations[2][3]),
        z = round(Linear_system_of_equations[3][3])
    ))
    Print_equations()

def Gaussian_elimination(column, row, value=0):
    
    eq_row = Linear_system_of_equations[row] #eq_row means equation row

    if eq_row[column-1] == value: #if the value is already what is wanted, the script moves on to next number.
        print("No action required - number already " + str(value))
        return

    elif value == 1 and eq_row[column-1] != 0:
        #checks all numbers in the equation that aren't zero can be times by 1 / number of interest
        if all(number % eq_row[column-1] == 0 for number in eq_row if number != 0) or column == row: 
            Linear_system_of_equations[row] = []
            for number in eq_row:
                Linear_system_of_equations[row].append(number / eq_row[column-1] if number!= 0 else 0)
            
            statement = "Row {row} was multiplied by 1 over " + str(eq_row[column-1]) + " from column {column}, row {row}"
            print(statement.format_map(vars()))
            return
        
    for equation in Linear_system_of_equations.keys(): 
        #checks if can swap rows/equations
        if equation != row:
    
            #checks if can multiply another row and add
            if all(number == 0  for number in Linear_system_of_equations[equation][:column-1]) or Linear_system_of_equations[equation][column-1] == 1:
                Linear_system_of_equations[row] = [eq_row[number] - (Linear_system_of_equations[equation][number] * ((eq_row[column-1] - value) / Linear_system_of_equations[equation][column-1])) for number in range(len(eq_row))]
                
                statement = "Row {equation} was multiplied by " + str(-round((eq_row[column-1] - value) / Linear_system_of_equations[equation][column-1], 2)) + " and added to row {row}"
                print(statement.format_map(vars()))
                return
     
            elif Linear_system_of_equations[equation][equation-1] != 1 and Linear_system_of_equations[equation][column-1] == value: #the first part is checking that it doesn't have a 1 as to not disturb the diaganol 1 trend
                Linear_system_of_equations[row] = Linear_system_of_equations[equation] #current row is swapped with a suitable row
                Linear_system_of_equations[equation] = eq_row #old row is swapped with current row
                    
                statement = "Swapped rows {row} and {equation}"
                print(statement.format_map(vars()))
                return

def Start():

    print("Starting Gaussian elimination...\n")
    Print_equations()
    
    post_row_echelon_form_queue = [] 

    for column in range(1, number_of_equations + 1):
        for row in range(1, number_of_equations + 1):

            if row == column:
                Gaussian_elimination(column, row, 1)
                Print_matrix()
            elif row > column:
                Gaussian_elimination(column, row)
                Print_matrix()
            elif row < column: 
                post_row_echelon_form_queue.append([column, row])
    
    for remainder in post_row_echelon_form_queue:
        column, row = remainder
        Gaussian_elimination(column, row)
        Print_matrix()
    
    Output()
           
Start()