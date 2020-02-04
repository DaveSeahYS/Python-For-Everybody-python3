def computepay(h, r):
    if h < 0 or r < 0:  # ensure none negatives
        return None
    elif h > 40:  # Calculations for overtime
        return (40 * r + (h - 40) * 1.5 * r)
    else:  # No overtime
        return (h * r)


try:  # Code to run if numerical value
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("please input your rate:")
    r = float(rate)
    p = computepay(h, r)
    print(p)
except:
    print("Please input a value")