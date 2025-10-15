from ffmpeg.nodes import Stream
import ffmpeg
from video.services.video.operations.abstract_operation import AbstractOperation
from video.services.video.operations.overlay.scale import Scale
from core.utils.dot_dict import DotDict
from video.services.video.operations.overlay.overlay import Overlay
from video.services.video.operations.overlay.scale import Scale


class AddText(AbstractOperation):
    operations = [Scale]

    def __init__(self, stream: Stream) -> None:
        self._stream = stream

    def run(self, options: DotDict) -> Stream:
        texts = options.get("texts")

        if texts != None and isinstance(texts, list):
            for text in texts:
                text = DotDict(text)
                content = text.get("content")
                left = int(text.get("left", 0))
                top = int(text.get("top", 0))
                color = text.get("color", "black")
                size = text.get("size", 15)
                fontFile = text.get("font_file")
                args = {}

                if fontFile:
                    args = {"fontfile": f"storage/fonts/{fontFile}"}

                if content:
                    self._stream = ffmpeg.drawtext(
                        self._stream,
                        content,
                        left,
                        top,
                        fontcolor=color,
                        fontsize=size,
                        **args,
                    )

        return self._stream
