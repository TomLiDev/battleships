# Battleships!

## Overview

This project was intended to provide a fun game based on the classic battleships game. 

![An image of the finished website on different devices](documentation/space-quiz-homepage-devices.png)

Please use the link below to view the live, deployed game as an app on the Heroku platform:

[Battleships! Live game](https://toms-battleships-f6a8a663bf2b.herokuapp.com/)

## CONTENTS

- [User Experience](#user-experience)

- [User Stories](#user-stories)

- [Design](#design)

- [Colorama](#colorama)

- [Emoji](#emoji)

- [Flow Diagrams](#flow-diagrams)

- [Features](#features)

- [General Features on All Pages](#welcome-message-and-board-size-selection)

- [Displaying Boards](displaying-boards)

- [Username Page](#username-page)

- [Quiz Main page](#quiz-main-page)

- [Results Page](#results-page)

- [Leaderboard](#leaderboard)

- [404 Error Page](#404-error-page)

- [Future Implementations/Plans](#future-implementationsplans)

- [Accessibility](#accessibility)

- [Technologies Used](#technologies-used)

- [Deployment](#deployment)

- [Local Development](#local-development)

- [Testing](#testing)

- [Credits](#credits)

- [Acknowledgements](#acknowledgements)

## User Experience

Toms battleships is a python-driven game based on the classic battleships game.

Instructions will be provided for optional view alongside the main game. 

### User Stories

#### First Time Visitors

As a first time visitor I want to understand how to play the game and have the ability to start the game quickly. I'd like a fun experience playing the game and the option to start another game quickly afterwards to keep me engaged. 

#### Return Visitor

As a return visitor I want to be able to play a game quickly without the need to read through instructions. Some different options for the size of the game board would be good to provide variety and keep the game interesting on repeat plays. 

## Design

Being a python driven project, there are limited options for introducing fonts, colour and different design aspects.

### Colorama

However I will import and use the Colorama library to customise some of the messages displayed to the player to provide some contrast and variety in the messages. The purpose of this colouring will be to provide some contrast and variety, to visually improve the game and make it more visually appealing, whilst also providing some targeting of the messages so that the player has a better understanding of what is happening and how to interact with the game.

Messages that are targeted at the player will be displayed with green text, giving prompts for actions, input etc. 

Messages that are relevant to the 'enemy', the computer actions, will be displayed in red. 

Some messages, such as the opening welcome may be displayed with a background colour as well as coloured text, to create a message banner effect. The idea being this will look more like a title. 

General messages and instructions will be displayed in the default white text with a black background.

This difference in styling and presentation of the text messages is intended to create the impression that the player is 'being spoken to' by an advisor or second in command with the green messages, whilst the red messages can be clearly identified as 'the enemy'. This effect should make the game feel more human, make for a more engaging game and keep the player wanting to play. 

### Emoji

I will use the emoji library to add smileys, frown faces etc at relevant points in the game to accompany messages. E.g. a big smiley face will come after the initial Welcome to the Game message, a frown or angry face may accompany the message that one of the players ships have been hit. 

Similar to the colouring of the text, this will create a more human experience whilst playing the game, adding a touch of emotion to certain events, improving the overall experience and making the game more engaging. 

### Flow Diagrams

The below is a link to the original flow chart designed for this project. It the top hyperlink doesn't work please use the link immediately below:

[First Flow Diagram](https://lucid.app/lucidchart/5d689449-5866-4bfb-8a0e-fb4715e93c02/edit?viewport_loc=8%2C395%2C1365%2C641%2C0_0&invitationId=inv_986bc45a-fb6d-4b80-b4b2-52cddf59675b)
[First Flow Diagram](documentation/first-flowchart.png)

## Features

As a python driven project, this game does not really have features in the same way as a website. However there are a number of functions which display information to the player or require input from the player which are particularly relevant to the game play and experience. 

### Welcome Message and Board Size Selection

Accompanying the welcome message, the player will be asked to enter one of two options for the size of the board. This input will be used in the functions to create game boards of the relevant size. Validation will be used to ensure a viable input is given and the game will begin from this point.

### Displaying Boards

At the start of the players turn a function will be used to present the layout and position of the players ships. This will need to show the ships on the board in a way which is as close as possible to an actual game board of battleships to ensure a good experience and fun game. 

A similar function will be needed to show where the player has fired and whether or not they have hit the computers ships. Care will need to be taken to ensure that only shots are displayed, and the computer ships themselves are not revealed. Again this will need to match an actual battleships board as closely as possible.

### Player Fire 

After the player and computer boards have been created the player will be asked to input coordinates to 'fire on'. The required format of this input will be explained and validation will be used to ensure that a viable input is provided by the player so the game can continue.

### Game over

Once all the ships on either the player or computer board have been sunk I want to incorporate a function which displays a congratulations/commiserations message and gives the option to start another game immediately from that point, without repeating instructions or welcome messages. 

## Future Implementations/Plans

In the future I would like to incorporate:

Intelligence in Computer Fire - To make the game more challenging and improve the play, in the future I would like to add some aspect of intelligence into the computers fire. As a function this could be done with a boolean value, if the computers last shot was a hit, this could set the value to true. If this value was true the computer would access its last fire coordinates and then fire around these coordinates, essentially trying to sink the players ship, in the way a human player might. This could be quite a challenging function to create, it would require a significant amount of validation to make sure these 'intelligent' shots didn't go off the board or on coordinates that had already been fired on. Another challenging aspect would be to keep the computer firing around its hit coordinates, even if subsequent shots around these coordinates has missed, so essentially keeping the computer firing in the right part of the board until it sunk a ship. The time I think it would take to make this work as intended against the project deadline was the reason I didn't develop it, but it would certainly make an interesting challenge to code, and add a dimension of difficulty to the game.

Horizontal and Vertical Ship Placement - It would be good to build on the existing ship placement functionality with the possibility of vertical ship placement as well as horizontal. This could be done by accessing a specific index on each row of the board and setting these to a particular ship value. However creating the function to be able to do this, as well as horizontal placement, without running into errors, ships being placed over each other etc, would be time consuming to create and is a relatively minor element of the game play. 

### Accessibility

As a command line project there are few options to improve or consider accessibility, however care has been taken to ensure that good contrast is maintained when coloured text is used. 

## Technologies Used

### Languages Used

This project is written in Python. 

### Libraries and External Sources

- Git - Version control.

- Github - To save and store code for the game itself. 

- Heroku - The platform for deploying the game as an app.

- Code anywhere - The workspace and IDE for producing the game.

- Flow Diagrams

- Colorama - Library imported for coloured text

- Emoji - Library imported for emojis

- W3C Validators - For checking validity of HTML and CSS.

- JSHint - Used to check the validity and quality of Javascript.

## Deployment

This was website was deployed using Heroku. Instructions to do this are:

1. Go to Github and Log in (or sign up).

2. Find the repository for this project, TomLiDev/battleships

3. Copy the code from the repository into your IDE

4. In your IDE, create the requirements.txt doc with the pip3 > freeze command, ensuring the requirements.txt is named exactly that. 

5. Go to Heroku, and log in (or sign up)

6. Navigate to the Heroku Dashboard and click "Create new app".

7. Enter a name

8. From the "Add buildpack" option, add the Python buildpack and save

9. Add the node.js buildpack and save

10. Select Github from the deployment method

11. Find the repository name for this project, battleships (TomLiDev), click connect

12. Scroll to the next section and select automatic deploys

## Local Development

### How to fork

1. Log in (or sign up) to Github.

2. Go to the repository for this project, TomLiDev/battleships.

3. Click the Fork button in the top right corner.

### How to clone

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, TomLiDev/battleships.

3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.

4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

Please see seperate testing.md for full details.

[Testing](TESTING.md)

## Credits

### Code Used

The following sites were used for information/code:

#### List comprehension for correct game board creation

https://nedbatchelder.com/blog/201308/names_and_values_making_a_game_board.html

#### List comprehension for creatinf row_references list

https://www.geeksforgeeks.org/python-get-first-element-of-each-sublist/

### Content

The majority of the content was created by the author.

The emojis displayed with some of the messages are accessed via the imported emoji library. 

## Acknowledgements

- Graeme Taylor - My Code Institute Mentor

- My family - For your help in testing, playing my game and providing feedback.