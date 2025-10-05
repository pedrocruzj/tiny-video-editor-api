from video.services.video.video_source import VideoSource
from video.services.video.run_operations import RunOperations
import ffmpeg
from core.utils.dot_dict import DotDict
from uuid import uuid4
from os import getenv


class VideoEditorService:

    def __init__(self, source: VideoSource, pix_fmt="yuv420p") -> None:
        self._source = source
        self._stream = ffmpeg.input(source.src)
        self._pix_fmt = pix_fmt

    def run(self, options: dict) -> str:
        stream = RunOperations(self._stream).run(DotDict(options))

        output_name = (
            str(getenv("ROOT_PATH"))
            + "/storage/outputs/"
            + str(uuid4())
            + "."
            + self._source.src.split(".").pop()
        )

        out = ffmpeg.output(stream, output_name, pix_fmt=self._pix_fmt)
        ffmpeg.run(out)

        return output_name
