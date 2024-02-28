# EPQ-project
This contains every piece of code that I have written for my EPQ project, whether it is a beta of the final code, some testing or simply me doing some random code practice
Every single piece of code will be written in python 3.12, so to see the code in action, a python interpreter needs to be installed

#-Explanation of project-

The project is on a simulation on evolution. In the simulation, there are a set number of agents(computer generated species) and mushrooms. At the start of a generation, each agent will go around and eat random mushrooms on the floor(psa don't do this in real life this is a simulation only). The mushroom has a health value and a poison value. If the health value is greater than the poison value, the mushroom will be green, and the agent's health would increase. Otherwise, if the poison value is greater, the mushroom will be red, and the agent's health will decrease. At the end of each generation, the agent breed with each other, and the healthier agent has a higher chance of passing down their genes. Over time, the expected result is that every agent will avoid the red mushrooms and all go for the green mushrooms.




Below are the explanation for every piece of code:

- Genetic_algorithm_beta_1.py:
My first attempt at creating a programme that adapts to the surroundings, which is made trivial through me giving a very simple environment of a quadratic equation. I created this in order to have a general feel for the final project, and to understand the basis of genetic algorithm.
 
