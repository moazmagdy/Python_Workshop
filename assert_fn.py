"""
This script implements the assert function to 
ensure code reliability.
"""
#This function calculates the average of scores.
#we use assertion to ensure proper input values.
def avg(x):
    """
    x --> [int]
    """
    assert type(x) is list , "Input not a list"
    assert len(x) != 0 , "Empty list"
    assert all([type(i) is not int for i in x]), "All values must be integers"
    
    return sum(x)/len(x)