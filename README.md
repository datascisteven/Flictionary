<center><h1><font size=18>Flictionary</font></h1></center>
 
# Introduction

We were participats of the Flatiron School Game Jam, which was centered on the theme of Pursuing Mastery and was conducted by Cody Miller. This was an opportunity for Flatiron software engineers, data scientists, designers, and cybersecurity students to build something together through the medium of a game. The game can be anything that you can think of, but it is all about making an enjoyable experience.

Here were some of the guidelines we were given:

- Use all of your diverse skills to collaborate and put something together that showcases the value of Pursuing Mastery through the medium of developing a game
- Making a game can be a lot of fun, having to think through the logic of everything that happens in your game and anticipate how the user will play your game is a blast.
- Make sure your are utilizing the skills of your entire team when building this thing is a challenge.
- Working together with others that think differently than you is an invaluable experience that will pay dividends in the job search and your career in general.

A group of 8 alumni banded together comprising of 2 DS, 5 SE, and 1 UX/UI alumni, and we landed on this idea of a Pictionary-inspired app. In an effort to get data science represented, I had just talked to Cody about image recognition in games. There was lots of excitement around making such a game, but our biggest quandary ultimately proved to be how do we connnect front-end to the back-end.

This repository represents the continued efforts of a hodgepodge of Flatiron alumnni to build a Pictionary-inspired gaming app, Flictionary, including those from the Software Engineering, Data Science, and UX/UI programs, but as a data scientist, this represents more of the backend efforts to develop a neural network for deployment onto Flask.

We split into two groups, front-end and back-end, with front-end using React, HTML/CSS, Javascript and the back-end using Python and Flask. I ended up leading the back-end team, and we met separately as teams first, but then came together to collaborate over Discord and Zoom, and we met every weekday at a  scheduled time over a two week period. 

# Brainstorming 

Some of front-end considerations for the game:

1. what features did we want on the user game interface?
2. did we want the player to compete against the computer or against another player?
2. do we have front-end call back to model after submitting or on a consistent basis as we draw
3. how do we get information to the back-end or from the back-end?

Some of the back-end considerations for the game:

1. what kind of neural network do we need to use?
2. how big is this dataset?
3. do we need to deploy this on a cloud service instead of Heroku?

I will speak to some of these points.  Some of the features we landed on were a drawing pad with a clear screen button, login or signup, timer, drawing pad with different pencils, profile picture/creation, leaderboard.

One of our team members has an artistic son, and she gave us feedback that he would love being able to have the computer guess his drawing as he continued to draw. We stuck with the simpler model of drawing and submit for time's sake.

We ended up picking 10 animals to work with in developing a neural network because it was much easier to manage. We initially started to work with jsut the numpy files as they were relatively small in size as compared to the raw or simplified versions.

I am currently working on developing a better neural network with greater accuracy

# Data Sources:

The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The drawings were captured as timestamped vectors, tagged with metadata including what the player was asked to draw and in which country the player was located. You can browse the recognized drawings on [quickdraw.withgoogle.com/data](https://quickdraw.withgoogle.com/data).


Here is the Github link for the dataset:  [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)


# Data Understanding:

There were 47 animals in the dataset out of the 345 categories.



# Modeling:






# Results:





# Folder Structure:






# Contact Information:









  