from flask import Flask, request, jsonify, render_template
from chatbot import get_bot_response
import os

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('a.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "")
        if not user_input:
            return jsonify({"reply": "Please provide a message."})
        response = get_bot_response(user_input)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add this at the end
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
else:
    # For Vercel deployment
    application = app