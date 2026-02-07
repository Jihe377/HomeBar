# HomeBar - 家庭调酒配方管理软件

基于PRD中MVP内容构建的网页应用，用于管理个人酒柜、配方库和调酒记录。

## 功能特性

### MVP核心功能
1. **个人酒柜管理**：添加/编辑基酒与常用材料，设置存量
2. **配方库**：
   - 手动添加配方（支持从剪贴板快速识别）
   - 内置经典权威配方（IBA等）
   - 一键筛选"可制作配方"（基于现有库存）
3. **我的调酒记录**：
   - 记录某次调制使用的实际分量
   - 添加简单评价（如"太甜"、"完美"）和标签（如"夏日"、"烈"）

### 新增功能
- **购物清单**：基于想做的配方，自动列出缺失材料
- **口味偏好设置**：在初始设置时选择偏好

## 技术栈

### 前端
- React 18
- TypeScript
- Tailwind CSS
- Axios (HTTP客户端)
- React Router (路由)

### 后端
- Python 3.11+
- FastAPI
- SQLAlchemy (ORM)
- SQLite (开发环境)/PostgreSQL (生产环境)
- Pydantic (数据验证)

## 项目结构

```
HomeBar/
├── frontend/              # React前端应用
│   ├── public/
│   ├── src/
│   │   ├── components/    # React组件
│   │   ├── pages/        # 页面组件
│   │   ├── hooks/        # 自定义Hook
│   │   ├── services/     # API服务
│   │   ├── types/        # TypeScript类型定义
│   │   └── utils/        # 工具函数
│   ├── package.json
│   └── tailwind.config.js
├── backend/               # FastAPI后端服务
│   ├── app/
│   │   ├── api/          # 路由端点
│   │   ├── core/         # 核心配置
│   │   ├── db/           # 数据库相关
│   │   ├── models/       # 数据模型
│   │   ├── schemas/      # Pydantic模式
│   │   └── services/     # 业务逻辑
│   ├── requirements.txt
│   └── main.py
├── README.md
└── .gitignore
```

## 快速开始

### 环境要求
- Node.js 18+
- Python 3.11+
- Git

### 后端设置
```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 运行开发服务器
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 前端设置
```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 运行开发服务器
npm start
```

## API文档
启动后端服务后，访问以下地址：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 开发计划
- [ ] MVP核心功能实现
- [ ] 用户认证系统
- [ ] 数据持久化
- [ ] 响应式设计
- [ ] 测试覆盖
- [ ] 部署配置

## 许可证
MIT