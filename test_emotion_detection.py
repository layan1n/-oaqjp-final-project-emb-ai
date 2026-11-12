"""Unit tests for emotion detection."""

import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detection results."""

    def check_emotion(self, expected):
        """Check the dominant emotion."""
        scores = {
            emotion: 0.1
            for emotion in ("anger", "disgust", "fear", "joy", "sadness")
        }
        scores[expected] = 0.9

        with patch("EmotionDetection.emotion_detection.requests.post") as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {
                "emotionPredictions": [{"emotion": scores}]
            }
            result = emotion_detector("Test sentence")
            self.assertEqual(result["dominant_emotion"], expected)

    def test_anger(self):
        """Test anger."""
        self.check_emotion("anger")

    def test_disgust(self):
        """Test disgust."""
        self.check_emotion("disgust")

    def test_fear(self):
        """Test fear."""
        self.check_emotion("fear")

    def test_joy(self):
        """Test joy."""
        self.check_emotion("joy")

    def test_sadness(self):
        """Test sadness."""
        self.check_emotion("sadness")

    def test_blank(self):
        """Test blank input."""
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
