# Final Project

Emotion Detector using IBM Watson NLP.

Repository for final project

This project detects five emotions (anger, disgust, fear, joy, and sadness) in text and identifies the dominant emotion. It includes a Flask web interface, error handling for blank input, and unit tests.

## Files
- `EmotionDetection/emotion_detection.py`: Emotion detection function
- `EmotionDetection/__init__.py`: Package exports
- `server.py`: Flask application
- `templates/index.html`: Web interface
- `test_emotion_detection.py`: Unit tests

## Run
Install `flask` and `requests`, then run `python3 server.py`.

## Tests and static analysis
Run `python3 -m unittest -v test_emotion_detection.py` for unit tests.
Install `pylint` and run `python3 -m pylint server.py` to produce the static-analysis output.
