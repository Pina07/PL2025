def parse_csv(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    data = []
    current_row = []
    inside_quotes = False
    value = ''
    
    i = 0
    while i < len(content):
        char = content[i]
        
        if char == '"':
            if inside_quotes and i + 1 < len(content) and content[i + 1] == '"':
                value += '"'
                i += 1
            else:
                inside_quotes = not inside_quotes
        elif char == ';' and not inside_quotes:
            current_row.append(value.strip())
            value = ''
        elif char == '\n' and not inside_quotes:
            if value:
                current_row.append(value.strip())
                value = ''
            if current_row:
                data.append(current_row)
                current_row = []
        else:
            if char == '\n':
                value += ' '
            else:
                value += char
        
        i += 1
    
    if value:
        current_row.append(value.strip())
    if current_row:
        data.append(current_row)
    
    return data[1:]  # Skip the first row (header)

# Process the parsed data to create the required results
def process_data(data):
    composers = sorted(set(row[4] for row in data))
    period_distribution = {}
    period_titles = {}

    for row in data:
        period = row[3]
        title = row[0]
        
        if period not in period_distribution:
            period_distribution[period] = 0
        period_distribution[period] += 1
        
        if period not in period_titles:
            period_titles[period] = []
        period_titles[period].append(title)
    
    for period in period_titles:
        period_titles[period].sort()
    
    return composers, period_distribution, period_titles

# Example usage
file_path = 'obras.csv'
parsed_data = parse_csv(file_path)
composers, period_distribution, period_titles = process_data(parsed_data)

print("Compositores:")
print(composers)
print("\n\n\nDistribuição de Obras por Período")
print(period_distribution)
print("\n\n\nDicionário:")
print(period_titles)