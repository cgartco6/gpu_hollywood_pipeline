from models.video_sd import VideoSD
from models.wav2lip import Wav2Lip
from models.xtts import XTTS
from models.musicgen import MusicGen
from gpu.inference_engine import InferenceEngine


class Orchestrator:

    def __init__(self):

        self.engine = InferenceEngine()

        self.video = VideoSD()
        self.audio = XTTS()
        self.music = MusicGen()
        self.lipsync = Wav2Lip()

    def run(self, scene):

        video_path = f"outputs/video_{scene['id']}.png"
        audio_path = f"outputs/audio_{scene['id']}.wav"
        music_path = f"outputs/music_{scene['id']}.wav"
        final_path = f"outputs/final_{scene['id']}.mp4"

        audio = self.engine.run(self.audio.synthesize, scene["voice"], audio_path)

        video = self.engine.run(self.video.generate, scene["visual"], video_path)

        music = self.engine.run(self.music.generate, scene["music"], music_path)

        final = self.engine.run(
            self.lipsync.apply,
            video,
            audio,
            final_path
        )

        return {
            "video": final,
            "audio": audio,
            "music": music
        }
