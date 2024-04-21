import random
import turtle

shape = turtle.Pen()


#making the function that returns a random integer from 3 to 8
def randomNumber():
    randNum = random.randint(3, 9)
    return randNum

#making the functions for both the spiral shapes and the rotating shapes, and plugging in the randum number into both of them
#I also used an if statement to choose which color each line would be

def rotatingShape(number):
        for count in range(0, 8):
            shape.left(50)
            for count in range(0, number):

                shape.forward(50)
                #getting the correct angle
                shape.left(360/number)
                
                color = random.choice(['red', 'green', 'yellow', 'blue'])

                if color == 'red':
                    shape.color('red')
                elif color == 'green':
                    shape.color('green')
                elif color == 'yellow':
                    shape.color('yellow')
                else:
                    shape.color('blue')
def spiral(number):
        for count in range(0, 100):

            shape.forward(count)
            #getting the angle
            shape.left(360/number)

            color2 = random.choice(['red', 'green', 'yellow', 'blue'])

            if color2 == 'red':
                shape.color('red')
            elif color2 == 'green':
                    shape.color('green')
            elif color2 == 'yellow':
                shape.color('yellow')
            else:
                shape.color('blue')




#creating the loop to check if the random integer was even or odd, and then plugging it in to the corresponding function, and running it 4 times
for count in range(0, 4):
    randNum = randomNumber()
    if randNum % 2 == 0:
        rotatingShape(randNum)
    else:
        spiral(randNum)
    shape.clear()
   
