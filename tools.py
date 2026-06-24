


from langchain.tools import tool
from youtube_transcript_api import YouTubeTranscriptApi
import re


@tool
def youtube_transcript(video_url: str) -> str:
    """
    Extract transcript from a YouTube video URL.

    Input:
        Full YouTube URL

    Returns:
        Video transcript text.
    """

    try:

        # Extract video ID

        patterns = [
            r"v=([a-zA-Z0-9_-]+)",
            r"youtu\.be/([a-zA-Z0-9_-]+)"
        ]

        video_id = None

        for pattern in patterns:
            match = re.search(pattern, video_url)

            if match:
                video_id = match.group(1)
                break

        if not video_id:
            return "Could not extract YouTube video ID."

        transcript = YouTubeTranscriptApi.get_transcript(
            video_id
        )

        text = " ".join(
            chunk["text"]
            for chunk in transcript
        )

        return text[:10000]

    except Exception as e:
        return f"Transcript error: {str(e)}"
    


def multiply(a:int, b:int)->int:
    """use this tool when you have to calculate something"""
    return a*b