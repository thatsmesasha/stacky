from flask import Flask, request, jsonify
from engine import answer
import os
from jsonschema import validate

app = Flask(__name__)
port = os.environ['STACKY_API_PORT']

@app.route('/process', methods=['POST'])
def process():
    content = request.get_json(force=True)
    print('Received: {}'.format(content))

    schema = {
        'type' : 'object',
        'properties': {
            'question': {
                'type': 'string'
            }
        },
        'additionalProperties': False,
    }
    try:
        validate(content, schema)
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return jsonify({ 'error': 'invalid format' }), 422

    response = answer(content['question'])
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=port, host='0.0.0.0')
