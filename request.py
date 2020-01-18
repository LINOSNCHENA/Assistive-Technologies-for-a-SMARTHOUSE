import requests
url = 'http://localhost:5000/results'
fever_now = requests.post(url,json = {'feat1':52,'feat2':20, 'feat3':42 'feat4':23, 
                                      'feat5':42,'feat6':41,'feat7':44,'feat8':47})
print(fever_now.json())

