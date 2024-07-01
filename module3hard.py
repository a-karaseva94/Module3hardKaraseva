from experience import vibor

def calculate_structure_sum(param):
  sum_all = []
  for i in range(len(param)):
    if isinstance(param[i], list):
        for j in param[i]:
            dlina = sum(vibor(j))
            sum_all.append(dlina)

    elif isinstance(param[i], dict):
        for keys in param[i].keys():
            dlina1 = sum(vibor(keys))
            sum_all.append(dlina1)
        for values in param[i].values():
            dlina2 = sum(vibor(values))
            sum_all.append(dlina2)

    elif isinstance(param[i], int) or isinstance(param[i], str):
        dlina = sum(vibor(param[i]))
        sum_all.append(dlina)

    elif isinstance(param[i], tuple):
        for j in range(len(param[i])):
            if isinstance(param[i][j], int) or isinstance(param[i][j], str):
                dlina = sum(vibor(param[i][j]))
                sum_all.append(dlina)
            elif isinstance(param[i][j], list):
                for k in param[i][j]:
                    dlina = sum(vibor(k))
                    sum_all.append(dlina)
            elif isinstance(param[i][j], dict):
                for keys in param[i][j].keys():
                    dlina1 = sum(vibor(keys))
                    sum_all.append(dlina1)
                for values in param[i][j].values():
                    dlina2 = sum(vibor(values))
                    sum_all.append(dlina2)


  result = sum(sum_all)
  return result


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)