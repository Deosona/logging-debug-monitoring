from datetime import datetime
from app.config import (
    BURST_TIME_WINDOW_SECONDS,
    BURST_COUNT_THRESHOLD,
    REPEAT_HIGH_VIOLATION_THRESHOLD
)

def detect_patterns(violations):
    suspicious_patterns = []

    if not violations:
        return suspicious_patterns

    # Convert timestamps
    timestamps = []
    for v in violations:
        try:
            timestamps.append(datetime.fromisoformat(v.timestamp))
        except Exception:
            continue

    timestamps.sort()

    # Burst detection
    for i in range(len(timestamps)):
        count = 1
        for j in range(i + 1, len(timestamps)):
            diff = (timestamps[j] - timestamps[i]).total_seconds()
            if diff <= BURST_TIME_WINDOW_SECONDS:
                count += 1

        if count >= BURST_COUNT_THRESHOLD:
            suspicious_patterns.append("Burst violations detected")
            break

    # Repeated high severity detection
    high_count = sum(
        1 for v in violations if str(v.severity_level).lower() == "high"
    )

    if high_count >= REPEAT_HIGH_VIOLATION_THRESHOLD:
        suspicious_patterns.append("Repeated high severity violations")

    return suspicious_patterns