from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)  # 默认从 templates/ 和 static/ 提取文件

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])  # ✅ 注意路径名要求
def analyze_emotion():
    text = request.form['text']
    result = emotion_detector(text)

    if 'error' in result:
        return f"Error occurred: {result['error']}"

    # ✅ 格式化输出结果
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