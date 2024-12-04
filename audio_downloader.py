import yt_dlp

def download_audio_yt_dlp(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'C:/ffmpeg/bin',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    link = input("Enter the YouTube video link: ").strip()
    download_audio_yt_dlp(link)
