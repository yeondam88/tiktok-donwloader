from flask import Flask, render_template, request, send_from_directory
import os
from download_tiktok import download_tiktok_video

app = Flask(__name__)
DOWNLOAD_FOLDER = 'static/downloads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        filename = request.form['filename'] + '.mp4'
        output_path = os.path.join(DOWNLOAD_FOLDER, filename)

        try:
            download_tiktok_video(url, output_path)
            return render_template('index.html', filename=filename)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == '__main__':
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
