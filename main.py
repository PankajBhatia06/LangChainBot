from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
  
@app.route('/handleget', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)
  
@app.route('/handlepost', methods=['POST'])
def handle_post():
    if (request.method == 'POST'):
        textData = request.form['testData']
        data = {"response" : textData}
        return jsonify(data)
  
if __name__ == '__main__':
    app.run(port=3445)