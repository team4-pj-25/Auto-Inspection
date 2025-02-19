# Auto-Inspection
API developed using FastAPI <br>
Require fine-tuned YOLO11-L detect model (file name: best_model.pt) <br>
model ref: https://docs.ultralytics.com/ko/tasks/detect/

**request(POST)**: {<br>
  "flie": img <br>
  } <br>

**response**: {   <br>
  "original_image": img(base64 format), <br>
  "detected_image": img(base64 format) <br>
  } 

## Easy usage with Docker Image
**docker run -p 8003:8003 kosonkh7/team4_product_inspection:v0.2.0** (or latest) <br>
test url: localhost:8003/docs
