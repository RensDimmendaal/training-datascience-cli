# CLI Demo for Sklearn Model

In previous lessons you have already learned the basics of building a classification model with text data.
However, in practice you will notice that it's inconvenient if you have to startup a jupyter notebook every time you want to make a prediction.
In this lesson we show you one basic option to make tools that are useful to yourself and your colleagues.

## Task 1: Explore Fire

[Python Fire](https://github.com/google/python-fire) is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object.

1. Go to the project page and learn how to install it
2. Open the fire_demos folder, look at the code, and try using the tools in the command line

## Task 2: Apply Fire -- Classifying messages as insulting (or not) 

You were asked to make a model which can predict if a message is insulting or not.
To do this you were given a dataset twitter messages, which were labeled as insulting or not. 
As a good data scientist you started working in a notebook, and after some iteration you ended up with 'Untitled 42.ipynb'.
Now the question is: can you turn this into a command line interface?

Your command line interface must be able to:
  1. accept a dataset, train a model, and save it
  2. accept a model, and save the sentiment of each word in the vocabulary
  3. accept a dataset, predict if they are insults, and save it
  4. accept a sentence, predict if it is an insult, and return that info in the command line

Logistics:
* Data is loaded from './data/'
* Store your code in './assignment/'
* Save all output to './output/'