import asyncio
import cv2
from PIL import Image
from pathlib import Path
from random import randrange

# CAN ALSO REMOVE ASYNC here and controller, that will speed up the process for some reason
def blocking_io(channel):
    X = cv2.imread(f"./pics/{channel}.png")   # reads an image in the BGR format
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # BGR -> RGB
    img = Image.fromarray(X)

    img.save(f"./output/test{channel}.jpg")
    data = Path(f"./output/test{channel}.jpg").read_bytes()
    return data


async def blocking_io_slower(channel):
    
    i = randrange(5)
    print(i)
    await asyncio.sleep(i)
    
    X = cv2.imread(f"./pics/{channel}.png")   # reads an image in the BGR format
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # BGR -> RGB
    img = Image.fromarray(X)

    img.save(f"./output/test{channel}.jpg")
    data = Path(f"./output/test{channel}.jpg").read_bytes()
    return data

    
    