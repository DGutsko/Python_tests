import json

import requests

class Test_Star_Wars():
    '''Полчучение персонажей'''

    def receive_films(self):
        get_url_1 = 'https://swapi.dev/api/people/4/'
        result = requests.get(get_url_1)
        print('статус код: ' + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Успешно')
        else:
            print('Провал!')
        result.encoding = 'utf-8'
        print(result.text)
        data = json.loads(result.text)
        film_number = data['films']
        print(film_number)
        people = []
        for line in film_number:
            people.append(line.replace('\n', ' '))

        for i in range(len(people)):
            get_url = people[i]
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print('статус код: ' + str(result_get.status_code))
            print(result_get.text)
            data = json.loads(result_get.text)
            people_number = data['characters']
            print(people_number)
            character = open('people.txt', 'a')
            for people_id in people_number:
                character.write(people_id)
                character.write('\n')
            character.close()
        names_of_people = [line.rstrip('\n') for line in open('people.txt')]
        print(names_of_people)

        names = []
        for line in names_of_people:
            names.append(line.replace('\n', ' '))

        for i in range(len(names)):
            get_url = names[i]
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print('статус код: ' + str(result_get.status_code))
            print(result_get.text)
            data = json.loads(result_get.text)
            name_number = data['name']
            print(name_number)
            name_people = [name_number]
            print(name_people)
            name = open('names.txt', 'a', encoding='utf-8')
            for name_id in name_people:
                name.write(name_id)
                name.write('\n')
            name.close()

        names_final = [line.rstrip('\n') for line in open('names.txt')]
        print(names_final)
        res = [*set(names_final)]
        print(res)
        fin_name = open('names2.txt', 'a', encoding='utf-8')
        for f_name in res:
            fin_name.write(f_name)
            fin_name.write('\n')
        fin_name.close()



films = Test_Star_Wars()
films.receive_films()