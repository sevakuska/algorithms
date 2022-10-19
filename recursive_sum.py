def recursive_sum(lterable):
    if not lterable:
        return 0
    return lterable[0] + recursive_sum(lterable[1:])
