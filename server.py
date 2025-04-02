"""
Flask Web Application for Emotion Detection.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the main page with input form.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def analyze_emotion():
    """
    Handle POST request, analyze emotion, and return formatted result.
    """
    text = request.form['text']
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)