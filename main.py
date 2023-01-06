import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help = "Defines file to read from")

args = parser.parse_args()
zero_space_unicode = "​"
weird_space_unicode = " "
musical_thing = "ㅤ"
invisible_plus = "⁤"

if args.input:
    file = args.input

textFile = open(file, "r")
inputtedText = textFile.read()
textFile.close()

chunkedList = inputtedText.split(" ")
final = ""
flipper = 0
randoms = []
while flipper < 3:
    randoms.append(random.randint(0, len(inputtedText)))
    flipper = flipper + 1

for place in randoms:                    #put weirdness here
    inputtedText = inputtedText[:place] + zero_space_unicode + inputtedText[place:]

file = file[:-4] + "_output.txt"

fobj = open(file, "w", encoding="utf-8")
fobj.write(inputtedText)
fobj.close()

