from app.config import SEVERITY_WEIGHTS

def calculate_score(violations):
    total_score = 0

    for v in violations:
        weight = SEVERITY_WEIGHTS.get(str(v.severity_level).lower(), 0)
        adjusted_score = weight * v.confidence_score
        total_score += adjusted_score

    return round(total_score, 2)