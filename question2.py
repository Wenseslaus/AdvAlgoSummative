# Question 2

grades = [37, 73, 67, 38, 33, 57, 29, 84] # An array to take the input of grades
n = 60 # Number of Students

# Function to round_off the grades
def round_off(grades):
    new_grades = [] # Storing new grades in it's own array
    for grade in grades: # Loop through each of the grade in grades
        if grade < 38: # Make sure the grade is not less than 38 because it will not have any effect (Student fails anyways)
            new_grades.append(grade) # Add the grade to the new grades if it's less than 38
        elif ((round(grade/5))*5) > grade & ((round(grade/5))*5) - grade < 3: # Else check that the new grade is greater than current and also difference is less than 3
            new_grades.append(((round(grade/5))*5)) # If tru then store the new grade
        else: # If not true skip to the next step
            new_grades.append(grade) # then store the old grade because it doesnt qualify
    print (new_grades) # Run the function
    return new_grades # Return the new grade if all above conditions qualify or the original one if not qualified.


# Function to check that the number of students doesn't exceed 60 or grades is not out of bound
def checker_fun():
    if len(grades) > 60 or max(grades) > 100 or min(grades) < 0: # Check students are not more than 60, or grades not out of bound
        print("Values exceded 60, or Maximum value is greater than 100 or minimum value is less than 0. Please check correctly!") # Print Error Message
    else:
        round_off(grades) # Fun the function to round_off
checker_fun() # Run the checker function