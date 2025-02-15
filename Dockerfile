# Python Slim 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 설치 (OpenCV, YOLO 관련 라이브러리 포함)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \       
    libglib2.0-0 \          
    ffmpeg \                 
    libsm6 \                
    libxrender1 \           
    libxext6 \              
    && rm -rf /var/lib/apt/lists/*

# 필요한 패키지 설치 (파이토치 CPU 버전 사용, ultralytics를 위한 사전 설치)
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /app

# 포트 노출
EXPOSE 8003

# FastAPI 실행 (포트 8003에서 실행)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload", "--log-level", "info"]