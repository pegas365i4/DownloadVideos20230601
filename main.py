import yt_dlp

url = "https://www.youtube.com/watch?v=PQMzOUeprlk"
ydl_opts = {
    "writeautomaticsub": True,
    "subtitleslangs": ["en"],
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
