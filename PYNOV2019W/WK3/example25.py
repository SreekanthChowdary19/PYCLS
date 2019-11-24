# Returning a multiple values from the function


# WAP get sum and avg of given list


def get_sum_avg(x):
    s = 0
    for e in x:
        s = s+e
    return s, s/len(x)



total, avg = get_sum_avg([10, 20, 30, 40, 50])
print("Total", total)
print("Avg", avg)



output = get_sum_avg([100, 200, 300, 400, 500])
print("Total", output[0])
print("Avg", output[1])
