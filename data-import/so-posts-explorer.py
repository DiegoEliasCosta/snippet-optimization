import pandas as pd
import xml.etree.ElementTree as etree
import os
from bs4 import BeautifulSoup


def xml2df(xml_data):
    root = etree.XML(xml_data) # element tree
    all_records = []
    for i, child in enumerate(root):
        all_records.append(child.attrib)
    return pd.DataFrame(all_records)


def extractCode(body):
    """
    Use the tag <code> to extract the code from the post body
    """
    soup = BeautifulSoup(body, 'lxml')
    return soup.find_all('code')


if __name__ == '__main__':

    dir = os.path.join('..', 'data')
    file = os.path.join(dir, 'pt-stackoverflow-pandas-posts.xml')
    file = os.path.join(dir, 'filtered-pandas-post.xml')

    output_file = os.path.join(dir, 'pt-stackoverflow-pandas-posts.csv')
    output_file = os.path.join(dir, 'filtered-pandas-post.csv')

    xml_data = open(file, encoding='utf-8').read()

    df = xml2df(xml_data)
    df.to_csv(output_file, sep=',', )

    questions = df[df.PostTypeId == '1']
    answers = df[df.PostTypeId == '2']

    top_questions = questions.sort_values(by='Score', ascending=False)[:10]

    ids = top_questions.Id
    # TODO Fix the Ids
    answers_top_questions = answers[answers.ParentId in ids]

    top_df = top_questions.concat(answers_top_questions)
    print(top_df.Title)



    #df.codes = df.Body.apply(extractCode)

    #print(df.codes)

    # most_aswered = df.sort_values(by='AnswerCount', ascending=False)
    # print(most_aswered[['Title', 'AnswerCount']])





