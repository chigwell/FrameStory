import requests
import cv2
import os
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from tqdm import tqdm


IMAGE_CAPTIONING_MODEL = "Salesforce/blip-image-captioning-large"


class VideoDescriber:
    def __init__(self, model_name=IMAGE_CAPTIONING_MODEL, show_progress=True, max_tokens=100, temp_dir='tmp', threshold=50000):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        self.show_progress = show_progress
        self.max_tokens = max_tokens
        self.temp_dir = temp_dir
        self.threshold = threshold

    def download_video(self, video_url, save_path):
        video_content = requests.get(video_url).content
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as video_file:
            video_file.write(video_content)

    def extract_significant_frames(self, video_path, threshold=50000):
        cap = cv2.VideoCapture(video_path)
        frames = []
        times = []
        last_frame = None
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_iter = tqdm(range(total_frames), "Extracting frames") if self.show_progress else range(total_frames)
        for _ in frame_iter:
            success, frame = cap.read()
            if not success:
                break
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if last_frame is not None:
                diff = cv2.absdiff(last_frame, gray_frame)
                non_zero_count = np.count_nonzero(diff)
                if non_zero_count > threshold:
                    frames.append(frame)
                    times.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0)
            last_frame = gray_frame
        cap.release()
        return frames, times

    def describe_frames(self, frames, times):
        descriptions = []
        previous_desc = ""
        for i, (frame, time) in enumerate(zip(frames, times)):
            if i + 1 < len(times):
                duration = times[i + 1] - time
            raw_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).convert('RGB')
            inputs = self.processor(raw_image, return_tensors="pt")
            out = self.model.generate(**inputs, max_new_tokens=self.max_tokens)
            description = self.processor.decode(out[0], skip_special_tokens=True)
            if description != previous_desc:
                descriptions.append({"start": time, "duration": duration, "description": description})
                previous_desc = description
                if self.show_progress:
                    print({"start": time, "dur": duration, "desc": description})
        return descriptions

    def get_video_descriptions(self, video_path=None, video_url=None):
        if video_url:
            video_path = os.path.join(self.temp_dir, 'temp_video.mp4')
            self.download_video(video_url, video_path)
        frames, times = self.extract_significant_frames(video_path, self.threshold)
        descriptions = self.describe_frames(frames, times)
        return descriptions

# Example usage
# if __name__ == '__main__':
#     video_url = 'https://cdn.vidwidget.ru/storage/videos/0d26ed03-2085-4977-92ce-930c5980173d.mp4'
#     describer = VideoDescriber()
#     descriptions = describer.get_video_descriptions(video_url=video_url)
#     print(descriptions)



