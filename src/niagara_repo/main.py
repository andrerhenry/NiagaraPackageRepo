import os
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

os.makedirs('/tmp/uploads', exist_ok=True)
UPLOAD_FOLDER = '/tmp/uploads'
#UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'jar', 'txt'}

# Set working directory to root of repo
#os.chdir(Path.cwd().parent.parent)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(32)

def allowed_file(filename:str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/uploads', methods=['POST'] )
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        print(file)

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))    


        


@app.route('/niagara/4.14/<package_name>', methods=['GET'])
def get_package(package_name:str):
    return print(f'Attempting to get: {package_name}')





def main():
    print("Hello from niagarapackagerepo!")


if __name__ == "__main__":
    main()
