from  flask import Flask, jsonify
from proj.tasks import tweets
from flask import Flask, jsonify

myapp = Flask(__name__)
@myapp.route('/tweets/api/v1.0/frequencies', methods=['GET'])
def getresults():
    result = tweets.delay()
    #cant return the result directly because its an asynchronous call
    while result.ready == False :
        print ('calculating the frequency of pronouns, keep patience')
    return result.get()

if __name__ == '__main__':
    myapp.run(host='0.0.0.0',debug=True)

