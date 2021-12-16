# Question 1 - Pseudocode
# Set the variable that will hold the sum value and initiate it to 0
# Loop throuhg each element from the first value to the last value given incrementally
# Add the looping value to the sum so that it's stored
# Return the sum

def adding(n):
    sum = 0 # Variable to hold the sum
    for i in range (1, n+1, 1): # Loop from 1 to last value (n+1) in a step of 1
        sum+=i # Add the i to the sum
    return sum # Return the sum value after the loop is complete


print(adding(10)) # Sum is 55
print(adding(10000)) # Sum is 50005000
print(adding(1000000)) # Sum is 500000500000
print(adding(1000000000)) # Sum is 500000000500000000