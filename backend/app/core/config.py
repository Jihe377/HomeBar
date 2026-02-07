from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    # 项目配置
    PROJECT_NAME: str = "HomeBar API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # 安全配置
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7天
    
    # CORS配置
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # 前端开发服务器
        "http://127.0.0.1:3000",
    ]
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./homebar.db"
    # 生产环境使用PostgreSQL
    # DATABASE_URL: str = "postgresql://user:password@localhost/homebar"
    
    # 调试模式
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()