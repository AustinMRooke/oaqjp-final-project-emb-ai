"""Server file for the Emotion Detection System"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the text in an emotion detector"""

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)


    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']
    dominant_emotion=response['dominant_emotion']

    if anger is None:
        return "Invalid Text! Please try again!"

    return_text = f"For the given statement, the system response is 'anger':{anger},"
    return_text += f" 'disgust':{disgust}, 'fear':{fear}, 'joy':{joy}, and 'sadness':{sadness}."
    return_text += f"The dominant emotion is {dominant_emotion}."

    return return_text

@app.route("/")
def render_index_page():
    """Show index page upon visit"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
