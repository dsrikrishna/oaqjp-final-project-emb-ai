from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route ("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyze = request.args.get("textToAnalyze")
    emotion_response = emotion_detector(text_to_analyze)
    return (f"For the given statement, the system response is 'anger': {emotion_response['anger']},"
    f" 'disgust': {emotion_response['disgust']}, 'fear':{emotion_response['fear']},"
    f" 'joy': {emotion_response['joy']} and 'sadness': {emotion_response['sadness']}."
    f" The dominant emotion is <b>{emotion_response['dominant_emotion']}</b>.")
    
@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="localhost",port=5000)