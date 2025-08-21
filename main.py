from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import json
from datetime import datetime
import os
import aiofiles
from data_processor import DataProcessor
from models import UploadResponse, FilterRequest

app = FastAPI(
    title="医疗器械不良事件分析系统API",
    description="提供医疗器械不良事件数据的上传、处理和分析功能",
    version="1.0.0"
)

# 配置CORS - 允许所有来源（在生产环境中应该更严格）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，或指定您的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 确保上传目录存在
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/api/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    # 您的上传逻辑...

@app.post("/api/process-data")
async def process_data(filters: FilterRequest):
    # 您的处理逻辑...

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

# 添加根路径路由
@app.get("/")
async def root():
    return {"message": "Medical Device Analysis API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)