from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return "CTF Challenge Solution API is running!"

@app.route('/list/<challenge>', methods=['GET'])
def list_scripts(challenge):
    challenge_path = os.path.join(BASE_DIR, challenge)
    if not os.path.isdir(challenge_path):
        return jsonify({"error": f"Challenge '{challenge}' not found"}), 404
 
    scripts = [f[:-3] for f in os.listdir(challenge_path) if f.endswith('.py')]
    return jsonify({"challenge": challenge, "scripts": scripts})

@app.route('/run/<challenge>/<script_name>', methods=['GET'])
def run_script(challenge, script_name):
    challenge_path = os.path.join(BASE_DIR, challenge)
    if not os.path.isdir(challenge_path):
        return jsonify({"error": f"Challenge '{challenge}' not found"}), 404

    script_file = os.path.join(challenge_path, f"{script_name}.py")
    if not os.path.isfile(script_file):
        return jsonify({"error": f"Script '{script_name}.py' not found in '{challenge}'"}), 404

    try:
        result = subprocess.run(
            ["python", script_file],
            capture_output=True, text=True, check=True
        )
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.stderr}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
