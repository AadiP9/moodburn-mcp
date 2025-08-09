from flask import Flask, request, jsonify, render_template  # Explicitly import render_template
from dotenv import load_dotenv
import os
import openai
import json
from prompts import PROMPTS
import utils

app = Flask(__name__)
load_dotenv()

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/process', methods=['POST'])
def process_request():
    data = request.get_json()
    task = data.get('task')
    text = data.get('text')
    
    if not task or not text:
        return jsonify({"error": "Missing 'task' or 'text' in request"}), 400
    
    handler = {
        'mood': handle_mood,
        'study_plan': handle_study_plan,
        'flashcards': handle_flashcards,
        'quiz': handle_quiz,
        'summary': handle_summary,
        'todo': handle_todo,
        'shuffle_tasks': handle_shuffle_tasks
    }.get(task)
    
    if not handler:
        return jsonify({"error": f"Unknown task: {task}"}), 400
    
    return handler(text)

def handle_mood(text):
    prompt = PROMPTS['mood'].format(statement=text)
    response = utils.call_openai(prompt)
    return jsonify(response)

def handle_study_plan(text):
    prompt = PROMPTS['study_plan'].format(syllabus=text)
    response = utils.call_openai(prompt)
    return jsonify(response)

def handle_flashcards(text):
    prompt = PROMPTS['flashcards'].format(notes=text)
    response = utils.call_openai(prompt)
    return jsonify(response)

def handle_quiz(text):
    prompt = PROMPTS['quiz'].format(content=text)
    response = utils.call_openai(prompt)
    return jsonify(response)

def handle_summary(text):
    prompt = PROMPTS['summary'].format(notes=text)
    response = utils.call_openai(prompt)
    return jsonify({"summary": response})

def handle_todo(text):
    prompt = PROMPTS['todo'].format(task=text)
    response = utils.call_openai(prompt)
    return jsonify(response)

def handle_shuffle_tasks(text):
    try:
        data = json.loads(text)
        tasks = data['tasks']
        mood_index = data['mood_index']
    except (json.JSONDecodeError, KeyError):
        return jsonify({"error": "Invalid input format"}), 400
    
    prompt = PROMPTS['shuffle_tasks'].format(
        tasks="\n".join([f"- {task}" for task in tasks]),
        mood_index=mood_index
    )
    response = utils.call_openai(prompt)
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')  # Now properly imported

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
