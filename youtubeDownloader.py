"""
YouTube Downloader

A script to download YouTube videos or playlists and save them to your local disk. 
Supports video and audio formats, codecs, and other customizations.

Copyright (C) 2023 chatgptdev

This script was designed and written entirely by ChatGPT 4.0 based on prompts 
by @chatgptdev

This program is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published by
the Open Source Initiative.

You should have received a copy of the MIT License along with this
program. If not, see <https://opensource.org/licenses/MIT>.
"""

import argparse
import os
import youtube_dl
import ffmpeg

def parse_arguments():
    parser = argparse.ArgumentParser(description="Download YouTube videos and save them to disk.")
    parser.add_argument("url", help="The URL of the YouTube video or playlist to download.")
    parser.add_argument("-o", "--output", help="The output directory for the downloaded video(s).", default=".")
    parser.add_argument("-vf", "--video-format", help="The desired video format.", choices=["mp4", "mkv", "webm"], default="mp4")
    parser.add_argument("-af", "--audio-format", help="The desired audio format. If provided, the program will download the audio-only version.", choices=["mp3", "m4a", "ogg", "wav"])
    parser.add_argument("-p", "--playlist", action="store_true", help="If set, treat the URL as a playlist and download all videos in the playlist.")
    parser.add_argument("-s", "--subtitles", help="The desired subtitle language (e.g., 'en' for English). If provided, the program will download subtitles in the specified language.")
    parser.add_argument("-q", "--quality", help="The desired video quality (e.g., '720p', '480p', '360p').", choices=["1080p", "720p", "480p", "360p"], default="1080p")
    parser.add_argument("-l", "--limit", type=int, help="The maximum download speed in KiB/s (e.g., 500 for 500 KiB/s). If provided, the program will limit the download speed.")
    parser.add_argument("--proxy", help="The proxy server to use (e.g., 'http://proxy.example.com:8080'). If provided, the program will use the specified proxy server for downloading.")
    parser.add_argument("--video-codec", help="The desired video codec (e.g., 'h264', 'vp9'). If provided, the program will download videos with the specified codec.")
    parser.add_argument("--audio-codec", help="The desired audio codec (e.g., 'aac', 'opus'). If provided, the program will download audio with the specified codec.")
    parser.add_argument("--metadata", nargs="+", help="Custom metadata to set for the downloaded video(s) in the format 'key=value'. Multiple metadata fields can be specified.")
    return parser.parse_args()


def download_video(url, output_dir, video_format, audio_format, is_playlist, subtitles, quality, limit_speed, proxy, video_codec, audio_codec, metadata):
    os.makedirs(output_dir, exist_ok=True)

    video_codec_selector = f"[vcodec={video_codec}]" if video_codec else ""
    audio_codec_selector = f"[acodec={audio_codec}]" if audio_codec else ""

    format_selector = f"bestvideo[height<={quality[:-1]}][ext={video_format}]{video_codec_selector}+bestaudio[ext=m4a]{audio_codec_selector}/best[height<={quality[:-1]}][ext={video_format}]/best"
    if audio_format:
        format_selector = f"bestaudio/best{audio_codec_selector}"

    metadata_opts = {}
    if metadata:
        for item in metadata:
            key, value = item.split("=", 1)
            metadata_opts[key] = value

    postprocessor_args = []
    if video_codec:
        postprocessor_args.extend(["-vcodec", video_codec])
    if audio_codec:
        postprocessor_args.extend(["-acodec", audio_codec])
    if metadata_opts:
        for key, value in metadata_opts.items():
            postprocessor_args.extend(["-metadata", f"{key}={value}"])

    postprocessor_dict = {
        "key": "FFmpegVideoConvertor" if not audio_format else "FFmpegExtractAudio",
        "preferedformat": video_format if not audio_format else audio_format,
    }

    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(playlist)s" if is_playlist else "", "%(title)s.%(ext)s"),
        "format": format_selector,
        "postprocessors": [postprocessor_dict],
        "writesubtitles": bool(subtitles),
        "subtitleslangs": [subtitles] if subtitles else None,
        "noplaylist": not is_playlist,
        "continuedl": True,
        "ratelimit": limit_speed * 1024 if limit_speed else None,
        "proxy": proxy,
        "postprocessor_args": postprocessor_args if postprocessor_args else None,
        "fragment_retries": 2
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    args = parse_arguments()
    download_video(args.url, args.output, args.video_format, args.audio_format, args.playlist, args.subtitles, args.quality, args.limit, args.proxy, args.video_codec, args.audio_codec, args.metadata)

if __name__ == "__main__":
    main()
