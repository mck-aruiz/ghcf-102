def equated_monthly_installments(principal, rate_per_annum, years_to_repay):
    """
    Calculates the equated monthly installments (EMI) for a loan.

    Args:
        principal (float): The principal amount borrowed.
        rate_per_annum (float): The rate of interest per annum.
        years_to_repay (int): The number of years to repay the loan.

    Returns:
        float: The equated monthly installment amount.

    Raises:
        Exception: If the principal is less than or equal to 0.
        Exception: If the rate of interest is less than 0.
        Exception: If the years to repay is less than or equal to 0 or not an integer.
    """
    if principal <= 0:
        raise Exception("Principal borrowed must be > 0")
    if rate_per_annum < 0:
        raise Exception("Rate of interest must be >= 0")
    if years_to_repay <= 0 or not isinstance(years_to_repay, int):
        raise Exception("Years to repay must be an integer > 0")

    # Yearly rate is divided by 12 to get monthly rate
    rate_per_month = rate_per_annum / 12 / 100

    # Years to repay is multiplied by 12 to get number of payments as payment is monthly
    number_of_payments = years_to_repay * 12

    # Calculate amortization
    amortization = (
        principal
        * rate_per_month
        * (1 + rate_per_month) ** number_of_payments
        / ((1 + rate_per_month) ** number_of_payments - 1)
    )

    return amortization
