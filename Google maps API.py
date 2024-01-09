import requests
class Test_new_location():
    '''Работа с новой локацией'''


    def test_create_new_location(self):
        '''Создание новой локации'''
        base_url = 'https://rahulshettyacademy.com'
        key = '?key=qaclick123'
        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result_post = requests.post(post_url, json = json_for_create_new_location)
        print(result_post.text)
        print('статус код: ' + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print('Успешно! Создана новая локация')
        else:
            print('Провал!')
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print('Статус код ответа: ' + check_info_post)
        assert check_info_post == 'OK'
        print('Статус ответа верный')
        place_id = check_post.get('place_id')
        print('Статус код ответа: ' + place_id)
        print(result_post.text)
        place = open('post.txt', 'a')
        place.write(place_id)
        place.write('\n')
        place.close()

        get_resource = '/maps/api/place/get/json'
        place = open('post.txt', 'r')
        lines = place.readlines()
        print(lines)
        print(len(lines))
        for line in lines:
            print(line)
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print('статус код: ' + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print('Успешно! Проверка новой локации успешна')
        else:
            print('Провал! Ошибочный запрос локации')


for i in range(5):
        new_place = Test_new_location()
        new_place.test_create_new_location()