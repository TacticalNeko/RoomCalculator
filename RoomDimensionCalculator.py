import time

print("Hi, welcome to my room dimensions calculator!")
amountOfWalls = int(input("Please input how many walls are in the room: "))

for i in range(amountOfWalls):
    wallWidth = float(input("Please input the width of the wall in m: "))
    wallLength = float(input("Please input the length of the wall in m: "))
    wallHeight = float(input("Please input the height of the wall in m: "))

print("Brilliant! I'll start calculating...")
roomVolume = wallWidth * wallLength * wallHeight
floorArea = wallWidth * wallLength
wallArea = wallWidth * wallHeight
paintNeeded = wallArea

print("Calculating complete!")
print("The area of the floor is: " + str(floorArea) + "m²!")
print("The amount of paint needed for 1 coat is: " + str(paintNeeded) + "l!")
print("The volume of the entire room is: " + str(roomVolume) + "m³!")