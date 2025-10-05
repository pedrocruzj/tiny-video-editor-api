# 🎬 Tiny video editor API

A simple API that allows you to resize a video and add overlays to it.

---

## 🖥️ Server

./dev.sh -u → Start the server and build containers if they are not already built.  
./dev.sh -d → Stop the server.  
./dev.sh -b → Build containers only.

## 📦 Endpoint

`POST /video/edit`

---

## 🧩 Description

This endpoint processes a video by resizing it and optionally adding image overlays.

---

## 🧾 Request Body

### Parameters

| Name   | Type     | Required | Description                                         |
| ------ | -------- | -------- | --------------------------------------------------- |
| `src`  | `string` | ✅       | URL of the source video.                            |
| `data` | `object` | ✅       | JSON object containing video settings and overlays. |

---

## 💡 Example Request

```bash
POST /video/edit
Content-Type: application/json

{
  "src": "https://example.com/video.mp4",
  "options": {
    "main": {
      "width": 300,
      "height": "-1",          // Use current height
      "pix_fmt": "yuv420p"     // Default value
    },
    "overlays": [
      {
        "src": "https://example.com/myimg.jpg",
        "width": 100,
        "left": 50,
        "top": 50
      }
    ]
  }
}
```

## ⚙️ Response

The local path of the video is returned. Example: /usr/src/app/storage/outputs/2b381d73-b89f-416b-8de3-693b8978b920.mp4
