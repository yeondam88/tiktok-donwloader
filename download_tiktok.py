import yt_dlp

def download_tiktok_video(url, output_path="output.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 가장 높은 품질로 다운로드
        'outtmpl': output_path,  # 출력 파일 이름
        'merge_output_format': 'mp4',  # 비디오와 오디오를 mp4로 병합
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
