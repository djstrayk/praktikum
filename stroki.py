def check_query(query):
    request =  (query.split())
    if request[0] == 'Анфиса,': return 'запрос к Анфисе'
    else: return 'запрос к кому-то ещё'

# дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '-', result)
