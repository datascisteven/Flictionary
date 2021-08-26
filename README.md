<center><h1><font size=18>Flictionary</font></h1></center>
 
# Introduction:

A ragtag group of 8 alumni comprising of 2 DS, 5 SE, and 1 UX/UI banded together for the Flatiron School Game Jam.  The hackathon was centered around the theme of Pursuing Mastery and was conducted by SE alum Cody Miller. This was an opportunity for Flatiron alums from the different programs (software engineers, data scientists, designers, and cybersecurity) to synergistically (and sometimes not) build something together through the medium of a game. The game can be anything that the group brainstorms together on the first day, but it is all about making an enjoyable experience.

This repository represents the continued efforts of this hodgepodge of Flatiron alumni to build a Pictionary-inspired gaming app, which we ultimately named Flictionary, but as the lead of the back-end team, this repo represents more of the backend efforts to develop a neural network for deployment onto Flask.

# Background:

Here were some of the guidelines we were given:

- Use all of your diverse skills to collaborate and put something together that showcases the value of Pursuing Mastery through the medium of developing a game.
- Making a game can be a lot of fun, having to think through the logic of everything that happens in your game and anticipate how the user will play your game is a blast.
- Make sure you are utilizing the skills of your entire team when building this thing is a challenge.
- Working together with others that think differently than you is an invaluable experience that will pay dividends in the job search and your career in general.

# Blog:

Please stay tuned for the blog on Medium describing our brainstorming process, group dynamics, recap of our group chats and meetings, what our successes and challenges were, what I learned from the experience, as well as our future steps.

While there were many passionate people working hard over the past two weeks on this project and were enthusiastic to see it go to completion, I recognize that job searching and life demands can take priority, and the project may go to the backburner.


# Data Sources:

The Quick Draw Dataset is a collection of 50 million drawings across 345 categories, contributed by players of the game Quick, Draw!. The drawings were captured as timestamped vectors, tagged with metadata including what the player was asked to draw and in which country the player was located. You can browse the recognized drawings on [quickdraw.withgoogle.com/data](https://quickdraw.withgoogle.com/data).

Kaggle hosted a Quick, Draw! Doodle Recognition Challenge 3 years ago, and they released another format for the images and we used that dataset for some of the models:  [https://www.kaggle.com/c/quickdraw-doodle-recognition/data](https://www.kaggle.com/c/quickdraw-doodle-recognition/data)
 

Github link for the dataset:  [https://github.com/googlecreativelab/quickdraw-dataset](https://github.com/googlecreativelab/quickdraw-dataset)

The original Google Quick, Draw Game:  [https://quickdraw.withgoogle.com](https://quickdraw.withgoogle.com)

Here is the link to the deployment of game as continued work in progress:  Coming soon


# Data Understanding:

The original dataset contains 345 categories, but we opted to use animals for our game as they are fun to draw and would appeal to a younger and older audience.  There were 47 animals in the dataset out of the 345 categories, and we ultimately picked 10 animals for our modeling.

Google published the Quick Draw data in four different formats:

1. raw dataset: `*.ndjson`
2. simplified drawing files: `*.ndjson`
3. binary files: `*.bin`
4. numpy bitmaps: `*.npy`

The raw dataset is available as ndjson files separated by category with the following keys:

- key_id: unique identifier across all drawings
- word: category that player prompted to draw
- recognized: whether word recognized by game
- timestamp: when drawing was created
- countrycode: two letter country code
- drawing: JSON array representing vector drawing

The simplified drawing files are also in ndjson format, but the vectors were simplified, removed the timing indo, and positioned and scaled to a 256x256 region. The binary format is for efficient comprehension and laoding. The simplified drawings were rendered into a 28x28 grayscale bitmap in numpy (`*.npy`) fromat.

# Modeling:

For the backend, there were two considerations for developing the model:

1. Which set of image files to 

To Be Continued....





# Results:

To Be Continued










# Folder Structure:

	├── README.md               	<- the top-level README for reviewers of this project
	├── _notebooks			<- folder containing all the project notebooks
	│   ├── cnn.ipynb		<- notebook for CNN model
	│   ├── EDA.ipynb		<- notebook for dataset understanding and EDA
	│   ├── mobilenet.ipynb		<- notebook for MobileNet model
	│   ├── pytorch.ipynb		<- notebook for Pytorch model
	│   └── shuffle_csv.ipynb  	<- notebook for creating shuffle csvs
	├── final_notebook.ipynb    	<- final notebook for overall project
	├── _src                    	<- folder of python files for building model for Flask
	│   ├── build_model.py		<- python file for building RNN model
	│   ├── simple_conv_nn.py	<- python file for building CNN model
	│   └── image_utils.py  	<- python file for working with images
	├── _data                   	<- folder of various data files
	├── _Flictionary_App        	<- folder for Flask files
	│   ├── _templates		<- notebook for dataset understanding and EDA
	│   │   ├── index.html		<- landing page for Flask app
	│   │   └──  hook.html		<- post-submission page for Flask app
	│   └── run.py			<- python file to run Flask app
	└── Project_Presentation.pdf	<- pdf of the presentation



# Contributors:

***Front-End Team:***

- **[BMoClay](https://github.com/BMoClay)**
- **[Chanson9892](https://github.com/Chanson9892)**
- **[darrickpang](https://github.com/darrickpang)**

***Back-End Team:***

- **[Jkang91](https:///github.com/JKang91)**
- **[oklena](https://github.com/oklena)**
- **[roadpilot](https//github.com/roadpilot)**


# Contact Information:

[![Email Badge](https://img.shields.io/static/v1?label=Email&message=stevenyan@uchicago.edu&color=8b0000&style=for-the-badge&logo=GMail&logoColor=white&logoWidth=30)](mailto:stevenyan@uchicago.edu)

[![Github Badge](https://img.shields.io/static/v1?label=GitHub&message=@datascisteven&color=9966CC&style=for-the-badge&logo=GitHub&logoWidth=30)](https://www.github.com/datascisteven)

[![LinkedIn Badge](https://img.shields.io/static/v1?label=LinkedIn&message=@datascisteven&color=0A66C2&style=for-the-badge&logo=LinkedIn&logoWidth=30)](https://www.linkedin.com/in/datascisteven)

[![Medium Badge](https://img.shields.io/static/v1?label=Medium&message=@datascisteven&color=003366&style=for-the-badge&logo=Medium&logoWidth=30)](https://datascisteven.medium.com)

[![Portfolio Badge](https://img.shields.io/static/v1?label=Website&message=datascisteven.github.io&color=FF6600&style=for-the-badge&logo=GoogleChrome&logoColor=white&logoWidth=30)](https://datascisteven.github.io)
 






  
