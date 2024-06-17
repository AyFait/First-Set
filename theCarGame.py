#Now there is a different, and shorter, approach to this program in a
#video tutorial I saw on youtube, but I it is ok to make
#my own way of it, even though it quite a bit longer to code

start = False
stop = True
carExit = True 
#while command != "quit":
while True:
    command = input("Input your command (type 'help' for manual): ").lower()
    if command == "start":
        if start:
            print("Car Already Started...")
            
        else:
            start = True
            stop = False
            carExit = False
            print("Car Started!...")

    elif command == "stop":
    
        ''' 
        here can use - if not start - to negate the start boolean value. i.e if start = True then stop = False and also only start var is really needed in this prog.

        		if not start:
        		print("Car Stopped")

        		else:
        		Print("Car already stopped!")
        '''
 		
        if stop:
            
            print("Car Already Stopped!")

        else:
            stop = True
            start = False
            carExit = False
            print("Car Stopped!")

    elif command == 'quit':
        if carExit:
            print("You're not even in the Car yet!")

        else:
            print("Car Stopped, Exiting the Car!")
            break

    elif command == "help":
        print('''
Just Type:
start to START the car
stop to STOP the car
quit to EXIT the car    
        ''')
    else:
        print("Command not understood, type 'help' for manual...")
