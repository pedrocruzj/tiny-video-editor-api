from video.services.video.operations.main_stream.scale import Scale
from video.services.video.operations.overlay.add_overlay import AddOverlay
from ffmpeg.nodes import Stream
from core.utils.dot_dict import DotDict


class RunOperations:

    operations = [Scale, AddOverlay]

    def __init__(self, stream: Stream) -> None:
        self._stream: Stream = stream

    def run(self, options: DotDict) -> Stream:
        for operation in self.operations:
            self._stream = operation(self._stream).run(options)

        return self._stream
