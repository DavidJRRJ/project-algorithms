def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0
    for entry, exit in permanence_period:
        if not all(isinstance(time, int) for time in (entry, exit)):
            return None
        if entry <= target_time <= exit:
            count += 1

    return count
