from fastapi import FastAPI
import time

from app.logger import log_info, log_error, log_performance
from app.monitoring import get_system_metrics
from app.schemas import LogMessage

app = FastAPI(
    title="Standalone Logging & Debug Monitoring System",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {"status": "Debug Monitoring System Running"}


@app.post("/log")
def create_log(log: LogMessage):
    if log.level.lower() == "error":
        log_error("User Log", log.message)
    else:
        log_info("User Log", log.message)

    return {"status": "Log recorded"}


@app.get("/metrics")
def system_metrics():
    return get_system_metrics()


@app.get("/simulate-performance")
def simulate_performance():
    start_time = time.time()

    time.sleep(1)  # simulate heavy task

    log_performance("simulate_performance", start_time)

    return {"message": "Performance logged"}
