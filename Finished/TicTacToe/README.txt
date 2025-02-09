Tic Tac Toe Player

This experiment's goal is to see what is the ideal neural network design that can learn to Tic Tac Toe.

For the network, there wil be 9 input nodes and 9 output nodes. 9 input nodes will be corrispond the 9 
boxes of Tic Tac Toe. Input of 0 will mean theres a free space, 1 means it's take by a friendly mark, 
and a -1 means it's taken by an opponent's mark. The 9 output nodes will corrispond to the 9 boxes that 
the bot can choose from. The experiment will try different numbers of of hidden layers and nodes each. 
During each game, if the network tries to place a mark on a taken square, the game will put a mark on a 
random free spot. 
 
Because of my skill level and technical understanding, I will take a natural selection approach to 
teaching the model. To start, I will initialize 20 neutral networks. The 20 networks will compete in a 
round robin to find which is the best network. The bottom 10 networks will be eliminated and they will be 
replaced by 10 clones of the top 10 networks. Each clone will have a random mutation in in weights and 
biases. I hope this will create an evolutionary model that will produce the most fit network.
