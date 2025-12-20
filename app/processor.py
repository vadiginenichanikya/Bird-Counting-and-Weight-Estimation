import cv2
import json
import os
from datetime import datetime

def analyze_video(video_path, output_dir="outputs"):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("Cannot open video file")

    bird_count = 0
    frame_id = 0
    detections = []

    output_video_path = os.path.join(output_dir, "annotated_output.mp4")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_id += 1

        # Dummy bird detection (simulation)
        if frame_id % 30 == 0:
            bird_count += 1
            detections.append({
                "frame": frame_id,
                "bird_id": bird_count,
                "estimated_weight_grams": 120
            })

        cv2.putText(
            frame,
            f"Bird Count: {bird_count}",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        out.write(frame)

    cap.release()
    out.release()

    json_output = {
        "video": os.path.basename(video_path),
        "total_birds_detected": bird_count,
        "detections": detections,
        "processed_at": datetime.now().isoformat()
    }

    json_path = os.path.join(output_dir, "result.json")
    with open(json_path, "w") as f:
        json.dump(json_output, f, indent=4)

    return output_video_path, json_path
