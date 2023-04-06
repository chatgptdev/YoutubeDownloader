# YoutubeDownloader

A command-line program to download YouTube videos and save them to disk. The program supports downloading individual videos, playlists, and downloading audio-only versions. It also provides options to customize video quality, format, and codecs.

It was entirely designed and implemented by ChatGPT 4.0 following prompts by @chatgptdev.

## Requirements

  - Python 3.6+
  - youtube-dl
  - ffmpeg (both python package and ffmpeg binary)

To install the required packages, run the following command:

```
pip install ffmpeg-python
pip uninstall youtube-dl
pip install git+https://github.com/ytdl-org/youtube-dl.git@master
```

Due to [an issue](https://github.com/ytdl-org/youtube-dl/issues/31530) that was fixed in the master branch but not yet officially released, it's necessary to install the most recent version of youtube-dl from the GitHub master branch using the commands mentionned above.

ffmpeg binaries can be downloaded from official website at https://ffmpeg.org/download.html

## Usage

The program can be used as follows:

```
python youtubeDownloader.py [-h] [-o OUTPUT] [-vf {mp4,mkv,webm}] [-af {mp3,m4a,ogg,wav}]
                             [-p] [-s SUBTITLES] [-q {1080p,720p,480p,360p}] [-l LIMIT]
                             [--proxy PROXY] [--video-codec VIDEO_CODEC] [--audio-codec AUDIO_CODEC]
                             [--metadata key=value [key=value ...]] [--info]
                             url
```

Supported options are:

  - `url`: The URL of the YouTube video or playlist to download.
  - `-o`, `--output`: The output directory for the downloaded video(s). (default: current directory)
  - `-vf`, `--video-format`: The desired video format. (choices: mp4, mkv, webm, default: mp4)
  - `-af`, `--audio-format`: The desired audio format. If provided, the program will download the audio-only version. (choices: mp3, m4a, ogg, wav)
  - `-p`, `--playlist`: If set, treat the URL as a playlist and download all videos in the playlist.
  - `-s`, `--subtitles`: The desired subtitle language (e.g., 'en' for English). If provided, the program will download subtitles in the specified language.
  - `-q`, `--quality`: The desired video quality. (choices: 1080p, 720p, 480p, 360p, default: 1080p)
  - `-l`, `--limit`: The maximum download speed in KiB/s (e.g., 500 for 500 KiB/s). If provided, the program will limit the download speed.
  - `--proxy`: The proxy server to use (e.g., 'http://proxy.example.com:8080'). If provided, the program will use the specified proxy server for downloading.
  - `--video-codec`: The desired video codec (e.g., 'h264', 'vp9'). If provided, the program will download videos with the specified codec.
  - `--audio-codec`: The desired audio codec (e.g., 'aac', 'opus'). If provided, the program will download audio with the specified codec.
  - `--metadata`: Custom metadata to set for the downloaded video(s) in the format 'key=value'. Multiple metadata fields can be specified.
  - `--info`: If set, display technical information about the video without downloading it.

## Example

 - To download a video with default settings:

   ```
   python youtubeDownloader.py https://www.youtube.com/watch?v=example
   ```

 - To download a YouTube video in MP4 format with H.264 video codec and in 720p quality and save it in the downloads directory:

   ```
   python youtubeDownloader.py -q 720p -o downloads --video-codec h264 https://www.youtube.com/watch?v=example
   ```

 - Download an audio-only version of a video in mp3 format:
   ```
   python youtubeDownloader.py -af mp3 https://www.youtube.com/watch?v=example
   ```

 - Download a video with subtitles in English:
   ```
   python youtubeDownloader.py -s en https://www.youtube.com/watch?v=example
   ```

 - Download all videos in a playlist:
   ```
   python youtubeDownloader.py -p https://www.youtube.com/playlist?list=example_playlist_id
   ```

 - Display technical information about a video without downloading it:
   ```
   python youtubeDownloader.py --info https://www.youtube.com/watch?v=example
   ```

 - Download a video using a specific video and audio codec:
   ```
   python youtubeDownloader.py --video-codec vp9 --audio-codec opus https://www.youtube.com/watch?v=example
   ```

 - Download a video with custom metadata:
   ```
   python youtubeDownloader.py --metadata title="Custom Title" --metadata author="Custom Author" https://www.youtube.com/watch?v=example
   ```

 - Download a video using a proxy server:
   ```
   python youtubeDownloader.py --proxy http://proxy.example.com:8080 https://www.youtube.com/watch?v=example
   ```

## Contributing

We welcome contributions to improve the script or add new features. If you would like to contribute, please follow these steps:

 1. Fork the repository on GitHub.
 2. Clone your fork to your local machine.
 3. Create a new branch for your changes.
 4. Make your changes and test them.
 5. Commit your changes and push them to your fork.
 6. Create a pull request on the original repository with a clear description of your changes.
    
## License

This project is released under the MIT License. See the [LICENSE](https://github.com/chatgptdev/YoutubeDownloader/blob/main/LICENSE) file for more information.
