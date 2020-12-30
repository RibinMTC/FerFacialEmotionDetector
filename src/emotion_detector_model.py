from fer import FER
import cv2
import pprint
import tensorflow as tf
import operator

from flask import jsonify


class EmotionDetector:
    """
    Main class which predicts facial emotions for a given image.
        1. Predicts one of the cardinal emotions (fear, anger, surprise, neutral, disgust, sad), if faces were detected.
        2. Predicts none if no face or emotion was detected.
    This class is utilized by the aesthetics_predictor_api_pk, which delegates flask requests to the predict method and
    sends the response back to the client.
    """
    def __init__(self):
        self.session = tf.compat.v1.Session()

        with self.session.as_default():
            with self.session.graph.as_default():
                self.detector = FER(mtcnn=True)

    def predict(self, content_path, start_frame=0, end_frame=0):
        try:
            with self.session.as_default():
                with self.session.graph.as_default():
                    image = cv2.imread(content_path)
                    results = self.detector.detect_emotions(image)
                    pprint.pprint(results)
                    parsed_output = self.parse_output(results)
                    return jsonify(parsed_output)
        except Exception as e:
            print(str(e))
            return None

    def parse_output(self, results):
        facial_emotion_key = "facialEmotions"
        if results is None or len(results) == 0:
            return {facial_emotion_key: "none"}
        facial_emotions = []
        for result in results:
            dominant_emotion = max(result["emotions"].items(), key=operator.itemgetter(1))[0]
            facial_emotions.append(dominant_emotion)
        distinct_facial_emotions = list(set(facial_emotions))
        return {facial_emotion_key: distinct_facial_emotions}
