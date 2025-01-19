# Example of an applicant's characteristics
credit_score = 750
annual_income = 60000
has_collateral = True
has_existing_loan = False

# This criterion should be True if the applicant's annual income is at least $50,000 or they have collateral
income_criterion = (annual_income >= 50000 or has_collateral)

# Decision: check if all of the criteria are satisfied
is_approved = ((credit_score > 700) or income_criterion and not has_existing_loan)
print(is_approved)