crew_details={
              "Pilot":"Kumar",
              "Co-pilot":"Raghav",
              "Head-Stewardess":"Malini",
              "Stewardess":"Mala"
              }

pilot = crew_details.get("Pilot")
print(pilot)
crew_details.update({"Pilot": "Ahmed"})
pilot = crew_details.get("Pilot")
print(pilot)

crew_details.update({"Security": "Ali"})

print(crew_details)
