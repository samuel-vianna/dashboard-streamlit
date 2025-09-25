def calculate_nps(summary: dict) -> float:
    total = summary.get("total", 1)  
    positive = summary.get("positive", 0)
    negative = summary.get("negative", 0)
    
    if total == 0:
        return 0    

    nps_score = ((positive / total) - (negative / total)) * 100
    return round(nps_score, 2)
