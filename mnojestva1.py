def print_shopping_list(pizza, salad): # напишите здесь свою функцию
    pizza_set, salad_set =  set (pizza), set (salad)
    shopping_list= pizza_set.union(salad_set)
    print (','.join(shopping_list))

pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)
