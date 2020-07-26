import hashlib
import os

from werkzeug.utils import secure_filename


class UploadFile:
    def saveFile(file,path):
        file_name = hashlib.md5(os.path.splitext(os.path.basename(file.filename))[0].encode("utf")).hexdigest()
        file_type = os.path.splitext(os.path.basename(file.filename))[1]
        file.save(path+secure_filename(file_name + file_type))
        return file_name +file_type