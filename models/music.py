class MusicModel:

    def generate(self, prompt, output_path):

        with open(output_path, "w") as f:
            f.write(f"MUSIC:{prompt}")

        return output_path
