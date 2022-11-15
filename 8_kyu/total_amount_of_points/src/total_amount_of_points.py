def points(games):
    
    result = 0
    
    for match in games:
        if match [0] > match[2]:
            result += 3
        if match [0] < match[2]:
            continue
        if match [0] == match[2]:
            result += 1
    
    return result