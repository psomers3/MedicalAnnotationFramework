import os
import shutil
from seg_utils.utils.database import SQLiteDatabase


class Structure:
    IMAGES_DIR = "/data/images/"
    VIDEOS_DIR = "/data/videos/"
    WSI_DIR = "/data/whole slide images/"
    FILE_DIRS = [IMAGES_DIR, VIDEOS_DIR, WSI_DIR]
    DATABASE_DEFAULT_NAME = '/database.db'


def create_project_structure(project_path: str):
    """This method takes the user-specified project location and
     (1) creates the necessary directories for the project
     (2) calls the Database class to create an empty database with the desired structure"""
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
    os.makedirs(project_path)
    for file_dir in Structure.FILE_DIRS:
        os.makedirs(project_path + file_dir)
    database_path = project_path + Structure.DATABASE_DEFAULT_NAME
    _ = SQLiteDatabase(database_path, True)


def check_environment(project_path: str) -> bool:
    """This function checks for a given path whether it is a valid project location,
    i.e. whether it contains a 'data' folder with videos, images and whole slide images"""
    for file_dir in Structure.FILE_DIRS:
        if not os.path.exists(project_path + file_dir):
            return False
    return True
