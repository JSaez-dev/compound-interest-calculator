def calculate_compound_interest(principal, rate, years):
    results = []
    for year in range(1, years + 1):
        amount = principal * (1 + rate) ** year
        results.append((year, round(amount, 2)))
    return results

def main():
    principal = float(input("Initial capital ($): "))
    rate = float(input("Annual interest rate (e.g. 0.09 for 9%): "))
    years = int(input("Number of years: "))

    print("\nGrowth projection:")
    print("-" * 30)
    for year, amount in calculate_compound_interest(principal, rate, years):
        print(f"Year {year}: ${amount}")

main()
