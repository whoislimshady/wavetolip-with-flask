import os
from app import app
#import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from   inference import *

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_video():
    
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file1 = request.files['file1']
	file = request.files['file']
 
  	
	if file.filename  == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		filename = "input_vid.mp4"
		
		file1.save(app.config['UPLOAD_FOLDER']+"input_audio.wav")
		file.save(app.config['UPLOAD_FOLDER']+filename)
		main()
		#print('upload_video filename: ' + filename)
		flash('Video successfully uploaded and displayed below')

		return render_template('upload.html', filename=filename)
	

@app.route('/display/<filename>')
def display_video(filename):
	return redirect(url_for('results', filename), code=301)




if __name__ == "__main__":
    app.run()