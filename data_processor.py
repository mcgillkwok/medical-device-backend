# backend/data_processor.py
import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
        self.df = None
        
    def process(self):
        """处理上传的数据文件"""
        # 根据文件扩展名读取数据
        if self.file_name.lower().endswith('.csv'):
            self.df = pd.read_csv(self.file_path)
        elif self.file_name.lower().endswith(('.xlsx', '.xls')):
            self.df = pd.read_excel(self.file_path)
        else:
            raise ValueError("不支持的文件格式")
        
        # 数据清洗和处理
        self._clean_data()
        
        # 生成分析结果
        result = {
            "raw_data": self.df.to_dict(orient='records'),
            "summary": self._generate_summary(),
            "years": self._extract_years(),
            "status_stats": self._calculate_status_stats(),
            "category_stats": self._calculate_category_stats(),
            "injury_stats": self._calculate_injury_stats(),
            "reporter_stats": self._calculate_reporter_stats(),
            "product_stats": self._calculate_product_stats()
        }
        
        return result
    
    def _clean_data(self):
        """数据清洗"""
        # 处理日期字段
        if '报告日期' in self.df.columns:
            self.df['报告日期'] = pd.to_datetime(self.df['报告日期'], errors='coerce')
        
        # 处理空值
        self.df.fillna('', inplace=True)
    
    def _extract_years(self):
        """提取可用年份"""
        if '报告日期' in self.df.columns:
            years = pd.DatetimeIndex(self.df['报告日期']).year.unique()
            return sorted([int(year) for year in years if not pd.isna(year)])
        return []
    
    def _generate_summary(self):
        """生成数据摘要"""
        total_records = len(self.df)
        approved = len(self.df[self.df['经营企业使用单位报告状态'] == '审核通过'])
        
        return {
            "total_records": total_records,
            "approved_records": approved,
            "approval_rate": round(approved / total_records * 100, 2) if total_records > 0 else 0
        }
    
    def _calculate_status_stats(self):
        """计算状态统计"""
        # 实现状态统计逻辑
        pass
    
    def _calculate_category_stats(self):
        """计算产品类别统计"""
        # 实现产品类别统计逻辑
        pass
    
    def _calculate_injury_stats(self):
        """计算伤害类型统计"""
        # 实现伤害类型统计逻辑
        pass
    
    def _calculate_reporter_stats(self):
        """计算报告人统计"""
        # 实现报告人统计逻辑
        pass
    
    def _calculate_product_stats(self):
        """计算产品统计"""
        # 实现产品统计逻辑
        pass