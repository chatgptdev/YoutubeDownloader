# YoutubeDownloader

This script allows you to download YouTube videos or playlists and save them to your local disk. It also supports video and audio formats, codecs, and other customizations.

It was entirely design and implemented by ChatGPT 4.0 following prompts by @chatgptdev.

## Requirements

  - Python 3.6+
  - youtube-dl
  - ffmpeg (both python package and ffmpeg binary)

To install the required packages, run the following command:

```
pip install ffmpeg-python
pip install git+https://github.com/ytdl-org/youtube-dl.git@master
```

Due to [an issue](https://github.com/ytdl-org/youtube-dl/issues/31530) that was fixed in the master branch but not yet officially released, it's necessary to install the most recent version of youtube-dl from the GitHub master branch using the command mentionned above.
If you have already installed youtube-dl, please uninstall it first:
```
pip uninstall youtube-dl
```

## Usage

To use the script, execute the following command:

```
python3 youtubeDownloader.py [url] [options]
```

Supported options are:

    url: The URL of the YouTube video or playlist to download.
    -o, --output: The output directory for the downloaded video(s). (default: current directory)
    -vf, --video-format: The desired video format. (choices: "mp4", "mkv", "webm"; default: "mp4")
    -af, --audio-format: The desired audio format. If provided, the program will download the audio-only version. (choices: "mp3", "m4a", "ogg", "wav")
    -p, --playlist: Treat the URL as a playlist and download all videos in the playlist.
    -s, --subtitles: The desired subtitle language (e.g., "en" for English). If provided, the program will download subtitles in the specified language.
    -q, --quality: The desired video quality. (choices: "1080p", "720p", "480p", "360p"; default: "1080p")
    -l, --limit: The maximum download speed in KiB/s (e.g., 500 for 500 KiB/s). If provided, the program will limit the download speed.
    --proxy: The proxy server to use (e.g., "http://proxy.example.com:8080"). If provided, the program will use the specified proxy server for downloading.
    --video-codec: The desired video codec (e.g., "h264", "vp9"). If provided, the program will download videos with the specified codec.
    --audio-codec: The desired audio codec (e.g., "aac", "opus"). If provided, the program will download audio with the specified codec.
    --metadata: Custom metadata to set for the downloaded video(s) in the format "key=value". Multiple metadata fields can be specified.

## Example

To download a YouTube video in MP4 format with H.264 video codec, run the following command:

```
python3 youtubeDownloader.py https://www.youtube.com/watch?v=example -o downloads --video-codec h264
```

This will download the video and save it to the "downloads" folder in MP4 format with H.264 video codec.

## License

This project is released under the MIT License.
