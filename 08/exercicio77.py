lista = ('darlan', 'jose', 'notebook', 'monitor', 'teclado','mouse')
for l in lista:
    print(f"na palavra {l} temos: ")
    for v in l:
        if v in 'aeiou':
            print(v)