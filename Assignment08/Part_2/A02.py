age = int(input("Enter Age: "))
severity = input("Enter Severity (critical/moderate/low): ").lower()
insurance = input("Insurance (yes/no): ").lower()

if severity == "critical":
    if age >= 60:
        print("Treatment = Immediate ICU")
    else:
        print("Treatment = Emergency Ward")

elif severity == "moderate":
    if insurance == "yes":
        print("Treatment = Priority Treatment")
    else:
        print("Treatment = General Queue")

elif severity == "low":
    if age < 10:
        print("Treatment = Pediatric Priority")
    else:
        print("Treatment = Wait")