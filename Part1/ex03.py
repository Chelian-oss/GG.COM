# Create original string without using quotes
string1 = str(" ".join(["Chelian", "is", "18", "year", "old", "boy"]))

# Convert to lowercase
string_lower = string1.lower()

# Convert to uppercase
string_upper = string1.upper()

# Remove spaces
string_nospace = string1.replace(" ", "")

# Print results
print(string1)
print(string_lower)
print(string_upper)
print(string_nospace)

print(string_nospace)