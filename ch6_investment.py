
def invest(amount, rate, years):
    for year in range(years):
        amount = (amount * rate) + amount
        print(round(amount, 2))


input_amount = input("Enter the amount: ")
input_rate = input("Enter the rate: ")
input_years = input("Enter the years: ")

invest(float(input_amount), float(input_rate), int(input_years))

