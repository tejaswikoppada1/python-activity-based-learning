# Campus Event Financial Planning

# Fixed costs
venue = 15000
equipment = 10000
transport = 8000
certificates = 2000

# Cost per participant
catering_per_person = 250

# Event details
participants = 100
registration_fee = 500
sponsorship = 20000

# Calculate fixed cost
fixed_cost = venue + equipment + transport + certificates

# Calculate catering cost
catering = catering_per_person * participants

# Calculate total event cost
total_cost = fixed_cost + catering

# Calculate participant contribution
participant_contribution = registration_fee * participants

# Calculate total available funds
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = total_cost - total_funds

# Calculate minimum registrations needed to break even
amount_needed_from_registrations = total_cost - sponsorship

if amount_needed_from_registrations > 0:
    minimum_registrations = (
        amount_needed_from_registrations + registration_fee - 1
    ) // registration_fee
else:
    minimum_registrations = 0

print("CAMPUS EVENT FINANCIAL PLAN")
print("----------------------------")

print("Venue Cost: Rs.", venue)
print("Equipment Cost: Rs.", equipment)
print("Catering Cost: Rs.", catering)
print("Transport Cost: Rs.", transport)
print("Certificate Cost: Rs.", certificates)

print("\nTotal Event Cost: Rs.", total_cost)
print("Participant Contribution: Rs.", participant_contribution)
print("Sponsorship: Rs.", sponsorship)
print("Total Available Funds: Rs.", total_funds)

if shortfall > 0:
    print("Sponsorship/Registration Shortfall: Rs.", shortfall)
else:
    print("Surplus: Rs.", abs(shortfall))

print("Minimum Registrations Needed to Break Even:",
      minimum_registrations)