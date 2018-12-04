# trumptweets
Trump Tweet generation project for machine learning class.

Final project for Machine Learning class at Wichita State University.
<br>
Authors: Jack Hale, Matt Madden, Tyler Espinoza, Zubair Khan

Usage: <br>
To use the recursive neural network trained for the final presentation of the project, do the following steps:
1. Install Python 3.6
2. Clone the repository
3. pip install tensorflow
4. pip install textgenrnn
5. cd into repository directory
6. **python text_gen_from_save.py {number of tweets} {prefix string} {degrees of freedom}**

NOTE: degree of freedom should be between 0.0 and 1.0 - we recommend a value of 0.5
<br>
NOTE: set prefix string = "None" to have the neural network generate an tweet from scratch.
