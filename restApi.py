from flask import Flask, request, jsonify 
import json 
import os
import pandas as pd

app = Flask(__name__) 
port = '80' 
dataframe = pd.read_csv('/tmp/downloaded.csv')

@app.route('/', methods=['POST']) 
def index(): 
  data = json.loads(request.get_data())
  input = data['nlp']['source']
  result = test1(input)
  return jsonify( 
    status=200, 
    replies=[{ 
      'type': 'text', 
      'content': result, 
    }]
  ) 

@app.route('/errors', methods=['POST']) 
def errors(): 
  print(json.loads(request.get_data())) 
  return jsonify(status=200) 


stringExample = 'instance vcpu for r4.large storage'


instances= dataframe['Instance Type'].tolist()
#print(instances)
columnHeadings = dataframe.columns.values.tolist()
#print(columnHeadings)
columnHeadings = [x.lower() for x in columnHeadings]

def test1(input):
  
  instancePresent = ''
  columnHeadingsPresent = ''
  result = 'please include more information'
  
  for instance in instances:
    if instance in input:
      instancePresent = instance
  
  for column in columnHeadings:
    if column in input:
      columnHeadingsPresent = column.title()
      if columnHeadingsPresent in 'Vcpu':
        columnHeadingsPresent = 'vCPU'
      
  if instancePresent and columnHeadingsPresent:
    #print('instancePresent and columnHeadings are equal to true')
    indexInstance = instances.index(instancePresent)
    dataValue = dataframe.iloc[indexInstance][columnHeadingsPresent]
    return 'Instance type: ' + instancePresent + ', ' + columnHeadingsPresent + ': ' + str(dataValue)
    #get corresponding value of column value and store it
    
  return result
  

def test3(input):
  selectedPhrase= ''
  triggerPhraseDict = { 'compute':['c5', 'c4'], 'memory':['x1', 'r5', 'r4', 'z1d'], 'accelerated':['p3','p2','g3','f1'], 'general':['t3','t2','m5','m4'],'storage':['h1','i3','d2'] } 
  triggerPhrases = triggerPhraseDict.keys()
  result = []
  for phrase in triggerPhrases:
    if phrase in input:
      selectedPhrase = phrase
      for instance in instances:
          for keyInstance in triggerPhraseDict[selectedPhrase]:
            if keyInstance in instance:
              result.append(instance)
      
  result = list(set(result))
  stringResult = ''
  
  for item in result:
    stringResult += item
    stringResult += ', '
  #print(result)
  print(stringResult)
  
def findResult(input):
  print('no')

#variable = test1(stringExample)
#print(variable)
test3(stringExample)

#print(instances)
#test2()
#app.run(port=port)

