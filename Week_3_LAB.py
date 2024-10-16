my_list = [15,23,32,46]
print(my_list[0])
print(my_list[-1])
print(my_list[:2]) # or print(my_list[0:2])
result = my_list[0] + my_list[-1] # add the first and last item and assign them to result
my_list.append(result) # add result to the nd of the list using append method.

print(result)

##########################################################################################

your_list = [200,15, "Programming", 1+2, "Lab 3"]
print(len(your_list))
your_list.append(181)

print(your_list)

your_list.remove("Lab 3")

print(len(your_list))
print(your_list)
print(your_list[0])

##########################################################################################

your_list[1] = 181
print(type(your_list))
your_tuple = tuple(your_list)
print(type(your_tuple))
print(your_tuple[0])
print(len(your_tuple))

another_tuple = (8, 18, 181) # New tuple

joined_turple = your_tuple + another_tuple # Variable to add the two tuples together
print(joined_turple)
your_list = list(joined_turple) # Convert the joined tuple to a list
print(type(your_list)) # Verify the data type of the list
your_set = set(your_list) # Convert the list to set
print(len(your_set)) # Find the length of the set
your_set.add("Gabriel") # Add an item to the set
print(your_set)
your_set.add("Gabriel")
print(your_set)

##########################################################################################

another_set = {1,3,4} # New set
new_set = your_set & another_set # Finds the common items between "your_set" and "another_set"
print(new_set)

##########################################################################################

car_details = {"car_make": "Toyota",  # New dictionary with key-values
"car_model": "Corolla"}
print(car_details)
make = car_details["car_make"]
print(car_details)
car_details["year"] = 2024 # Adds a new key-value 
print(car_details)
car_details["colour"] = "Red"
print(car_details)
del car_details["colour"] # Deletes key-value from the dictionary
print(car_details)

##########################################################################################

#Exercises:

# 1. Which data type is appropriate to store GPS coordinates? Float
# 2. Which data type is appropriate to store items of a shopping cart? String
# 3. Which data type is useful to find common values between two lists? Set