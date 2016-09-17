# Project 4: Reinforcement Learning
## Train a Smartcab How to Drive


This project is part of machine learning nano-degree program. In this part, I implemented a Q-learning algorithm to make decisions for a Smartcab moving in a city that is approximated by a grid. As the cab moves, it encounters other agents or cars in the environment, and based on its actions the cab gets reward. I implemented and tested a Q-learning algorithm, and found that by using 5 states (traffic light information, oncoming traffic and next-waypoint information), the cab was able to navigate by itself. Further, the algorithm was stable enough to scale for scenario with 3 to 40 other agents in the environment. 

The code is organized as follows, 

1. agent_random.py random driving agent.
2. agent_Q.py Q-learning agent with 5 states (traffic light information, 3- oncoming traffic and next-waypoint information). 
3. agent_Q_2states.py Q-learning agent with 2 states (traffic light information and next-waypoint information). 



The results are summarized [here](http://vxy10.github.io/2016/09/16/SmartCab_supplemental/)

Below are youtube videos of the smartcab (red color) moving in environment with 3 and 20 other agents. 

<iframe width="420" height="280" src="https://www.youtube.com/embed/-eYBKD3-NN4" frameborder="0" allowfullscreen></iframe>

<iframe width="420" height="280" src="https://www.youtube.com/embed/a4X9R7v3mrc" frameborder="0" allowfullscreen></iframe>
