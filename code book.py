import re
with open('book.txt', 'r', encoding='utf-8') as file:
   onstring = file.read().split('\n')
   book = {}
   products = []
   for item in onstring:
       key = item.split('_')[0]
       value = item.split('_')[1:]
       products += value
       value = set(value)
       book[key] = value
products = set(products)

ingredients = []
def membership_test(user_lst):
   goods = []
   for ingredient in user_lst:
       if ingredient in products:
           goods += ingredient
       else:
           print(f'Извините, в нашей книге нет блюд с такими продуктами: "{ingredient}" :(')
   return goods


def meals():
   for k, v in book.items():
       if user_lst.intersection(v):
           ingred = str(user_lst.intersection(v))
           ingred = ingred.replace('{', '')
           ingred = ingred.replace('}', '')
           print(f'Вы можете приготовить "{k}", используя следующие продукты: ', ingred)
           addition = v - user_lst
           if addition:
               addition_lst = list(addition)
               print('Вам также понадобятся следующие ингредиенты:')
               print(', '.join(addition_lst), "\n")


print('Добро пожаловать! Здесь Вы найдете блюдо по вкусу! :)')
while True:
   user_input = input('Введите ингредиенты через запятую: ').lower().strip()
   user_input = re.sub(r'\s+', ' ', user_input)
   user_input = re.sub(r'\s*[,]\s*', ',', user_input).split(',')
   ingredients += user_input
   choice = input('Добавить еще продукты? ').lower().strip()
   if choice == 'нет':
       user_lst = set(ingredients)
       if membership_test(user_lst):
           meals()
       print('Спасибо что воспользовались нашей книгой!)')
       break
   elif choice != 'да':
       print('Ошибка! Начните сначала')
       break
