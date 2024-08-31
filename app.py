from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash, session
import os
import threading
import time
from download_tiktok import download_tiktok_video

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/downloads'
app.secret_key = 'supersecretkey'

# Ensure the downloads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def delete_file_after_download(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {filename} deleted after download.")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tiktok_url = request.form['tiktok_url']
        filename = request.form['filename'] + '.mp4'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        download_tiktok_video(tiktok_url, filepath)
        
        session['filename'] = filename

        flash(f"File downloaded as {filename}. It will be deleted after you download it.")
        return redirect(url_for('download_file', filename=filename))

    # Clear the filename after handling the POST request
    session.pop('filename', None)
    return render_template('index.html')

@app.route('/downloads/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        # Send file for download
        response = send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
        
        # Delete the file after download
        threading.Thread(target=delete_file_after_download, args=(filename,)).start()

        return response
    else:
        flash("File does not exist or has already been deleted.")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
