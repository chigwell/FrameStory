[![PyPI version](https://badge.fury.io/py/FrameStory.svg)](https://badge.fury.io/py/frame_story)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/FrameStory)](https://pepy.tech/project/frame_story)

# Frame Story

`FrameStory` is a Python package designed for extracting and describing significant frames from videos. Leveraging state-of-the-art machine learning models, it can provide detailed descriptions of video content, making it a powerful tool for content analysis, accessibility, and summarization.

## Installation

To install `FrameStory`, you can use pip:

```bash
pip install FrameStory
```

## Usage

Using `FrameStory` is straightforward. Below are examples demonstrating how to extract and describe significant frames from videos with various parameters.

### Describing Video by URL

```python
from frame_story.video_describer import VideoDescriber

video_url = "https://example.com/video.mp4"
describer = VideoDescriber(show_progress=True)
descriptions = describer.get_video_descriptions(video_url=video_url)
print(descriptions)
```

### Describing Video from Local Path

```python
video_path = "/path/to/your/video.mp4"
describer = VideoDescriber(show_progress=True, max_tokens=50)
descriptions = describer.get_video_descriptions(video_path=video_path)
print(descriptions)
```

### Customizing Extraction Threshold

The `extract_significant_frames` method allows you to customize the threshold for what constitutes a "significant" change between frames.

```python
video_url = "https://example.com/video.mp4"
describer = VideoDescriber(threshold=25000)
descriptions = describer.get_video_descriptions(video_url=video_url)
print(descriptions)
```

These examples demonstrate the versatility of `frame_story` in processing videos from different sources and with various levels of detail in descriptions.

## Features

- Extraction of significant frames from videos for detailed analysis.
- Generation of descriptive text for each significant frame using state-of-the-art image captioning models.
- Support for videos from URLs or local file paths.
- Customizable settings for progress display, description length, and frame extraction threshold.
- Easy to integrate into Python projects for content analysis, summarization, and accessibility applications.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/frame_story/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
