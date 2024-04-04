from fastapi import Request
from dependecy.logger import logger
import time




async def log_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start

    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "process_time": process_time,
        "host": request.client.host,
        "ip": request.client.host
    }
    logger.info(log_dict, extra=log_dict)

    return response