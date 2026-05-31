from diffusers import StableDiffusionPipeline
import torch
from gpu.device import get_device


class VideoSD:

    def __init__(self):

        self.device = get_device()

        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )

        self.pipe = self.pipe.to(self.device)

    def generate(self, prompt: str, output_path: str):

        image = self.pipe(prompt).images[0]
        image.save(output_path)

        return output_path
