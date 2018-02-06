import argparse
import os
import time
from datetime import timedelta
import xml.etree.ElementTree as etree

# Report Variables

class Report:
    """
    Class to report the progress of the filter operation
    """

    def __init__(self):
        self.qInspected = 0
        self.qFound = 0
        self.aFound = 0
        self.startTime = time.time()
        self.nErrors = 0
        self.progressStep = 100000  # default
        self.errorList = []

    def questionInspected(self):
        self.qInspected += 1

    def questionFound(self):
        self.qFound += 1

    def answerFound(self):
        self.aFound += 1

    def errorFound(self, msg):
        self.nErrors += 1
        self.errorList.append(msg)

    def reportProgress(self):
        if self.qInspected % self.progressStep == 0:
            elapsed = time.time() - self.startTime
            print("# inspected = %d | # of questions %d | # of answers %d | Time elapsed %s" %
                  (self.qInspected, self.qFound, self.aFound, timedelta(seconds=elapsed)), flush=True)


# Global
questionsIdsSet = set()
report = Report()


def isQuestion(elem):
    return elem.get("PostTypeId") == '1'


def filter_post(file, output, title, tag):
    global report

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
            # Clean the memory
            elem.clear()
            root.clear()
            # Report progress
            report.reportProgress()

        outputFile.write("\n</posts>")


def writeToOutput(elem, outputFile):
    global report
    try:
        outputFile.write(etree.tostring(elem, encoding="unicode"))

    except UnicodeEncodeError:
        # print("Error on processing element ")
        id = elem.get("Id")
        report.errorFound('Unicode Error while processing the elem with Id = %s' %
                          id)
        # ignore for now
        pass


def inspectAnswer(elem, outputFile):
    global report

    questionId = elem.get("ParentId")

    # Add answers to the already inspected question
    if questionId in questionsIdsSet:
        report.answerFound()
        writeToOutput(elem, outputFile)


def inspectQuestion(elem, outputFile, tag, title):
    global report

    report.questionInspected()

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
        report.questionFound()
        writeToOutput(elem, outputFile)


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
        report.progressStep = int(args.progress_step)

    if args.in_memory:
        raise NotImplementedError('Functionality not yet implemented')

    filter_post(args.file, args.output, title, tag)

    print('Process Finished')
    print('\t # of Questions Inspected = %d' % report.qInspected)
    print('\t # of Questions Found = %d' % report.qFound)
    print('\t # of Answers Found = %d' % report.aFound)
    print('\t # of Errors = %d' % report.nErrors)
    print('\n'.join(report.errorList))
