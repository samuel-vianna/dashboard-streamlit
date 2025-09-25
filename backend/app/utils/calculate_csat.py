def calculate_csat(summary: dict) -> float:
    total = summary.get("total", 1) 
    positive = summary.get("positive", 0) 

    if total == 0:
        return 0

    csat_score = (positive / total) * 100
    return round(csat_score, 2)
