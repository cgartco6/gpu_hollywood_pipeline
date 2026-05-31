from models.video_diffusion import VideoDiffusionModel
from models.lipsync import LipSyncEngine
from models.tts import TTSModel
from models.music import MusicModel


video_model = VideoDiffusionModel()
lipsync = LipSyncEngine()
tts = TTSModel()
music = MusicModel()


def process_scene(scene):

    video_path = f"outputs/video_{scene['id']}.mp4"
    audio_path = f"outputs/audio_{scene['id']}.wav"
    music_path = f"outputs/music_{scene['id']}.wav"
    final_path = f"outputs/final_{scene['id']}.mp4"

    audio = tts.synthesize(scene["voice"], audio_path)
    vid = video_model.generate(scene["visual"], video_path)
    mus = music.generate(scene["music"], music_path)

    final = lipsync.apply(vid, audio, final_path)

    return {
        "video": final,
        "audio": audio,
        "music": mus
    }
