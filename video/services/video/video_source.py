class VideoSource:
    
    def __init__(self, src: str) -> None:
        self.src: str = src
        self.duration = None
        self.extension = None
        self.mime_type = None