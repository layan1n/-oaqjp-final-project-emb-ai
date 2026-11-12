
"""Emotion detection using IBM Watson NLP."""

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
    "emotion_aggregated-workflow_lang_en_stock"
}


def emotion_detector(text_to_analyze):
    """Detect emotions in the given text."""
    emotions = ("anger", "disgust", "fear", "joy", "sadness")

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return {
            **{emotion: None for emotion in emotions},
            "dominant_emotion": None
        }

    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers=HEADERS,
        timeout=20
    )

    if response.status_code == 400:
        return {
            **{emotion: None for emotion in emotions},
            "dominant_emotion": None
        }

    response.raise_for_status()

    scores = response.json()["emotionPredictions"][0]["emotion"]

    result = {
        emotion: scores[emotion]
        for emotion in emotions
    }

    result["dominant_emotion"] = max(
        emotions,
        key=result.get
    )

    return result
