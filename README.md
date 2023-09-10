# Battleships!

## Overview

This project was intended to provide a fun game based on the classic battleships game. 

![An image of the finished website on different devices](documentation/space-quiz-homepage-devices.png)

Please use the link below to view the live, deployed game as an app on the Heroku platform:

[Battleships! Live game](https://tomlidev.github.io/Space-Quiz-Pilot-Assessment/)

## CONTENTS

- [User Experience](#user-experience)

- [User Stories](#user-stories)

- [Design](#design)

- [Colour Scheme](#colour-scheme)

- [Typography](#typography)

- [Imagery](#imagery)

- [Wireframes](#wireframes)

- [Features](#features)

- [General Features on All Pages](#general-features-on-all-pages)

- [Homepage](#homepage)

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

Key Features:

- The main battleships game. 

- Instructions for how to play the game. 

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

### Imagery

### Wireframes

[404 Error page Wireframe](documentation/wireframe-error-page.png)

## Features

As a python driven project, this game does not really have features in the same way as a website. However there are a number of functions which display information to the player or require input from the player which are particularly relevant to the game play and experience. 

### Welcome Message and Board Size Selection

Accompanying the welcome message, the player will be asked to enter one of two options for the size of the board. This input will be used in the functions to create game boards of the relevant size. Validation will be used to ensure a viable input is given and the game will begin from this point.

### Player Fire 

After the player and computer boards have been created the player will be asked to input coordinates to 'fire on'. The required format of this input will be explained and validation will be used to ensure that a viable input is provided by the player so the game can continue. 

### Displaying of Player Board and Computer Board

At the start of the players turn a function will be used to present the layout and position of the players ships. This will need to show the ships on the board in a way which is as close as possible to an actual game board of battleships to ensure a good experience and fun game. 

A similar function will be needed to show where the player has fired and whether or not they have hit the computers ships. Care will need to be taken to ensure that only shots are displayed, and the computer ships themselves are not revealed. Again this will need to match an actual battleships board as closely as possible.

### Game over

Once all the ships on either the player or computer board have been sunk I want to incorporate a function which displays a congratulations/commiserations message and gives the option to start another game immediately from that point, without repeating instructions or welcome messages. 

## Future Implementations/Plans

In the future I would like to incorporate:

A Timer - If I was to create this quiz again, instead of using a fixed number of questions, I would utilise a timer function and have the user answer as many questions as possible. This would make the game more more dynamic and exciting with a "race against the clock" element. I also think it would give a wider range of scores making the leaderboard more interesting, whilst also meaning players could look to play multiple times simply to beat their last score. This would require a much larger question bank than the site currently holds.

Difficulty Options - Different difficulty settings were something I was hoping to incorporate into this version of the quiz. I had moved the question bank constant into a separate dedicated Javascript file, with this to be exported into the HTML pages with the relevant script at the bottom of each HTML page.

![Image of separate Javascript file for questions](documentation/seperate-js-questions.png)

This seemed to be working well in the Code Anywhere - Python version of the webiste, however when I played the game on the deployed site from Github pages, the console showed an error Cannot load source. The somewhat broad description of the issue, and the fact that it only appeared in the deployed site, not the python site, with the impending deadline date simply meant I did not have the time to explore and resolve the issue. Therefore unfortunately I was forced to return the questionBank constant back into the original js file and remove the links.

This was a shame as I has explored using chatGBT to do most of the creation for easy, medium and hard question sets which would have greatly reduced the amount of time taken to simply create the questions. From there it would have been relativley simple to incorporate a button/option on the username page for the user to select difficulty, which could then have been used as the value to determine which set of questions were to be loaded into the shuffle questions function. From there the rest of the functions would have worked. The only other aspect which may have needed working would be greater scores for more difficult questions answered correctly, but again this would have been relatively simple to incorporate with an if statement checking the difficulty of the game as the add correct score function.

This is something I will explore further in my own time as it seems valuable not only for this quiz but for using separate Javascript files in future projects.

### Accessibility

This site has been built to be as accessible as possible, specifically:

- All images have alt text attributes and all links have aria labels for use by screen readers.

- The colour scheme has been chosen to ensure a good level of contrast is maintained for text across the site.

- Semantic markup has been used throughout.

- Including hover states to aid navigation.

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

2. Find the repository for this project, TomLiDev/Space-Quiz-Pilot-Assessment.

3. Click on the Settings link.

4. Click on the Pages link in the left hand side navigation bar.

5. In the Source section, choose main from the drop down select branch menu. Select Root from the drop down select folder menu.

6. Click Save. Your live Github Pages site is now deployed at the URL shown.

## Local Development

### How to fork

1. Log in (or sign up) to Github.

2. Go to the repository for this project, TomLiDev/Space-Quiz-Pilot-Assessment.

3. Click the Fork button in the top right corner.

### How to clone

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, TomLiDev/Space-Quiz-Pilot-Assessment.

3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.

4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.

5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

Please see seperate testing.md for full details.

[Testing](TESTING.md)

## Credits

### Code Used

The following sites were used for information/code:

####

#### Fisher-Yates Shuffle Algorithm

https://stackoverflow.com/questions/59810241/how-to-fisher-yates-shuffle-a-javascript-array

#### Session Storage

https://www.w3schools.com/jsref/prop_win_sessionstorage.asp

#### Sorting Array of Objects Based on Shared Object Property

https://flaviocopes.com/how-to-sort-array-of-objects-by-property-javascript/

### Content

The majority of the content was created by the author.

This site was used for the background image:
https://free4kwallpapers.com/space/space-background-wallpaper--27kA

Some of the quiz questions came from this site:
https://icebreakerideas.com/space-trivia/

## Acknowledgements

- Graeme Taylor - My Code Institute Mentor

- My family - For your help in testing, playing my game and providing feedback.