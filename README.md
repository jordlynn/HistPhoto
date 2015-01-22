# HistPhoto
A project for the University of Idaho library. I was tasked with designing a python program that would go through an entire .csv file and find all the names for jpg images. Then check if those images actually exist on the server, once they are found create a new .csv file that will have a column "thumbnail" that will have the image's name in that column or blank if the image doesn't exist.

#Usage
A simple execution is all that is needed of this python program: ``` ./checker.py ``` I've tried to add as much feedback in the form of print statements to the consol that is used to execute, once the program is actually comparing the two lists processing will take some time. current runtime on a list in the thousands takes 3-5 minutes

#Possible Improvements
This program is far from perfect, the search time comparing the lists is pretty high, a simple BST or even a bloom filter would really speed things up. I was told it needed to be simple enough a "non computer" person could edit and change it over time so a Linked List was choosen and I give a breif explanation of how this works in the comments of the code.
