from pprint import pprint
import requests
start_api_url="https://www.superheroapi.com/api/2619421814940190/"

def find_hero_id (heroes_list, start_api_url):
    dict_with_intelligence_of_heroes = {}
    for hero in heroes_list:
        # print(hero)
        url = start_api_url + 'search/' + hero
        response = requests.get(url)
        # print(url)
        # print(response)
        # pprint(response.json())
        #все содержимое ключа results:
        results = response.json()['results']
        # pprint(results)
        for list_of_possible_heroes in results:
           if list_of_possible_heroes['name'] == hero:
               # print(f""" {list_of_possible_heroes['name']} - этот герой - правильный""")
               powerstats_dict = {}
               powerstats_dict = list_of_possible_heroes['powerstats']
               # print(list_of_possible_heroes['powerstats'])
               hero_intelligence = int(powerstats_dict['intelligence'])
               # print(f"Это интеллект героя {hero} - {hero_intelligence}")
        dict_with_intelligence_of_heroes[hero] = hero_intelligence
    return dict_with_intelligence_of_heroes

dict_with_intelligence_of_heroes = find_hero_id(['Hulk', 'Captain America', 'Thanos'], start_api_url)
print(dict_with_intelligence_of_heroes.items())

def most_intelligent (dict_for_sorting_heroes_intelligence):
    values_list = dict_with_intelligence_of_heroes.values()
    print(values_list)
    max_intellect = max(values_list)
    for hero, intellect in dict_for_sorting_heroes_intelligence.items():
        if intellect == max_intellect:
            print(f"Самый умный супергерой - это {hero}, с интеллектом в {intellect}")

most_intelligent(dict_with_intelligence_of_heroes)

    # for key, value in dict_with_intelligence_of_heroes.items():

# print(response.status_code)
# print(response.text)
#
#
# print(f" Это класс переменной <responce_class> {response_class}")
# print(f" Это - содержимое переменное RESPONSE {response}")
# print(f" Это - содержимое метода STATUS.CODE примененного к {response.status_code}")