from typing import Union
from ffmpeg.nodes import Stream


class Overlay:

    def __init__(
        self,
        src: str,
        input_stream: Stream,
        width: float = -1,
        height: float = -1,
        left: float = 0,
        top: float = 0,
        angle: float = 0,
    ) -> None:
        self.src = src
        self.input_stream = input_stream
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.angle = angle
