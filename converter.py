from pydub import AudioSegment
from pathlib import Path
from shutil import copyfile
import sys
import os


def main():
    root_dir = Path(sys.argv[1])
    export_dir = Path(str(root_dir.parent) + "/" + root_dir.name + "_mp3_export")
    os.mkdir(export_dir)
    
    operate_dir(root_dir, export_dir)


def operate_dir(cur_dir, export_dir):
    for file in os.listdir(cur_dir):
        file_path = os.path.join(cur_dir, file)
        suffix = os.path.splitext(file_path)[1]
        # replicate directory tree for exported files
        if os.path.isdir(file_path):
            new_dir = os.path.join(export_dir, file)
            os.mkdir(new_dir)
            operate_dir(file_path, new_dir)
        # export flac files to mp3
        elif suffix == ".flac":
            print("converting " + file)
            flac_audio = AudioSegment.from_file(file_path, format="flac")
            export_file = os.path.join(export_dir, file)
            flac_audio.export(export_file, format="mp3")
        # copy over other files
        else:
            print("copying " + file)
            copyfile(file_path, os.path.join(export_dir, file))

if __name__ == "__main__":
    main()

