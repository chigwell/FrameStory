import os
import unittest
from unittest.mock import patch
from frame_story.video_describer import VideoDescriber


class TestVideoDescriber(unittest.TestCase):
    def setUp(self):
        self.model_name = "Salesforce/blip-image-captioning-large"
        self.video_describer = VideoDescriber(model_name=self.model_name, show_progress=False)

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    @patch("os.makedirs")
    @patch("requests.get")
    def test_download_video(self, mock_get, mock_makedirs, mock_open):
        mock_get.return_value.content = b"video data"
        video_url = "http://example.com/video.mp4"
        save_path = "videos/video.mp4"
        self.video_describer.download_video(video_url, save_path)
        mock_get.assert_called_once_with(video_url)
        mock_makedirs.assert_called_once_with(os.path.dirname(save_path), exist_ok=True)
        mock_open.assert_called_once_with(save_path, 'wb')
        mock_open().write.assert_called_once_with(b"video data")

    @patch("frame_story.video_describer.VideoDescriber.download_video")
    @patch("frame_story.video_describer.VideoDescriber.extract_significant_frames")
    @patch("frame_story.video_describer.VideoDescriber.describe_frames")
    def test_get_video_descriptions(self, mock_describe, mock_extract, mock_download):
        mock_describe.return_value = []
        mock_extract.return_value = ([], [])
        video_url = "http://example.com/video.mp4"
        descriptions = self.video_describer.get_video_descriptions(video_url=video_url)
        mock_download.assert_called_once_with(video_url, 'tmp/temp_video.mp4')
        mock_extract.assert_called_once()
        mock_describe.assert_called_once()
        self.assertEqual(descriptions, [])


if __name__ == "__main__":
    unittest.main()