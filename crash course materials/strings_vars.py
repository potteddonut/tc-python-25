# declaring variables
my_message = "Hello world!"
distance_from_home = 30     # variables can be any data type!
my_name = "My name is " + "Teacher Zach"
having_fun = True


my_cars = ["Lamborghini", "Ferrari", "BYD"]
print("My car is: " + my_cars[0])

my_cars.append("Tesla")
print("Now, my new car is " + my_cars[3])


new_car = input("What is the name of your new car?: ")
my_cars.append(new_car)
print("Now, my cars are ", my_cars)


if len(my_cars) < 10:
    print("We don't have enough cars!")


