from datetime import datetime

def Overlap(time_range1, time_range2):
    start_time1 = datetime.strptime(time_range1[0], '%Y-%m-%d %H:%M:%S')
    end_time1 = datetime.strptime(time_range1[1], '%Y-%m-%d %H:%M:%S')

    start_time2 = datetime.strptime(time_range2[0], '%Y-%m-%d %H:%M:%S')
    end_time2 = datetime.strptime(time_range2[1], '%Y-%m-%d %H:%M:%S')

    # เชคเวลาoverlab
    if start_time1 <= end_time2 and start_time2 <= end_time1:
        return True
    else:
        return False

test_cases = [
    (('2019-04-09 01:00:00', '2019-04-09 02:00:00'), ('2019-04-09 01:30:00', '2019-04-09 02:30:00')),
    (('2019-04-09 01:00:00', '2019-04-09 02:00:00'), ('2019-04-09 02:00:00', '2019-04-09 03:00:00')),
    (('2019-04-09 01:00:00', '2019-04-09 02:00:00'), ('2019-04-09 02:00:01', '2019-04-09 02:30:00')),
    (('2019-04-09 03:00:00', '2019-04-09 04:00:00'), ('2019-04-09 02:00:00', '2019-04-09 02:59:59')),
    (('0001-04-09 01:00:00', '0001-04-09 02:00:00'), ('0001-04-09 01:30:00', '0001-04-09 02:30:00'))
]

for case in test_cases:
    print(Overlap(case[0], case[1]))