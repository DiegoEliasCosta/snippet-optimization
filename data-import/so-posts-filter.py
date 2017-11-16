import argparse
import os
import time
from datetime import timedelta
import xml.etree.ElementTree as etree


# Report Variables
qInspected = 0
qFound = 0
aFound = 0
startTime = time.time()
nErrors = 0
progressStep = 100000

# progress = 100000

# Question - Answer Map
questionsIdsSet = set()


def isQuestion(elem):
    return elem.get("PostTypeId") == '1'  # Only Questions have titles


def filter_post(file, output, title, tag):
    with open(output, "a") as outputFile:

        # Header
        outputFile.write('<?xml version="1.0" encoding="utf-8"?>')
        # Begin root
        outputFile.write("\n<posts>\n")

        context = iter(etree.iterparse(file))
        _, root = next(context)

        for event, elem in context:
            if isQuestion(elem):
                inspectQuestion(elem, outputFile, tag, title)
            else:
                inspectAnswer(elem, outputFile)
            root.clear()

        outputFile.write("\n</posts>")


def writeToOutput(elem, outputFile):
    global nErrors
    try:
        outputFile.write(etree.tostring(elem, encoding="unicode"))

    except UnicodeEncodeError:
        #print("Error on processing element ")
        nErrors += 1
        # ignore for now
        pass


def inspectAnswer(elem, outputFile):

    global aFound
    global questionsIdsSet

    questionId = elem.get("ParentId")

    # Add answers to the already inspected question
    if questionId in questionsIdsSet:
        writeToOutput(elem, outputFile)
        aFound += 1


def inspectQuestion(elem, outputFile, tag, title):
    global qInspected
    global qFound
    global questionsIdsSet
    global progress
    global startTime
    global progressStep

    qInspected += 1
    # Report progress
    if qInspected % progressStep == 0:
        elapsed = time.time() - startTime
        print("# inspected = %d | # of questions %d | # of answers %d | Time elapsed %s" % (qInspected, qFound, aFound,
                                                                                            timedelta(seconds=elapsed)))

    found = False
    if title and title in str(elem.get("Title")).lower():
        found = True
    if tag and tag in str(elem.get("Tags")).lower():
        found = True

    # Write to file each found record
    if found:
        # Adds the question id to filter the answers
        id = elem.get('Id')
        questionsIdsSet.add(id)
        writeToOutput(elem, outputFile)
        qFound += 1


def existingFile(file):
    if not os.path.isfile(file):
        raise Exception("Invalid or non-existing file...")
    else:
        return file


# Just check whether it is possible to open the file
def creatableFile(file):
    try:
        f = open(file, 'w')
        f.close()
    except FileNotFoundError:
        raise Exception('Can not create the output file.')
    return file


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Stack Overflow Questions Filter')

    parser.add_argument('file', type=existingFile, help='StackOverflow Posts.xml file')
    parser.add_argument('output', type=creatableFile, help='StackOverflow Posts.xml file')
    parser.add_argument('--title', type=str, help='Filter questions by title containing the term')
    parser.add_argument('--tag', type=str, help='Filter by tag containing the term')
    parser.add_argument('--in-memory', action='store_true', help='Execute the filtering in memory [Default=FALSE].')
    parser.add_argument('--progress-step', help='The amount of questions to be inspected before every report.')

    args = parser.parse_args()

    print('Filtering questions from the file %s ' % args.file)

    print('Filtering Criteria')
    title = args.title
    if title:
        title = title.lower()
        print('\tQuestion Title contains: %s' % args.title)

    tag = args.tag
    if args.tag:
        tag = tag.lower()
        print('\tQuestion contains Tag: %s' % args.tag)

    if args.progress_step:
        progressStep = int(args.progress_step)

    if args.in_memory:
        raise NotImplementedError('Functionality not yet implemented')

    filter_post(args.file, args.output, title, tag)

    print('Process Finished')
    print('\t # of Questions Inspected = %d' % qInspected)
    print('\t # of Questions Found = %d' % qFound)
    print('\t # of Answers Found = %d' % aFound)
    print('\t # of Errors = %d' % nErrors)
