#Idris Adeyemi
#10/16/2022

#Hi this will aloow you to answer 6 problems by inputting the programs for each of the problems

#This is problem 1 saying hello world.
print("Hello World.")

#This is problem 2 which will ask for the user name and greet them with their name
NAME = input(" name:" )
print("Hello there", NAME)

#This is problem 3 which will greet both you and the instructor
NAME2 = input(" name of professor:")
print("hello", NAME, "and", NAME2)

#This is problem 4 trying to find the area of a circle
pi = 3.147
print(" The area of a circle is")
print(pi)

#This is problem 5 which you will be finding the mileage per gallon in a car.
Miles = int(input("current Miles: "))
Gallons = int(input("Gallons Used: "))
print(" Thank you, your MPG is: ", Miles/Gallons)

#This is problem 6 this will be converting degrees from Fahrenheit to Celsius
celsius = float(input("celsius: "))
fahrenheit = (celsius *9/5)+32
fahrenheit = round(fahrenheit,2)
print(celsius,'celsius is: ',fahrenheit, 'fahrenheit')
