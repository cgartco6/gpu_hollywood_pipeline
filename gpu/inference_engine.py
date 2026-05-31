from gpu.device import get_device
from gpu.memory import clear_cache


class InferenceEngine:

    def __init__(self):

        self.device = get_device()

    def run(self, model_fn, *args, **kwargs):

        """
        Central GPU execution wrapper
        """

        try:
            result = model_fn(*args, **kwargs)
            return result

        finally:
            clear_cache()
