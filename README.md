# Auto-Inspection
API developed using FastAPI

Require fine-tuned YOLO11-L detect model (File Name: best_model.pt) <br>
ref: https://docs.ultralytics.com/ko/tasks/detect/

## usage with Docker Image
cmd: docker run -p 8003:8003 kosonkh7/team4_product_inspection:v0.2.0 (or latest) <br>
test: localhost:8003/docs

**request(POST)**: img(jpg format) <br>
**response**: {   <br>
  "original_image": img(base64 format), <br>
  "detected_image": img(base64 format) <br>
} 
