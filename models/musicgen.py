class MusicGen:

    def __init__(self):
        pass

    def generate(self, prompt, output_path):

        # REAL: transformers / audioldm pipeline

        with open(output_path, "w") as f:
            f.write(f"MUSICGEN:{prompt}")

        return output_path
