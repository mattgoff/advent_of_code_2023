test_time = [7, 15, 30]
test_dist =  [9, 40, 200]

q1_time = [47, 98, 66, 98]
q1_dist = [400, 1213, 1011, 1540]

test2_time = [71530]
test2_dist = [940200]

q2_time = [47986698]
q2_dist = [400121310111540]

total = []
for t, d in zip(q2_time, q2_dist):
    score = []
    for hold_time in range(t):
        test_distance = hold_time * (t - hold_time)
        if test_distance > d:
            score.append(test_distance)
    total.append(len(score))
print(total)

result = 1
for number in total:
    result *= number
print(result)