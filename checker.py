#!/usr/local/bin/python
# libraries
import os
import csv
import urllib2
import re
import os


debugging = False

# classes
# We'll use a simple LL data structure to dynamically store the names that
# are going to be read from the pgX.txt file, I considered writing to an
# external file but bandwidth and data conservation seems to be a importnat
# issue in this office so this software will be more mindfull of it's calls
# to write to disk. Node class for LL follows:
class Node:
  def __init__ (self, data=None, keep=None, next=None):
    self.data = data
    self.keep = keep
    self.next = next

  def __str__ (self):
    return str(self.data)

  def SetNext(self, newNext):
    self.next = newNext

  def getNext(self):
    return self.next


class LinkedList:
  def __init__ (self):
    self.head = None
    self.conductor = self.head

  def CreateNode(self, item):
    temp = Node(item)
    temp.next = self.head
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()

    return count
  
  def PrintList(self, node):
    if node == None: return
    while node:
      print (node.data)
      node = node.next
    return
  

  def ReturnData(self, node):
    if node == None: print("ERROR! no list exists!")
    temp = node.data
    return temp
  
def ReverseNonDestructiveList(head):
  newList = LinkedList()
  newHead = None
  
  while head:
    temp = head.data
    
    newHead = newList.CreateNode(head.data)
    head = head.next
  
  return newList
  

def DeleteNode(mainList, node):
  if mainList == None:
    print("Can't remove from an empty list!")
    return
  current = mainList.head
  previous = None
  found = False
  
  while not found:
    if current == node:
      found = True
    elif current is None:
      raise ValueError("Node not in Linked List")
    else:
      previous = current
      current = current.next
      
    if previous is None:
      mainList.head = current.next
    else:
      previous.next = current.next
        
  return
    

#_DEPRECIATED_!
# FindPicNames can find image names inside a given folder on the local drive.
# this function is no longer used because we want to grab the info off a webpage.
#def FindPicNames(pgFolder):
#  picNames = [os.path.basename(x) for x in glob.glob(pgFolder + '/*.jpg')]
#  return picNames





def FindPicFolders():
  picFolders = [] # an array variable that holds the name of picture folders  
  #folderResponse = urllib2.urlopen('http://www.lib.uidaho.edu/special-collections/histphoto/')
  #expr = re.compile('pg[0-9]+', re.IGNORECASE)
 
  picFolders.append("pg1")
  picFolders.append("pg2")  
  picFolders.append("pg3")
  picFolders.append("pg4")
  picFolders.append("pg5")
  picFolders.append("pg6")
  picFolders.append("pg7")
  picFolders.append("pg8")
  picFolders.append("pg9")
  picFolders.append("pg10")
  picFolders.append("pg11")
  picFolders.append("pg12")
  picFolders.append("pg13")
  picFolders.append("pg14")
  picFolders.append("pg15")
  picFolders.append("pg16")
  picFolders.append("pg17")
  picFolders.append("pg18")
  picFolders.append("pg20")
  picFolders.append("pg21")
  picFolders.append("pg25")
  picFolders.append("pg26")
  picFolders.append("pg29")
  picFolders.append("pg32")
  picFolders.append("pg34")
  picFolders.append("pg35")
  picFolders.append("pg37")
  picFolders.append("pg38")
  picFolders.append("pg40")
  picFolders.append("pg60")
  picFolders.append("pg64")
  picFolders.append("pg65")
  picFolders.append("pg67")
  picFolders.append("pg68")
  picFolders.append("pg70")
  picFolders.append("pg71")
  picFolders.append("pg72")
  picFolders.append("pg73")
  picFolders.append("pg74")
  picFolders.append("pg75")
  picFolders.append("pg78")
  picFolders.append("pg79")
  picFolders.append("pg80")
  picFolders.append("pg81")
  picFolders.append("pg82")
  picFolders.append("pg83")
  picFolders.append("pg89")
  picFolders.append("pg90")
  picFolders.append("pg91")
  picFolders.append("pg92")
  picFolders.append("pg93")
  picFolders.append("pg95")
  picFolders.append("pg96")
  picFolders.append("pg97")
  picFolders.append("pg98")
  picFolders.append("pg99")
  picFolders.append("pg100")
  picFolders.append("pg101")
  picFolders.append("pg103")
  picFolders.append("pg6008")
  picFolders.append("pg6010")
  picFolders.append("pg6101")

  return picFolders

