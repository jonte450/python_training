def com(principal, rate, years):
    future_value = principal * (1+(0.01*rate)) ** years
    return future_value


print(round(com(10000,3.5,7)))
