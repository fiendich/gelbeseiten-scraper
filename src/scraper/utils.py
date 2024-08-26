import os

def ensure_output_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
