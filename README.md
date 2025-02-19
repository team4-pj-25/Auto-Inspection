# Auto-Inspection
REST API developed using FastAPI <br>
In the pre-packaging stage, this API is used to inspect whether the product is properly included.

Require fine-tuned YOLO11-L detect model (file name: best_model.pt) <br>
model ref: https://docs.ultralytics.com/ko/tasks/detect/

**Endpoint:** <br>
`POST /predict/image/`

**Request**: <br>
{ <br>
&emsp;"flie": img <br>
} <br>

**Response**: <br>
{   <br>
&emsp;"original_image": img(base64 format), <br>
&emsp;"detected_image": img(base64 format) <br>
} 

## Easy usage with Docker Image
**docker run -p 8003:8003 kosonkh7/team4_product_inspection:v0.2.0** (or latest) <br>
test url: localhost:8003/docs
