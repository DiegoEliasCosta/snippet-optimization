import argparse
import os
import xml.etree.ElementTree as ET

dir = os.path.join("../data", "pt.stackoverflow.com")
dir = os.path.join("../data", "stackoverflow.com-Posts")

# Report Variables
qInspected = 0
qFound = 0
aFound = 0
# progress = 100000

# Question - Answer Map
questionsIdsSet = set()


def isQuestion(elem):
    return elem.get("PostTypeId") == '1'  # Only Questions have titles


def filter_questions(file, output, title, tag):
    with open(output, "a") as outputFile:

        # Header
        outputFile.write('<?xml version="1.0" encoding="utf-8"?>')
        # Begin root
        outputFile.write("\n<posts>\n")

        # get an iterable
        for event, elem in ET.iterparse(file):

            if isQuestion(elem):
                inspectQuestion(elem, outputFile, tag, title)

            else:
                inspectAnswer(elem, outputFile)

        outputFile.write("\n</posts>")


def inspectAnswer(elem, outputFile):

    global aFound
    global questionsIdsSet

    questionId = elem.get("ParentId")

    # Add answers to the already inspected question
    if questionId in questionsIdsSet:
        outputFile.write(ET.tostring(elem, encoding="unicode"))
        aFound += 1


def inspectQuestion(elem, outputFile, tag, title):
    global qInspected
    global qFound
    global questionsIdsSet
    global progress

    qInspected += 1
    # Report progress
    if qInspected % 100000 == 0:
        print("# of questions inspected = %d | # of questions found %d | # of answers found %d" % (qInspected, qFound, aFound))
    found = False
    if title and title in str(elem.get("Title")):
        found = True
    if tag and tag in str(elem.get("Tag")):
        found = True

    # Write to file each found record
    if found:
        # Adds the question id to filter the answers
        id = elem.get('Id')
        questionsIdsSet.add(id)
        outputFile.write(ET.tostring(elem, encoding="unicode"))
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
    global progress

    parser = argparse.ArgumentParser(prog='Stack Overflow Questions Filter')

    parser.add_argument('file', type=existingFile, help='StackOverflow Posts.xml file')
    parser.add_argument('output', type=creatableFile, help='StackOverflow Posts.xml file')
    parser.add_argument('--title', type=str, help='Filter questions by title containing the term')
    parser.add_argument('--tag', type=str, help='Filter by tag containing the term')
    parser.add_argument('--in-memory', action='store_true', help='Execute the filtering in memory [Default=FALSE].')
    # parser.add_argument('--progress-step', help='The amount of questions to be inspected before every report.')

    args = parser.parse_args()

    print('Filtering questions from the file %s ' % args.file)

    print('Filtering Criteria')
    if args.title:
        print('\tQuestion Title contains: %s' % args.title)

    if args.tag:
        print('\tQuestion contains Tag: %s' % args.title)

    # if args.progress_step:
    #     progress = args.progress_step

    if args.in_memory:
        raise NotImplementedError('Functionality not yet implemented')




    filter_questions(args.file, args.output, args.title, args.tag)
