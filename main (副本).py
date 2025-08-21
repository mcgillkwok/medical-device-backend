# backend/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import json
from datetime import datetime
import os
from data_processor import DataProcessor

app = FastAPI(title="医疗器械不良事件分析系统API")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 确保上传目录存在
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    """处理文件上传"""
    try:
        # 保存上传的文件
        file_path = os.path.join(UPLOAD_DIR, f"{datetime.now().timestamp()}_{file.filename}")
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # 处理数据
        processor = DataProcessor(file_path, file.filename)
        result = processor.process()
        
        # 删除临时文件
        os.remove(file_path)
        
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"文件处理失败: {str(e)}")

@app.post("/api/process-data")
async def process_data(filters: dict):
    """根据筛选条件处理数据"""
    try:
        # 这里实现根据筛选条件处理数据的逻辑
        # 需要从filters中获取year, quarter, month, category等参数
        # 返回处理后的数据
        return {"status": "success", "data": {}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"数据处理失败: {str(e)}")

@app.get("/api/health")
async def health_check():
    """健康检查端点"""
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)