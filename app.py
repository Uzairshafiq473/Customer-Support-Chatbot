from flask import Flask, request, jsonify, render_template
from chatbot import get_bot_response

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('a.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"reply": "Please provide a message."})
    response = get_bot_response(user_input)
    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))