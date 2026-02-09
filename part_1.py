sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
total_sample = len(sample_bay)

print(sample_bay[0])
print(sample_bay[total_sample-1])
print(f"Total number of sample is {total_sample}")

for sample in sample_bay:
    print(f"Transmitting data for: {sample}")

new_findings = []

new_sample_number = int(input("How many new finding: "))

for i in range(new_sample_number):
    finding_item = input(f"Enter item number {i+1} name: ").title()
    new_findings.append(finding_item)

print(new_findings)

if "Dust" in sample_bay:
    sample_bay.remove("Dust")
else:
    pass

print(sample_bay)
