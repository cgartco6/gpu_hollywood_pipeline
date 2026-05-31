class Wav2Lip:

    def __init__(self):
        pass

    def apply(self, video_path, audio_path, output_path):

        # REAL: wav2lip inference call goes here

        with open(output_path, "w") as f:
            f.write(f"WAV2LIP:{video_path}+{audio_path}")

        return output_path
