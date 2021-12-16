# Input values and parameters
k = 4
n = 9875

def superDigit(n, k): # Function declaired to 
    def digit_sum(v): # Another function to peform the while loop
        while v > 9: # Check to make sure the number of greater thatn 10
            hold = 0 # This will hold the sum of all the digits
            for i in str(v): # Loop through n as a string
                hold += int(i) # add the sum to hold
            v = hold # Make hold as the new n
        return v # Return the sum which is now the new value of n
    x = digit_sum(int(str(n)*k)) # Perform the multiplcation operation
    return x # Return the final Answer

print(superDigit(n, k))