# RemoveMissing will work it's way through a LL and remove
# any nodes that do not have a corresponding image.
def RemoveMissing(foundPics, mainList):
  if mainList == None or foundPics == None : return # test conditionals
  
  else:
    node = mainList.head
    
    for picName in foundPics:
      
      while node != None:
    
        if picName == "" or node.data == "":
          node = node.next
        elif picName == node.data:
          node.keep = 1
          node = node.next
        else:
          node = node.next
        
      if node == None:
        node = mainList.head
        
  return mainList

# ReturnPages will go to the given web folder and return a list of all
# images that are found in the webpage
def ReturnPages( pgFolderName ):
  response = urllib2.urlopen('http://www.lib.uidaho.edu/special-collections/histphoto/' + pgFolderName + '/')
  arryOfImages = []
  
  for line in response:
    temp = line.find("href=")
    temp2 = line.find(".jpg")
    image = line[temp+6 : temp2+4]
    #print image #used for debugging
    if image != "":
      arryOfImages.append(image)
    
  return arryOfImages




def main():
    CSVin = open("HistPhotoTest.csv", "rb")
    CSVout = open("HistPhotoTestnew.csv", "wb")

    
    
    print("Creating linked list...")
    mainList = LinkedList()
    
    print("Filling list with possible names...")
    reader = csv.reader(CSVin)
    
    # ###################
    for line in reader:
      temp = line[0] + "-" +line[8] + ".jpg"
      mainList.CreateNode(temp)
    
    print("Done filling list!")
      
      
    print("Reversing list to match .cvs file...")
    mainList = ReverseNonDestructiveList(mainList.head)
    print("Done reordering list!")
      

    
    # Now that we have our list of possible pictures we are going to go through and
    # find those actual .jpg images.
    print("Finding folders with images on server...")
    pgFolders = FindPicFolders()
    
    # Now we have a list of PG# folders lets check for .jpg inside them

    foundPics = []
    for folder in pgFolders:
      newPID = os.fork()
      if newPID == 0:
        foundPics.append(ReturnPages(folder))
      else:
        print "ERROR FORKING!"
    
    print("Comparing images to list...")
    
    
    # foundPics will be an array of arrays each with their respective PG
    # folder, each folder is checked and then returned with the correct
    # images removed.    
    
    for imageList in foundPics:
      newPID = os.fork()
      if newPID == 0:
        RemoveMissing(imageList, mainList)

      
    print("Done comparing!")


    
    
    print("Beginging to write list to new .csv file...")
    # Now that we have the whole list of possible pictures we need to load
    # the image names into the .csv file "reader" reads from our source
    # csv file while writer will write to a new updated csv file
    
    CSVin.seek(0) # we need to start over at the begining of the file.
    writer = csv.writer(CSVout)
    
    node = mainList.head
    i = 0

   # This for loop is the heart of the second part of the program.
   # it will read one "row" at a time from the original file,
   # take that rown and in the 10th column (our thumbnail column)
   # it will insert the data payload from the first noad in the
   # linked list then writes the new row to the new csv file.
   # the inital "i" counter is just there so that the file will
   # eat the first line. This could be done more elegantly...

    
    
    
    for row in reader:
      if i > 0:
        #if mainList.ReturnData(node) != "": print(mainList.ReturnData(node)) #used for debugging.
        if node.keep == 1:
          row[10] = mainList.ReturnData(node)
          writer.writerow(row)
        else:
          writer.writerow(row)
          
      else:
        writer.writerow(row)
        i = 1
      node = node.next
    
    # Now that we're finished let the user know and 
    # close our .csv files.
    print("Finished writing to file!")
    CSVin.close()
    CSVout.close()
    
    
    print("done!")
    return

main()
