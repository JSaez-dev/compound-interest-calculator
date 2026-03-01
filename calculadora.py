def calculate_compound_interest(principal, rate, years, monthly_contribution=0):
    results = []
    total_invested = principal

    for year in range(1, years + 1):
        if monthly_contribution > 0:
            for month in range(12):
                principal = (principal + monthly_contribution) * (1 + rate / 12)
            total_invested += monthly_contribution * 12
        else:
            principal = principal * (1 + rate)

        interest_earned = principal - total_invested
        results.append({
            "year": year,
            "amount": round(principal, 2),
            "total_invested": round(total_invested, 2),
            "interest_earned": round(interest_earned, 2)
        })

    return results


def print_summary(results, initial_principal):
    print("\nYear-by-year breakdown:")
    print("-" * 55)
    print(f"{'Year':<6} {'Balance':>12} {'Invested':>12} {'Interest':>12}")
    print("-" * 55)

    for r in results:
        print(f"{r['year']:<6} ${r['amount']:>11} ${r['total_invested']:>11} ${r['interest_earned']:>11}")

    final = results[-1]
    print("-" * 55)
    print(f"\nSummary:")
    print(f"  Total invested:      ${final['total_invested']}")
    print(f"  Final balance:       ${final['amount']}")
    print(f"  Total interest:      ${final['interest_earned']}")


def main():
    print("=== Compound Interest Calculator ===\n")
    principal = float(input("Initial capital ($): "))
    rate = float(input("Annual interest rate (e.g. 0.09 for 9%): "))
    years = int(input("Number of years: "))
    monthly = float(input("Monthly contribution ($) (0 if none): "))

    results = calculate_compound_interest(principal, rate, years, monthly)
    print_summary(results, principal)


main()
