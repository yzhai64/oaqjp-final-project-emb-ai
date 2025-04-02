import requests
import json  # ✅ 用于格式化处理响应数据

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = json.loads(response.text)  # ✅ 将响应文本转换为 dict

        try:
            emotions = result["emotionPredictions"][0]["emotion"]
            # ✅ 提取各项得分
            anger = emotions["anger"]
            disgust = emotions["disgust"]
            fear = emotions["fear"]
            joy = emotions["joy"]
            sadness = emotions["sadness"]

            # ✅ 找出主导情绪
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        except Exception as e:
            return {"error": "Unexpected response structure", "details": str(e)}
    else:
        return {"error": response.status_code, "message": response.text}