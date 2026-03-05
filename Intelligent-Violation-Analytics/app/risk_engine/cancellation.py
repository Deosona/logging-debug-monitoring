from app.config import CANCELLATION_THRESHOLD, WARNING_THRESHOLD

def evaluate_cancellation(score, patterns):

    if score >= CANCELLATION_THRESHOLD:
        return True, "Auto-cancelled: risk score exceeded threshold"

    if "Repeated high severity violations" in patterns:
        return True, "Auto-cancelled: repeated high severity violations"

    if score >= WARNING_THRESHOLD:
        return False, "Warning: Moderate risk detected"

    return False, "Safe"