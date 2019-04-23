import requests

var = input('შეიყვანეთ ადგილმდებარეობის სახელი ან კოორდინატები, მაგ: \'41.1243, 42.141\':')


url = f'https://maps.googleapis.com/maps/api/geocode/json?address={var}&key=AIzaSyBQs3__s41n6DzOfVq-z7G5jlYxbPShEOY'

r = requests.get(url=url)

try:
    if var.isalpha():
        coordinate1 = str(r.json()['results'][0]['geometry']['bounds']['northeast']['lat']) \
                    + ' ' + str(r.json()['results'][0]['geometry']['bounds']['northeast']['lng'])
        coordinate2 = str(r.json()['results'][0]['geometry']['bounds']['southwest']['lat']) \
                    + ' ' + str(r.json()['results'][0]['geometry']['bounds']['northeast']['lng'])
        print('Northeast:', coordinate1, 'Southwest:', coordinate2)
    else:
        place = r.json()['results'][0]['address_components'][0]['long_name']
        print(place)
except IndexError:
    print('მითითებული ადგილმდებარეობა არ მოიძებნა')
