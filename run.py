from flask import Flask
from flask import request
import jsonschema
from jsonschema import validate
# import json


app = Flask(__name__)

def getResult_string(animal,sound,count,delimeter):
    result_String = ""
    i = 0
    while i < int(count):
        result_String += animal + " says " + sound + delimeter
        i += 1
    return result_String

@app.route('/hello', methods = ['GET'])
def get_method():
    animal = request.args.get('animal')
    sound = request.args.get('sound')
    count = request.args.get('count')
    result_string=getResult_string(animal,sound,count,'<br>')
    return result_string

reqSchema = {
    "type": "object",
    "properties": {
        "animal": {"type": "string"},
        "sound": {"type": "string"},
        "count": {"type": "number"},
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=reqSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

@app.route('/', methods = ['POST'])
def post_method():
    jsonData = request.get_json(force = True)
    isValid = validateJson(jsonData)
    if isValid:
        animal = jsonData['animal']
        sound = jsonData['sound']
        count = jsonData['count']
        result_string = getResult_string(animal,sound,count,'\n')
        return result_string
    else:
        return "not valid"
