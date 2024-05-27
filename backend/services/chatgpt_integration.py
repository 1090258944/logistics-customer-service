import openai
from flask import Blueprint, request, jsonify

chatgpt_blueprint = Blueprint('chatgpt', __name__)

@chatgpt_blueprint.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    
    # 调用 ChatGPT API 进行处理
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=query,
        max_tokens=150
    )
    
    return jsonify(response.choices[0].text)
