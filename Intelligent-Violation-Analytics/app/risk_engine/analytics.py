def severity_distribution(violations):

    distribution = {
        "low": 0,
        "medium": 0,
        "high": 0
    }

    for v in violations:
        level = str(v.severity_level).lower()
        if level in distribution:
            distribution[level] += 1

    return distribution