#import modules
import operator
import os
from os import listdir
from os.path import join
from PyPDF2 import PdfFileMerger


# define merger
merger = PdfFileMerger()

#define path
path = '/home/bivu/Documents/ebookTDD/'

#obtain list of all files and sort by name
allFiles = listdir(path)

#sorting by filename
fileList = {}
for files in sorted(allFiles):
    name = files.split(".")
    index = int(name[0])
    fileList.update({ files : index })

sortedFileList = sorted(fileList.iteritems(), key=operator.itemgetter(1))


#make a loop to append require files to merger()
for fileName, index in sortedFileList:
    inputFile = os.path.join(path, fileName)
    inputFile = open(inputFile, "rb")
    merger.append(inputFile)


#define the output file and print it
output = os.path.join(path, "SingleTDD.pdf")
output = open(output, "wb")
merger.write(output)
	