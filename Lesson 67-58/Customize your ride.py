print("Select your ride:")
print("1.Bike")
print("2.Car")

choice= int(input("Enter your choice"))
if choice == 1:
    print("Your choice was the bike")
    print("1.Bullet")
    print("2.Splendor")

    bike= int(input("Enter your choice "))
    if bike == 1:
        print("You have selected Bullet")
    else:
        print("You have selected Splendor")
elif choice == 2:
    print("You have selected Car")
    print("1.McLaren")
    print("2.Audi")
    car=int(input("Enter your choice"))
    if car==1:
        print("You have selected McLaren")
    else:
        print("YOu have selected Audi")
else:
    print("Invalid choice")