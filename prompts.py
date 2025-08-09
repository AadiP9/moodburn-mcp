PROMPTS = {
    'mood': (
        "Analyze the student's mood from their statement on a scale of 0-10 "
        "(0=lowest, 10=highest). Provide JSON output with keys 'mood_index' (int) "
        "and 'roast' (a funny, savage but safe one-liner).\n\n"
        "Statement: {statement}\n\n"
        "Example: {{\"mood_index\": 2, \"roast\": \"You're moving slower than a sloth on sleeping pills!\"}}"
    ),
    
    'study_plan': (
        "Create a detailed study plan from syllabus information. "
        "Output JSON with 'plan' (list of daily tasks), 'duration' (in weeks), "
        "and 'key_dates' (list of important dates).\n\n"
        "Syllabus: {syllabus}\n\n"
        "Structure: {{\"plan\": [\"Day 1: Topic A\", \"Day 2: Topic B\"], "
        "\"duration\": 4, \"key_dates\": [\"2023-09-10: Midterm\"]}}"
    ),
    
    'flashcards': (
        "Generate flashcards from academic notes. Output JSON with a list of flashcards "
        "where each has 'term' and 'definition'.\n\n"
        "Notes: {notes}\n\n"
        "Example: {{\"flashcards\": [{{\"term\": \"Photosynthesis\", \"definition\": \"Process where plants convert light to energy\"}}]}}"
    ),
    
    'quiz': (
        "Create a multiple-choice quiz with 5 questions. For each question, include "
        "4 options and mark the correct answer. Output JSON with 'questions' (list) "
        "each containing 'question', 'options' (list), and 'answer' (letter A-D).\n\n"
        "Content: {content}\n\n"
        "Example: {{\"questions\": [{{\"question\": \"What is 2+2?\", \"options\": [\"3\", \"4\", \"5\", \"6\"], \"answer\": \"B\"}}]}}"
    ),
    
    'summary': (
        "Summarize academic content into concise bullet points. "
        "Return just the summary text (no JSON).\n\n"
        "Notes: {notes}\n\n"
        "Example: \"- Key point 1\n- Key point 2\""
    ),
    
    'todo': (
        "Break down a large task into smaller, timed subtasks. "
        "Output JSON with 'subtasks' (list) each containing 'task' and 'time_estimate' (minutes).\n\n"
        "Task: {task}\n\n"
        "Example: {{\"subtasks\": [{{\"task\": \"Research phase\", \"time_estimate\": 60}}, {{\"task\": \"Outline structure\", \"time_estimate\": 30}}]}}"
    ),
    
    'shuffle_tasks': (
        "Reorder tasks based on mood index (0-10). Low mood (0-3): prioritize quick wins. "
        "Medium (4-6): mix quick and important. High (7-10): prioritize challenging tasks. "
        "Output JSON with 'tasks' (reordered list) and 'explanation' (brief reason).\n\n"
        "Tasks:\n{tasks}\nMood Index: {mood_index}\n\n"
        "Example: {{\"tasks\": [\"Quick task\", \"Medium task\", \"Hard task\"], \"explanation\": \"Prioritized quick wins for low mood\"}}"
    )
}
