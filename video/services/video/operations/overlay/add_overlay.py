from ffmpeg.nodes import Stream
import ffmpeg
from video.services.video.operations.abstract_operation import AbstractOperation
from video.services.video.operations.overlay.scale import Scale
from core.utils.dot_dict import DotDict
from video.services.video.operations.overlay.overlay import Overlay
from video.services.video.operations.overlay.scale import Scale


class AddOverlay(AbstractOperation):
    operations = [Scale]

    def __init__(self, stream: Stream) -> None:
        self._stream = stream

    def run(self, options: DotDict) -> Stream:
        overlays = options.get("overlays")

        if overlays != None and isinstance(overlays, list):
            for overlay in overlays:
                overlay = DotDict(overlay)
                src = overlay.get("src")

                if src != None:
                    left = float(overlay.get("left", 0))
                    top = float(overlay.get("top", 0))
                    width = float(overlay.get("width", -1))
                    height = float(overlay.get("height", -1))
                    angle = float(overlay.get("angle", 0))

                    overlay_obj = Overlay(
                        src=src,
                        input_stream=ffmpeg.input(src),
                        width=width,
                        height=height,
                        left=left,
                        top=top,
                        angle=angle,
                    )

                    for operation in self.operations:
                        overlay_obj = operation(self._stream).run(overlay_obj)

                    self._stream = ffmpeg.filter(
                        [self._stream, overlay_obj.input_stream], "overlay", left, top
                    )

        return self._stream
