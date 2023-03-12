import pdb
pdb.set_trace()

def max_from_list(listas):
    return [max(lst) for lst in listas]
    
listas = [[1,3,5], [3,8,200]]
maximos = max_from_list(listas)
print(maximos)
