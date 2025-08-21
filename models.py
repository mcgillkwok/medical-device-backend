# backend/models.py
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UploadResponse(BaseModel):
    status: str
    message: str
    data: Optional[Dict[str, Any]] = None

class FilterRequest(BaseModel):
    year: Optional[int] = None
    quarter: Optional[str] = None
    month: Optional[str] = None
    category: Optional[str] = None
    time_granularity: str = "quarter"

class DataSummary(BaseModel):
    total_records: int
    approved_records: int
    approval_rate: float
    available_years: List[int]

class StatusStats(BaseModel):
    period: str
    counts: Dict[str, int]

class CategoryStats(BaseModel):
    period: str
    counts: Dict[str, int]

class InjuryStats(BaseModel):
    period: str
    counts: Dict[str, int]

class ReporterStats(BaseModel):
    reporter: str
    count: int
    percentage: float

class ProductStats(BaseModel):
    product: str
    count: int
    percentage: float

class ProcessedDataResponse(BaseModel):
    summary: DataSummary
    status_stats: List[StatusStats]
    category_stats: List[CategoryStats]
    injury_stats: List[InjuryStats]
    reporter_stats: List[ReporterStats]
    product_stats: Dict[str, List[ProductStats]]