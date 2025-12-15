import os
from pathlib import Path
from flask import Flask, flash, request, redirect, url_for, send_file, jsonify
from werkzeug.utils import secure_filename
from typing import Any

ALLOWED_EXTENSIONS = {'jar', 'txt'}

def setup_app():
    os.makedirs('/tmp/uploads', exist_ok=True)
    # UPLOAD_FOLDER = '/tmp/uploads'
    UPLOAD_FOLDER = 'uploads'


    # Set working directory to root of repo
    #os.chdir(Path.cwd().parent.parent)

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = os.urandom(32)


    @app.route('/api/uploads', methods=['POST'] )
    def upload_file() -> Any:

        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file is None or file.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            print('file is in allowed files:', file.filename)
            
            if file.filename:
                filename = secure_filename(file.filename)
                save_path = Path(app.config['UPLOAD_FOLDER'])/filename
                print('file save path:', save_path)
                file.save(save_path)
            print('file saved sucessfully:', save_path.exists())
            return jsonify({"message": "Data received successfully"}), 200

    @app.route('/niagara/4.14/<package_name>', methods=['GET'])
    def get_package(package_name:str) ->Any:
        return print(f'Attempting to get: {package_name}')

    return app



def allowed_file(filename:str | None) -> bool:
    if filename:
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    if not filename:
        return False



if __name__ == "__main__":
    app = setup_app()
