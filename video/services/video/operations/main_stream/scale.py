from ffmpeg.nodes import Stream
from video.services.video.operations.abstract_operation import AbstractOperation
from core.utils.dot_dict import DotDict
import ffmpeg


class Scale(AbstractOperation):
    def __init__(self, stream: Stream) -> None:
        self._stream = stream

    def run(self, options: DotDict) -> Stream:
        height = options.get("main.height", default="-1")
        width = options.get("main.width", default="-1")

        if width or height:
            self._stream = ffmpeg.filter(self._stream, "scale", width, height)

        return self._stream
