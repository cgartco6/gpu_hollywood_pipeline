import subprocess


def build_final(video_files, output="outputs/final_movie.mp4"):

    cmd = ["ffmpeg", "-y"]

    for v in video_files:
        cmd += ["-i", v["video"]]

    cmd += ["-filter_complex", "concat=n=1:v=1:a=1", output]

    subprocess.run(cmd)

    return output
