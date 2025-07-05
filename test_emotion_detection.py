import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_sentiment_analyzer(self):
        test_cases_dict = {"I am glad this happened":"joy",
                          "I am really mad about this":"anger",
                          "I feel disgusted just hearing about this":"disgust",
                          "I am so sad about this":"sadness",
                          "I am really afraid that this will happen":"fear"}
        
        for statement, expected_dominant_emotion in test_cases_dict.items():
            self.assertEqual(emotion_detector(statement)['dominant_emotion'],expected_dominant_emotion)
if __name__=="__main__":
    unittest.main()