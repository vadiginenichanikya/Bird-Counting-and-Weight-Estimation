from processor import analyze_video
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app/main.py <video_path>")
        sys.exit(1)

    video_path = sys.argv[1]

    output_video, json_output = analyze_video(video_path)

    print("Processing completed ✅")
    print("Annotated video:", output_video)
    print("JSON output:", json_output)
