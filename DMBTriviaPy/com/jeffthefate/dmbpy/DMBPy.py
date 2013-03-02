'''
Created on Oct 7, 2012

@author: Jeff
'''

import json, httplib, csv, re, sys

def fix_string(string):
    string = repr(string)
    while '\\x' in string:
        index = string.index('\\')
        string = string[:index] + string[index+4:]
        print string
    return eval(string)
        
def add_question(category, question, answer):
    category = fix_string(category)
    question = fix_string(question)
    answer = fix_string(answer)
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/Question', json.dumps({
           "category": category, "question": question, "answer": answer
         }), {
           "X-Parse-Application-Id": "ImI8mt1EM3NhZNRqYZOyQpNSwlfsswW73mHsZV3R",
           "X-Parse-REST-API-Key": "1smRSlfAvbFg4AsDxat1yZ3xknHQbyhzZ4msAi5w",
           "Content-Type": "application/json"
         })
    '''
    connection.request('POST', '/1/classes/Question', json.dumps({
           "category": category, "question": question, "answer": answer
         }), {
           "X-Parse-Application-Id": "6pJz1oVHAwZ7tfOuvHfQCRz6AVKZzg1itFVfzx2q",
           "X-Parse-REST-API-Key": "uNZMDvDSahtRxZVRwpUVwzAG9JdLzx4cbYnhYPi7",
           "Content-Type": "application/json"
         })
    '''
    result = json.loads(connection.getresponse().read())
    print result

def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator,
                           skipinitialspace=True):
        if line:
            yield line
    
def test():
    fileLoc = raw_input("Enter the file location and name: ")
    try:
        for data in import_text(fileLoc, "\n"):
            if '|' in data[0]:
                print(data)
                pattern = re.compile(r"\|")
                datalist = pattern.split(data[0])
                count = 0
                entrylist = ["", "", "", "", "", "", "", ""]
                for data in datalist:
                    entrylist[count] = data
                    count = count + 1
                add_question(entrylist[0], entrylist[1], entrylist[2])
    except:
        print "Error! Check the file location"
        pass
    raw_input("Press any key to finish")

test()