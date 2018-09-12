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


stringExample = 'instance memory for r4.large processor architecture'
instances= dataframe['Instance Type'].tolist()
twoWordHeadings = ['operating system', 'processor architecture', 'network performance']
#print(instances)
columnHeadings = dataframe.columns.values.tolist()
#print(columnHeadings)
columnHeadings = [x.lower() for x in columnHeadings]

def test1(input):
  split = input.split(' ')
  
  instancePresent = ''
  columnHeadingsPresent = ''
  result = 'please include more information'
  
  for instance in instances:
    if instance in split:
      instancePresent = instance
  
  for column in columnHeadings:
    if column in split:
      columnHeadingsPresent = column.title()
      
  for heading in twoWordHeadings:
    if heading in input:
      columnHeadingsPresent = heading.title()
  
  if instancePresent and columnHeadingsPresent:
    #print('instancePresent and columnHeadings are equal to true')
    indexInstance = instances.index(instancePresent)
    dataValue = dataframe.iloc[indexInstance][columnHeadingsPresent]
    return 'Instance type: ' + instancePresent + ', ' + columnHeadingsPresent + ': ' + str(dataValue)
    #get corresponding value of column value and store it
    
  return result
  
def test2():
  print(dataframe['Instance Type'].tolist())
  #exampleList = dataframe.columns.values.tolist()
  #return instance name + column value

variable = test1(stringExample)
print(variable)
#print(instances)
#test2()
#app.run(port=port)

