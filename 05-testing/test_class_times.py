# tests the file times.py for a different time range.
import times

def test_class_times():
    break_length = 10*60
    num_breaks = 2
    lecture_intervals = num_breaks + 1
    time_range_0 = times.time_range("2019-10-31 10:00:00",
                                    "2019-10-31 13:00:00")

    time_range_1 = times.time_range("2019-10-31 10:05:00",
                                    "2019-10-31 12:55:00",
                                    3,
                                    break_length)

    overlapppp = times.overlap_time(time_range_0, time_range_1)
    expected = [('2019-10-31 10:05:00', '2019-10-31 10:55:00'),
                 ('2019-10-31 11:05:00', '2019-10-31 11:55:00'),
                 ('2019-10-31 12:05:00', '2019-10-31 12:55:00')]
    print(expected)
    #assert overlapppp == expected
test_class_times()
