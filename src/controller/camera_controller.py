import asyncio
from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Response

from src.services.camera import blocking_io, blocking_io_byteio, blocking_io_byteio_nok, blocking_io_slower


cameras_router = APIRouter(
    prefix="/cameras",
    tags=["cameras"]
)



@cameras_router.get("/BOF/{channel}")
async def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    await asyncio.sleep(1)
    byte_arr = await blocking_io_byteio_nok(channel)

    
    return Response(content=byte_arr, status_code=HTTPStatus.OK,media_type="image/png")


@cameras_router.get("/{channel}")
def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    byte_arr = blocking_io_byteio(channel)

    
    return Response(content=byte_arr, status_code=HTTPStatus.OK,media_type="image/png")


@cameras_router.get("/NICEbutSLOW/{channel}")
async def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    byte_arr = await blocking_io_byteio_nok(channel)

    
    return Response(content=byte_arr, status_code=HTTPStatus.OK,media_type="image/png")



@cameras_router.get("/NICE/{channel}")
def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    byte_arr = blocking_io_byteio(channel)

    
    return Response(content=byte_arr, status_code=HTTPStatus.OK,media_type="image/png")




@cameras_router.get("/good/{channel}")
def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    blocking_io(channel)
    
    return {"status": "ok", "description": f"Camera #{channel} success"}




@cameras_router.get("/SLOWED/{channel}")
async def capture(channel):
    if channel == 999:
        raise HTTPException(status_code=400, status="ko", description="Camera not found")
    
    # don't use async / await useless ( that slow the process, just let the thread take it)
    await blocking_io_slower(channel)
    
    return {"status": "ok", "description": f"Camera #{channel} success"}

