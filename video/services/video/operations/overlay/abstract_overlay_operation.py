from abc import ABC
from ffmpeg.nodes import Stream
from video.services.video.operations.overlay.overlay import Overlay


class AbstractOverlayOperation(ABC):

    def __init__(self, stream: Stream) -> None:
        raise NotImplementedError("This method is not implemented")

    def run(self, overlay: Overlay) -> Overlay:
        raise NotImplementedError("This method is not implemented")
