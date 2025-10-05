from abc import ABC
from ffmpeg.nodes import Stream
from core.utils.dot_dict import DotDict


class AbstractOperation(ABC):

    def __init__(self, stream: Stream) -> None:
        raise NotImplementedError("This method is not implemented")

    def run(self, options: DotDict) -> Stream:
        raise NotImplementedError("This method is not implemented")
