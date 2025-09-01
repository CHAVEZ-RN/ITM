import math

def savings(gross_pay, tax_rate, expenses):
    '''Savings.'''
    # Step 1: Calculate tax amount and subtract from gross pay (round down)
    after_tax = math.floor(gross_pay * (1 - tax_rate))
    
    # Step 2: Subtract expenses
    remaining = after_tax - expenses
    
    return remaining


def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.'''
    # Step 1: Total material consumed
    consumed = num_jobs * job_consumption
    
    # Step 2: Remaining waste
    waste = total_material - consumed
    
    # Step 3: Return formatted string
    return f"{waste}{material_units}"


def interest(principal, rate, periods):
    '''Interest.'''
    # Step 1: Calculate interest
    interest_amount = principal * rate * periods
    
    # Step 2: Add to principal
    final_value = principal + interest_amount
    
    # Step 3: Round down final value
    return math.floor(final_value)
