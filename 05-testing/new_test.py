# tests times.py for a new time range.
import times
import datetime
import pdb
def in_seconds(time_range, units):
    """ Converts a variable to seconds.
        units is a string - either "minutes", "hours", "days",
        "weeks" or years" to specify units of the given time range."""

    def minutes(time_range):
        return time_range * 60
    def hours(time_range):
        return time_range *60*60
    def days(time_range):
        return time_range*60*60*24
    def weeks(time_range):
        return time_range*60*60*24*7
    def years(time_range):
        return time_range*60*60*24*365.25

    units_dict = {
        "minutes": minutes,
        "hours": hours,
        "days": days,
        "weeks": weeks,
        "years": years
    }

    assert units in units_dict
    conversion = units_dict.get(units)
    return conversion(time_range)

def test_multiple_ranges():

    gap_length_A = in_seconds(10, "minutes")
    gap_length_B = in_seconds(35, "minutes")

    time_range_A = times.time_range("2019-10-31 00:00:00",
                                   "2019-10-31 23:50:00",
                                   24,
                                   gap_length_A)

    time_range_B = times.time_range("2019-10-31 00:30:00",
                                   "2019-10-31 23:55:00",
                                   24,
                                   gap_length_B)

    overlap = times.overlap_time(time_range_A, time_range_B)

    assert all([(datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S") -
    datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")).total_seconds() ==
    in_seconds(20, "minutes")
    for t0, t1 in overlap])
    print(all([(datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S") -
    datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")).total_seconds() ==
    in_seconds(20, "minutes")
    for t0, t1 in overlap]))

test_multiple_ranges()
