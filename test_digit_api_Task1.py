import json
import requests

first_names = []
multi_api_calls = []
person_details = {'firstNames': []}

####################################################################################################################################################################
# SOMETIME, GETTING BELOW ERROR WHICH I CANNOT FIGURE OUT SO IF YOU GET THE BELOW ERROR MESSAGE, TRY RUNNING IT AGAIN
# ON RE-TRYING, IT GIVE SUCCESS MESSAGE IN CONSOLE AND FILE OUTPUT
####################################################################################################################################################################

# Traceback (most recent call last):
#   File "/Users/dchowbey/PycharmProjects/DigitChallenge_API/test_digit_api_Task1.py", line 48, in <module>
#     person_details_sorted = sorted(z, key=lambda k: k["age"])
# TypeError: '<' not supported between instances of 'int' and 'NoneType'


for i in range(5):
    response = requests.get("https://randomuser.me/api/")
    # print(type(response.text))
    # print(response.text)
    response_data = json.loads(response.text)
    # print(response_data['results'][0]['name']['first'])
    temp = response_data['results'][0]['name']['first']
    first_names.append(response_data['results'][0]['name']['first'])
    temp_response1 = requests.get("https://api.agify.io/?name=" + temp)
    temp_response2 = requests.get("https://api.genderize.io/?name=" + temp)
    temp_response3 = requests.get("https://api.nationalize.io/?name=" + temp)

    name = json.loads(temp_response1.text)['name']
    age = json.loads(temp_response1.text)['age']
    age_count = json.loads(temp_response1.text)['count']

    gender = json.loads(temp_response2.text)['gender']
    probability = json.loads(temp_response2.text)['probability']
    gender_count = json.loads(temp_response2.text)['count']

    country = json.loads(temp_response3.text)['country']

    person_details['firstNames'].append({
        # "ageAPI": json.loads(temp_response1.text),
        # "genderAPI": json.loads(temp_response2.text),
        # "nationalityAPI": json.loads(temp_response3.text)

        "name": name,
        "age": age,
        "age_count": age_count,
        "gender": gender,
        "probability": probability,
        "gender_count": gender_count,
        "country": country

    })

y = json.loads(json.dumps(person_details))
z = y['firstNames']

person_details_sorted = sorted(z, key=lambda k: k["age"])

# Printing to sorted data on Console
print(json.dumps(person_details_sorted, indent=2))

# Storing the data in a JSON file with name
with open('person_details_sorted.json', 'w') as outfile:
    json.dump(person_details_sorted, outfile, indent=4, sort_keys=True)






