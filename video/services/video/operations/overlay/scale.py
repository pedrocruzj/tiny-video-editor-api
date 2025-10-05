from ffmpeg.nodes import Stream
import ffmpeg
from video.services.video.operations.overlay.abstract_overlay_operation import (
    AbstractOverlayOperation,
)
from video.services.video.operations.overlay.overlay import Overlay


class Scale(AbstractOverlayOperation):
    def __init__(self, stream: Stream) -> None:
        self._stream = stream

    def run(self, overlay: Overlay) -> Overlay:
        if overlay.input_stream != None:

            if overlay.width != "-1" or overlay.height != "-1":
                overlay.input_stream = ffmpeg.filter(
                    overlay.input_stream, "scale", overlay.width, overlay.height
                )

        return overlay
