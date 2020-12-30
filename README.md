## FerFacialEmotionDetector

FerFacialEmotionDetector is a python tool to predict facial emotions for the aesthetic assessment project. The project utilizes the [Facial Expression Recognition](https://github.com/justinshenk/fer) implementation.


1. The predictor uses Flask (by default listening on *localhost:5007*) to listen to incoming requests, which should contain the path to the image to detect facial emotions.
2. The predictor returns one of the following emotions : *fear, anger, surprise, neutral, disgust, sad* if a face was detected and *none* otherwise.

### Requirements

This project requires Python 3.

### Installation

Clone this repository and install the project requirements:

```bash
pip install -r requirements.txt
```
 
### Usage

The recommended usage is with a docker-compose file.

For testing the code without using Flask, run the following code:

```python
from src.emotion_detector_model import EmotionDetector
fer_emotion_detector = EmotionDetector()
fer_emotion_detector.predict("path/to/image")
```

To start the Flask Api, which listens for incoming prediction requests run:

```bash
gunicorn --config gunicorn_config.py --env API_CONFIG=api_config.json aesthetics_predictor_api_pkg.predictor_api_server:app
```