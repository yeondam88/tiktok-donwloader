import yt_dlp

def download_tiktok_video(url, output_path="output.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 가장 높은 품질로 다운로드
        'outtmpl': output_path,  # 출력 파일 이름
        'merge_output_format': 'mp4',  # 비디오와 오디오를 mp4로 병합
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_reel(url, output_path="output.mp4"):
    ydl_opts = {
        'format': 'best',  # 고화질 다운로드
        'outtmpl': output_path,
        'merge_output_format': 'mp4',  # 영상 포맷
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info_dict)
        return file_path