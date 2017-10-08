from __future__ import absolute_import, unicode_literals
from .celery import app
import os, json, jsonlines
from flask import jsonify

rootDir = '.'    
mydict = {'han': 0, 'hon': 0, 'den': 0, 'det': 0, 'denna': 0, 'denne': 0, 'hen':0}    
    
@app.task     
def tweets() :    
    count = 0    
    for dirName, subdirList, fileList in os.walk(rootDir):    
        if dirName == './data' :    
            print ('counting frequency of pronouns .. in progress!!')    
            for fname in fileList :    
                with jsonlines.open(dirName + '/' + fname) as reader:    
                    for obj in reader.iter(type=dict,skip_empty=True):    
                        count = count + 1    
                        if 'retweeted_status' in obj.keys() :    
                            if (obj['retweeted_status']) == None and (obj['retweeted']) == False :    
                                for elements in mydict :    
                                    lowertweet = obj['text'].lower()    
                                    for elements in mydict :    
                                        if elements in lowertweet :    
                                            mydict[elements] += 1    
                        elif 'retweeted_status'  not in obj.keys() :    
                            lowertweet = obj['text'].lower()    
                            for elements in mydict :    
                                if elements in lowertweet :    
                                    mydict[elements] += 1    
    
    return json.JSONEncoder().encode(mydict)    

