def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for start, end in permanence_period:
            if start <= target_time <= end:
                count += 1
    except TypeError:
        return None
    return count
