content = ""

with open('0022_names.txt', 'r') as file:
    content = sorted(file.read().replace("\"", "").split(","))

soma = 0
for i, name in enumerate(content):
    soma += sum((ord(c) - 64) for c in name) * (i + 1)

print(soma)

# evil one liner expression
print(sum(sum((ord(c) - 64) for c in name) * (i + 1) for i, name in enumerate(content)))




