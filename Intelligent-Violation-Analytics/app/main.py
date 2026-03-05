from fastapi import FastAPI
from app.risk_engine.models import ViolationLog
from app.risk_engine.scoring import calculate_score
from app.risk_engine.patterns import detect_patterns
from app.risk_engine.cancellation import evaluate_cancellation
from app.risk_engine.analytics import severity_distribution

app = FastAPI()

@app.post("/risk/analyze")
def analyze_risk(violations: list[ViolationLog]):

    score = calculate_score(violations)
    patterns = detect_patterns(violations)
    cancelled, reason = evaluate_cancellation(score, patterns)

    # Risk Category
    if score <= 5:
        category = "Low"
    elif score <= 10:
        category = "Medium"
    else:
        category = "High"

    return {
        "score": score,
        "category": category,
        "cancelled": cancelled,
        "reason": reason,
        "suspicious_patterns": patterns,
        "severity_distribution": severity_distribution(violations)
    }

# Temporary in-memory storage (for simulation)
violation_store = []

@app.post("/risk/analyze")
def analyze_risk(violations: list[ViolationLog]):

    violation_store.extend(violations)

    score = calculate_score(violations)
    patterns = detect_patterns(violations)
    cancelled, reason = evaluate_cancellation(score, patterns)

    if score <= 5:
        category = "Low"
    elif score <= 10:
        category = "Medium"
    else:
        category = "High"

    return {
        "score": score,
        "category": category,
        "cancelled": cancelled,
        "reason": reason,
        "suspicious_patterns": patterns,
        "severity_distribution": severity_distribution(violations)
    }


@app.get("/admin/summary")
def admin_summary():
    if not violation_store:
        return {"message": "No data available"}

    score = calculate_score(violation_store)
    patterns = detect_patterns(violation_store)
    cancelled, reason = evaluate_cancellation(score, patterns)

    return {
        "total_violations": len(violation_store),
        "overall_score": score,
        "patterns_detected": patterns,
        "cancellation_status": cancelled,
        "reason": reason
    }


@app.get("/admin/timeline")
def violation_timeline():
    return sorted(
        violation_store,
        key=lambda x: x.timestamp
    )


@app.get("/admin/severity-distribution")
def admin_severity_distribution():
    return severity_distribution(violation_store)