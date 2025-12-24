Bird Counting and Weight Estimation (Prototype)
Overview

This project is a prototype system for bird counting and weight estimation using a fixed-camera poultry CCTV video.

The system processes a video input and generates:

An annotated output video with bird count overlay

A JSON file containing detection and weight estimation details

This prototype is designed to demonstrate understanding of computer vision pipelines, object tracking concepts, and API-oriented architecture, as required for the internship task.

Project Features

Processes a fixed-camera poultry video

Simulated bird detection and tracking

Maintains stable bird IDs (rule-based simulation)

Counts birds over time

Estimates bird weight using a visual proxy

Generates annotated video output

Exports structured JSON results

Project Structure
Bird-Counting-and-Weight-Estimation/
├── app/
│   ├── main.py            # Entry point to run the pipeline
│   └── processor.py       # Complete video processing pipeline
├── src/
│   ├── bird_detector.py   # Planned module (future extension)
│   ├── tracker.py         # Planned module (future extension)
│   ├── weight_estimator.py# Planned module (future extension)
│   └── utils.py           # Planned module (future extension)
├── input_videos/
│   └── poultry_video.mp4  # Input poultry CCTV video
├── outputs/
│   ├── annotated_video_final.mp4  # Annotated output video
│   └── result_final.json          # JSON analysis results
├── requirements.txt
└── README.md

Design Note

The project is designed with a modular architecture in mind.

The src/ directory represents planned modular components such as:

Bird detection

Bird tracking

Weight estimation

For this prototype submission, the entire working pipeline is implemented inside app/processor.py to ensure a fully functional end-to-end demo within the given time constraints.

The architecture can be easily extended by migrating logic from processor.py into the respective modules inside src/.

Installation

Install required dependencies using:

pip install -r requirements.txt

How to Run

Run the pipeline using the following command:

python app/main.py input_videos/poultry_video.mp4

Output Files

After successful execution, the following files are generated inside the outputs/ directory:

annotated_video_final.mp4
Annotated video showing bird count overlay

result_final.json
JSON file containing:

Total birds detected

Frame-wise bird IDs

Estimated weight values

Processing timestamp

Weight Estimation Logic

This prototype uses a rule-based visual proxy for bird weight estimation.

Weight values are simulated based on detection logic

This approach demonstrates the pipeline structure

Can be replaced with regression or ML-based estimation models

Notes

This is a prototype implementation

Detection, tracking, and weight estimation are simulated

Designed for fixed-camera poultry videos

Easily extendable using YOLO + DeepSORT or similar models
