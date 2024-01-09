import requests
import json


class Test_new_joke():
    '''Создание шуток по каждой категории'''

    def __init__(self):
        pass

    def receive_category(self):
        '''Получение всех категорий'''
        url = 'https://api.chucknorris.io/jokes/categories'
        print(url)
        result = requests.get(url)
        print('статус код: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно')
        else:
            print('Провал!')
        result.encoding = 'utf-8'
        print(result.text)

        category_list = result.text.replace('\"', '').replace('[', '').replace(']', '').split(',')
        # print(category_list[0])

        return category_list

    def test_create_category_joke(self, category):
        '''Создание шуток по каждой категории'''
        url = 'https://api.chucknorris.io/jokes/random?category=' + category
        print(url)
        result = requests.get(url)
        print('Статус код: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно!')
        else:
            print('Провал!')
        result.encoding = 'utf-8'
        json_obj = json.loads(result.text)

        return json_obj['value']
        check = result.json()
        check_info = check.get('categories')
        print(check_info)


all_categories = Test_new_joke()
all_categories.receive_category()

categories = all_categories.receive_category()
for i in range(len(categories)):
    print(all_categories.test_create_category_joke(categories[i]))