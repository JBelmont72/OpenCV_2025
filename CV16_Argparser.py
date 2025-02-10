'''Argparser from Geeksfor Geeks.org
also from pyImage is https://pyimagesearch.com/2018/03/12/python-argparse-command-line-arguments/

Syntax: class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars=’-‘, fromfile_prefix_chars=None, argument_default=None, conflict_handler=’error’, add_help=True, allow_abbrev=True) Parameters:
https://www.geeksforgeeks.org/command-line-option-and-argument-parsing-using-argparse-in-python/?ref=ml_lbp

prog– name of the program (default=sys.argv[0])
usage– string describes the program usage(default: generated from arguments added to the parser)
description– text to display before the argument help(default: none)
epilog– text to display after the argument help (default: none)
parents– list of ArgumentParser objects whose arguments should also be included
formatter_class– class for customizing the help output
prefix_chars– set of characters that prefix optional arguments (default: ‘-‘)
fromfile_prefix_chars– set of characters that prefix files from which additional arguments should be read (default: None)
argument_default– global default value for arguments (default: None)
conflict_handler– strategy for resolving conflicting optionals (usually unnecessary)
add_help– Add a -h/–help option to the parser (default: True)
allow_abbrev– Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)
Adding Arguments: Next step is to fill the ArgumentParser with the information about the arguments of the program. This implies a call to the add_argument() method. These information tell ArgumentParser how to take arguments from the command-line and turn them into objects.

Syntax: ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest]) Parameters:

name or flags– either a name or list of option string
action– basic type of action to be taken when this argument is encountered at the command line
nargs– number of command-line arguments that should be consumed
const– constant value required by some action and nargs selections
default– value produced if the arguments are absent from the command line
type– type to which the command line arguments should be converted.
choices – A container of the allowable values for the argument
required – Whether or not the command-line option may be omitted (optionals only)
help– brief description of what the argument does
metavar – A name for the argument in usage messages
dest – The name of the attribute to be added to the object returned by parse_args()
Parsing Arguments: The information gathered in the step 2 is stored and used when arguments are parsed through parse_args(). The data is initially stored in sys.argv array in a string format. Calling parse_args() with the command-line data first converts them into the required data type and then invokes the appropriate action to produce a result.

Syntax: ArgumentParser.parse_args(args=None, namespace=None) Parameter:

args – List of strings to parse. The default is taken from sys.argv.
namespace – An object to take the attributes. The default is a new empty Namespace object
Application of Argparse in Python
In most cases, this means a simple Namespace object will be built up from attributes parsed out of the command line:

Namespace(accumulate=, integers=[ 2, 8, -7, 41 ])
These were the root concepts you need to be familiar with to deal with argparse. The following are some examples to support this application.

Example 1: To find the sum of command-line arguments using argparse

This code employs the ‘argparse' module to create a command-line interface for processing integers. It defines two command-line arguments: ‘integers’ to accept multiple integer values, and ‘accumulate’ to perform a sum operation on those integers. When the script is executed with integer values as arguments, it parses and calculates the sum of those integers, displaying the result. It provides a convenient way to perform integer accumulation through the command line.

'''
# import argparse
# parser = argparse.ArgumentParser(description ='Process some integers.')
# parser.add_argument('integers', metavar ='N', 
# 					type = int, nargs ='+',
# 					help ='an integer for the accumulator')

# parser.add_argument(dest ='accumulate', 
# 					action ='store_const',
# 					const = sum, 
# 					help ='sum the integers')

# args = parser.parse_args()
# print(args.accumulate(args.integers))
##########
# # import the necessary packages
# import argparse
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--name", required=True,
# 	help="name of the user")
# args = vars(ap.parse_args())
# # display a friendly message to the user
# print("Hi there {}, it's nice to meet you!".format(args["name"]))
#############
#Codeblock #1: Lines 1-20# import the necessary packages
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()	## instantiate object 'ap'

ap.add_argument("-i", "--input", required=True,
	help="path to input image")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
args = vars(ap.parse_args())
# load the input image from disk
image = cv2.imread(args["input"])
while True:
	# convert the image to grayscale, blur it, and threshold it
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5,5), 0)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	# extract contours from the image
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# loop over the contours and draw them on the input image
	for c in cnts:
		cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
	# display the total number of shapes on the image
	text = "I found {} total shapes".format(len(cnts))
	cv2.putText(image, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
		(0, 0, 255), 2)
	# write the output image to disk
	cv2.imshow('frame',image)
 	
	if cv2.waitKey(1) & 0xFF==ord('c'):

		cv2.imwrite(args["output"], image)
		break
     

		
cv2.destroyAllWindows()