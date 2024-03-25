#Bruce Reyes

#import math module
import math

"""We use self to call and access instances and attributes of a method. 
    It allows ust to modify the attributes of an object in a specific instance """
#create a class called car
class Car:
    
    #function to get coordinates of cars
    def __init__(self, x = 0.0, y = 0.0 ,heading = 0.0):
        self.x = x #starting x coordinate of the car
        self.y = y #starting y coordinate of the car
        self.heading = heading #starting heading of the car

    #function to turn the car
    def turn(self, degrees):
        self.heading = (self.heading + degrees) % 360 #ensures that turn 360 degrees
    
    #function to drive the car
    def drive(self, distance):
        #define h as heading to account for non zero headings
        h = math.radians(self.heading)
        #update attributes to current attributes
        self.x += distance * math.sin(h)
        self.y -= distance * math.cos(h)
   
    #function to print "Hello"
    def PrintHello():
        message = print("Hello")
        return message
    
    #function to print "Goodbye"
    def PrintGoodbye():
        message = print("Goodbye")
        return message

"""sanity_check is outside of the Car() class
    because it is meant to be a stand alone function"""

#sanity check function
def sanity_check():
    SanityCar = Car()# creating an instance of a car
    SanityCar.turn(90) #turn 90 degrees
    SanityCar.drive(10) #drive 10 units
    SanityCar.turn(30) # turn 30 degrees
    SanityCar.drive(20) # drive 20 units
        
    #print location then heading on next line
    print(f"Location {SanityCar.x}, {SanityCar.y}") 
    print(f"Heading: {SanityCar.heading}") #using f string to easily implement attributes
    return SanityCar

"""if __name__ statement that invokes the sanity check,
    so sanity check will basically always be called"""
if __name__ == "__main__":
    sanity_check()