import datetime

def time_range(time0, time1, n=1, g=0):
    # transform input times to the right format and to strings
    time0_string = datetime.datetime.strptime(time0, "%Y-%m-%d %H:%M:%S")
    time1_string = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")

    # find the time in seconds between the dates
    d = (time1_string - time0_string).total_seconds() / n + g * (1/n - 1)
    sec_range = [(time0_string + datetime.timedelta(seconds=i * d + i * g),
                  time0_string + datetime.timedelta(seconds=(i + 1) * d + i * g)
                  ) for i in range(n)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")
            ) for ta, tb in sec_range]


def overlap_time(observation1, observation2):
    overlap_time_array = []
    for time_range0, time_range1 in observation1:
        for time_range_a, time_range_b in observation2:
            low = max(time_range0, time_range_a)
            high = min(time_range1, time_range_b)
            overlap_time_array.append((low, high))
    return overlap_time_array


if __name__ == "__main__":
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    print(overlap_time(large, short))
