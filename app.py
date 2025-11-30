
from flask import Flask, request, send_file
import os, subprocess, uuid

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    file = request.files.get('video')
    if not file:
        return "No file", 400

    uid=str(uuid.uuid4())
    input_path=f"input_{uid}.mp4"
    audio_path=f"audio_{uid}.wav"
    subs_path=f"subs_{uid}.srt"
    out_path=f"out_{uid}.mp4"

    file.save(input_path)

    subprocess.run(["ffmpeg","-i",input_path,audio_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    with open(subs_path,"w") as f:
        f.write("1\n00:00:00,000 --> 00:00:02,000\n[Teks contoh terjemahan di sini]\n")

    subprocess.run(["ffmpeg","-i",input_path,"-vf",f"subtitles={subs_path}",out_path],
                   stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    return send_file(out_path,as_attachment=True)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
