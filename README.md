# rock-paper-scissors-exercise

Welcome to this Rock, Paper, Scissors program

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/willschmitz/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer. Then navigate there from the command line to the root directory prior to running your other commands.
````
cd desktop/rock-paper-scissors-exercise
````
Then you should use Anaconda to create and activate a new virtual environment
````
conda create -n my-first-env python=3.7  #This is only necessary the first time
conda activate my-first-env
````

After you create the virtual environment, you need to install some package dependancies. (See the [requirements.txt] (/requirements.txt) file) Run: 
````
pip install -r requirements.txt 
````

#Setup
In the root directory of your local depository, create a new file called ".env" and update the contents of the file with your desired username for the game. (Make sure to save the file afterwards). Use the variable PLAYER_NAME="" anf fill in your preferred name. 

#Usage
Run the python script:
```py
python Game.py
