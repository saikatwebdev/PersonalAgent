from langchain.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi
import re


@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b


@tool
def youtube_transcript(video_url: str) -> str:
    """
    Extract transcript from a YouTube video URL.
    """

    try:
        patterns = [
            r"v=([a-zA-Z0-9_-]+)",
            r"youtu\.be/([a-zA-Z0-9_-]+)"
        ]

        video_id = None

        for pattern in patterns:
            match = re.search(
                pattern,
                video_url
            )

            if match:
                video_id = match.group(1)
                break

        if not video_id:
            return "Could not determine video ID."

        transcript = (
            YouTubeTranscriptApi.get_transcript(
                video_id
            )
        )

        text = " ".join(
            chunk["text"]
            for chunk in transcript
        )

        return text[:10000]

    except Exception as e:
        return f"Transcript extraction failed: {str(e)}"

