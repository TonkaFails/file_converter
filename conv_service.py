import os
import ffmpeg
import threading
import time

def convert_file(output_format, input_path, output_path):
    print(f"Input Path: {input_path}, Output Path: {output_path}, Output Format: {output_format}")
    try:
        if output_format == 'mp4':
            ffmpeg.input(input_path).output(output_path, vcodec='libx264', pix_fmt='yuv420p').run(overwrite_output=True)
        elif output_format == 'gif':
            ffmpeg.input(input_path).output(output_path).run()
        elif output_format == 'png' or output_format == 'jpg' or output_format == 'jpeg':
            ffmpeg.input(input_path).output(output_path, vframes=1).run()
        elif output_format == 'mp3':
            ffmpeg.input(input_path).output(output_path, audio_bitrate='192k').run()
    except ffmpeg.Error as e:
        print(e.stderr)
        raise

def delayed_delete(file_path, delay=10):
    def task():
        try:
            time.sleep(delay)
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    threading.Thread(target=task).start()