class TTSModel:

    def synthesize(self, text, output_path):

        with open(output_path, "w") as f:
            f.write(f"AUDIO:{text}")

        return output_path
