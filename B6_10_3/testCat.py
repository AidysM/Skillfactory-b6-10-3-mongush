from cat import Cat, Wallet

c1 = Cat('Барон', 'мальчик', 2)
c2 = Cat('Сэм', 'мальчик', 2)
c3 = Cat('Придуманная', 'девочка', 3)

print("c1.getName=", c1.getName())
print("c1.getSex=", c1.getSex())
print("c1.getAge=", c1.getAge())

print("c2.getName=", c2.getName())
print("c2.getSex=", c2.getSex())
print("c2.getAge=", c2.getAge())

print("c3.getName=", c3.getName())
print("c3.getSex=", c3.getSex())
print("c3.getAge=", c3.getAge())

print("Клиенты")

client_1 = Wallet('Иван Петров', 50)
client_2 = Wallet('Петр Иванов', 100)

clients = [client_1, client_2]

for n in clients:
    print('Клиент "', n.client, '". Баланс: ', n.balanse, ' руб.')
