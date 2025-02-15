from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
from ultralytics import YOLO
import base64

app = FastAPI()

# YOLO 모델 로드
model = YOLO("best_model.pt")

# 클래스 이름 설정
class_names = [
    "bread", "snack", "coffee", "juice", "noodle", "seasoning", "shampoo",
    "soap", "bodywash", "moisturizer", "detergent", "toothpaste", "tata_salt",
    "cheese", "egg", "milk", "meat", "sausages", "beverage", "canned_food",
    "miscellaneous_item", "apple", "banana", "tomato", "cucumber", "carrot"
]

# 클래스별 색상 생성 함수
def get_color(cls_id):
    np.random.seed(cls_id)  # 클래스 ID를 기반으로 고유한 색상을 생성
    return tuple(np.random.randint(0, 255, 3).tolist())

@app.get("/")
async def root():
    return {"message": "FastAPI YOLO Server is Running!"}

@app.get("/model/info")
def get_model_info():
    return {"model_classes": class_names}

@app.post("/predict/image/")
async def predict_image(file: UploadFile = File(...)):
    print("GETIN")

    # 파일을 바이트로 읽고 OpenCV에서 처리
    file_bytes = await file.read()
    np_arr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # 원본 이미지 저장 (Base64로 변환)
    _, img_encoded = cv2.imencode('.jpg', image)
    original_image_base64 = base64.b64encode(img_encoded).decode("utf-8")

    # YOLO 예측 수행
    results = model(image, conf=0.25)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # 바운딩 박스 좌표
            cls_id = int(box.cls[0])  # 클래스 ID
            conf = float(box.conf[0])
            color = get_color(cls_id)  # 클래스 ID에 따른 색상 지정

            # 바운딩 박스 그리기
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            label = f"{class_names[cls_id]} ({conf:.2f})"
            cv2.putText(image, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 검출된 이미지도 Base64로 변환
    _, detected_img_encoded = cv2.imencode('.jpg', image)
    detected_image_base64 = base64.b64encode(detected_img_encoded).decode("utf-8")

    # JSON으로 원본과 YOLO 결과 이미지 함께 반환
    return JSONResponse(content={
        "original_image": original_image_base64,
        "detected_image": detected_image_base64
    })
