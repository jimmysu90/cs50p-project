# Highway Cruise - A video game made in Python
#### Video Demo:  https://www.youtube.com/watch?v=wZXcaqzA8yc
#### Description:
Highway Cruise is a video game made in Python using the pygame library. 

#### Controls:
In the game, you control a car that automatically drives forward on a highway. You can control the car using the left and right arrow keys to move side to side. Holding the up arrow key will accelerate the car while holding the space bar will brake (but the car never stops completely). If neither the up arrow nor the space bar is being pressed, the car returns to its default cruising velocity.

#### Objective:
The objective of the game is to continue driving along the highway for as long as possible without crashing into another car. Cars spawn at the top of the screen and are always driving at a slower speed than the player car. This means that the player will inetivibly crash into the car unless they steer their car into a safe lane. The cars spawn in random lanes and are driving at a random speed, so the player must adapt by moving into an unoccupied lane at the right time. As time progresses, the difficulty level will increase to a maximum of level 10. As the level increases, more cars will spawn simultaneously and reduce the number of safe lanes available for the player.

## Programming:
This game was made using the pygame library. I decided to make a separate file, classes.py, to import from. The reason I decided to do this was to make the main project.py file more concise and readable. This also made it easier to use some of the variables globally in multiple functions.

### Classes:
classes.py contains classes, such as:
1. Objects 
    - Creates objects for cars with the following properties:
        - A rectangle's location and size to represent the car in the game's world
        - The car's image
        - The car's velocity
        - The car's braking power (defaulted to 0 for non-player-cars)
2. Timers
    - Keeps track of timers in the game
3. Images
    - Initializes and assigns image files to program's variables
4. Settings
    - Manages the global settings values that the functions may use

### Functions:
The main program will continue to execute **run_game()** on loop until the user closes the game window. **run_game()** will first check whether the game is paused or not. If game is paused, if will display the controls menu for the game and wait until the player presses ENTER to unpause the game.

Once the player unpauses the game, the program will execute its main code until they crash into another car (game_over). This main code: 
1. Initiates the timers and keeps them running
1. Repeatedly scrolls the background by calling the **handle_bg()** function
    - Initially, the game loads one image onto the screen and another image one screen's height above the screen (which initially cannot be seen). The game will then scroll these images by continuously moving each of them down
        - These images are randomly selected from a pool of slightly varying images. This means that the roads and the backgrounds will vary randomly (with some dirt patches in the grass, cracks in the road, etc.) as the player continues driving instead of always scrolling through the same image. This was done to create the illusion that the player is moving to a different area as opposed to driving on a treadmill
    - When the top of the background image scrolls to the bottom of the screen, the program will move the image one screen's height above the screen and replace the image with a new one from the random pool and then continue to scroll downwards
1. Checks for collisions between the player and other cars using the **handle_cars()** function
    - The main function passes in an object that contains data about the player's car along with a list that contains multiple objects that each represent another car on the road
    - The **handle_cars()** function takes these objects and checks if the player's car overlaps (i.e. collided) with any of the other cars on the road. If there is any overlap, it will return the object that the player's car overlaps with (which means game over)
    - If there are no collisions, the function will continue to move the non-player cars' y-coordinate-value down by the car's velocity. This in conjunction with the background scrolling will create the illusion that the player car is moving faster than the non-player cars despite the fact that the player car technically isn't moving at all (unless the player uses the keyboard to manually move the car)
    - Once the non-player car has moved off the bottom of the screen, the game will remove its object from the list of cars
1. Checks for user's keyboard inputs and moves the car
    - The car will move unless the player attempts to move off the road or off the screen
1. Uses **spawn_cars()** to create new car objects (frequency is related to difficulty level)
    - **spawn_cars()** will randomly select how many cars, *r*, to spawn (based on difficulty level)
    - **spawn_cars()** will call **generate_car()** *r* number of times
        - **generate_car()** will generate a car object and randomly assign a colour and a velocity
    -**spawn_cars()** appends a list with these newly generated cars and returns them to be appended to the full list of cars
1. Increases the difficulty up to a maximum of level 10 using the game timer
1. Uses the **display()** function to update the graphics on the screen
    - **display()** uses global data to determine where to display the background images
    - **display()** uses a dictionary with object location data and colour to display the correct car image at the car's location
    - **display()** will always display a graphic of a stopwatch and show the current level and the elapsed time in seconds
    - If the game is paused, **display()** will show the controls menu
    - If the player has lost, **display()** will show the the game-over graphic

### Image Files:
The .png files are used as the graphics for this game. The car images were found on the internet and then editted using MS Paint and MS Paint 3D All other images were personally created for this project using MS Paint and MS Paint 3D.