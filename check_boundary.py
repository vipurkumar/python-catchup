""" Check the boundary has the given number """

def checkBoundaryRange(num,lower_boundary, upper_boundary):
    if num <= upper_boundary and num >= lower_boundary:
        return True
    elif num > upper_boundary:
        return False
    elif num < lower_boundary:
        return False

input("Enter Boundary to check in...")
input_lower_b = input ("Enter the Lower Boundary Range: ")
input_upper_b = input ("Enter the Upper Boundary Range: ")
input_num = input("Enter the number to check: ")

print(checkBoundaryRange(input_num,input_lower_b,input_upper_b))


input("Finished...")
