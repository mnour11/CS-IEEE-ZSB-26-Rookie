
X = int(input().strip()) 
weights = list(map(int, input().strip().split()))  
queries = []
while True:
    try:
        queries.append(int(input().strip()))
    except EOFError:
        break


attached = set()
current_weight = X


for q in queries:
    part_index = q - 1  
    if part_index in attached:
        current_weight -= weights[part_index]
        attached.remove(part_index)
    else:
        current_weight += weights[part_index]
        attached.add(part_index)
    print(current_weight)
