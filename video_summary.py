# video_summary.py
from pytube import YouTube
import ffmpeg

def download_video(url, save_path="video.mp4"):
    """
    Downloads the YouTube video at the given URL.
    Returns the path to the downloaded file.
    """
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()
    stream.download(filename=save_path)
    return save_path

def get_video_duration(video_path="video.mp4"):
    """
    Returns the video duration in seconds using ffmpeg.
    """
    try:
        probe = ffmpeg.probe(video_path)
        duration = float(probe['format']['duration'])
        return duration
    except Exception as e:
        print("Error getting video duration:", e)
        return None

def summarize_video(video_path="video.mp4"):
    """
    Placeholder for video summary logic.
    Currently returns basic info like filename and duration.
    """
    duration = get_video_duration(video_path)
    summary_text = f"Video: {video_path}\nDuration: {duration:.2f} seconds" if duration else "Could not read video duration."
    return summary_text
