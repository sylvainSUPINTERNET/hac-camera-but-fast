from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from src.services.camera import blocking_io
from src.controller.camera_controller import cameras_router


if __name__ == '__main__':
    app = FastAPI()
    
    # Default config ..., TODO : add some security ofc
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    
    app.include_router(cameras_router)
    uvicorn.run(app, host='0.0.0.0', port=8001)