def healthCheck (age, apples, booze):
    health = (100-age) + (apples * 3.5) - (booze * 2)
    print("Your Health States", health)

vijay_data = [26, 20, 0]
healthCheck(vijay_data[0], vijay_data[1], vijay_data[2])
healthCheck(*vijay_data)