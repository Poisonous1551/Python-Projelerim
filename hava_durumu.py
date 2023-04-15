import requests

sehir=input('Bir şehir giriniz: ')

url=f'https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid=5c6abc4e297095f06d6e90592ba8a431&units=metric&lang=tr'

response=requests.get(url)
veriler=response.json()

hava_durumu=veriler['weather'][0]['description'] if 'weather' in veriler else 'Bilinmiyor'
sicaklik=veriler['main']['temp'] if 'main' in veriler else 'Bilinmiyor'
nem=veriler['main']['humidity'] if 'main' in veriler else 'Bilinmiyor'

print('{} Şehrinin Hava Durumu : {}'.format(sehir,hava_durumu))
print('Nem orani: %{}'.format(nem))
print('Sicakliği:{} ℃'.format(sicaklik))