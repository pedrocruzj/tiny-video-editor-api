from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from video.services.video.video_editor_service import VideoEditorService
from video.services.video.video_source import VideoSource
import json
from core.utils.dot_dict import DotDict


def edit(request: HttpRequest):
    if request.method != "POST":
        return HttpResponse("Method POST is required", status=405)

    opts = DotDict(request.POST.get("options"))
    editor = VideoEditorService(
        VideoSource(src=str(request.POST.get("src"))),
        pix_fmt=str(opts.get("main.pix_fmt", "yuv420p")),
    )
    output_name = editor.run(json.loads(str(request.POST.get("options"))))

    return HttpResponse(output_name)
