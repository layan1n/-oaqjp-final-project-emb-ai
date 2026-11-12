
"""Unit tests for emotion detection."""

import unittest
from unittest.mock import patch
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detection results."""

    def check_emotion(self, expected):
        scores = {
            emotion: 0.1
            for emotion in (
                "anger", "disgust", "fear", "joy", "sadness"
            )
        }
        scores[expected] = 0.9

        with patch(
            "EmotionDetection.emotion_detection.requests.post"
        ) as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {
                "emotionPredictions": [{"emotion": scores}]
            }

            result = emotion_detector("Test sentence")
            self.assertEqual(result["dominant_emotion"], expected)

    def test_anger(self):
        self.check_emotion("anger")

    def test_disgust(self):
        self.check_emotion("disgust")

    def test_fear(self):
        self.check_emotion("fear")

    def test_joy(self):
        self.check_emotion("joy")

    def test_sadness(self):
        self.check_emotion("sadness")


if __name__ == "__main__":
    unittest.main()
