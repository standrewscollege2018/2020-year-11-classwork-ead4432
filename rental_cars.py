"""This program allows the user to book a rental car and allows you to keep track of the cars being borowred"""
#make a listx3
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsibishi Airtreck", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"] 
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
availability = [True, True, True, True, True, True, True, True, True]
#i
i = 0
#make an input variable
seats_wanted = input("How many seats do you want")
for i in range (len(cars)):
  print(i+1, cars[i], "has", seats[i], "seats")
#ask them which number they want
car_number = int(input("What number car do you want(please enter the number in front of the car)"))
#ask if they are sure it is the car they want
check_car = input("Is this the car you want the {}, please enter yes or no".format(cars[car_number]))
check_car.lower
if check_car == "no":
  car_number = input("What number car do you want(please enter the number in front of the car)")
else:
  if availability[car_number] == False:
    print("Your requested car is not availible for hire")
    car_number = input("What number car do you want(please enter the number in front of the car)")
  else:
    print("You have booked the", cars[car_number], "with", seats, "seats")
    availability[car_number] = False
    
