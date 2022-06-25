import  requests
import json
# TODO: replace with your own app_id and app_key
app_id = 'a94c10fc'
app_key = '0452162a1caf0cc167ebf9897ad1e82a	'
language = 'en-gb'
# word_id = 'python'

def getDefinitions(word_id):
  url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
  r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}).json()
  
  if 'error' in r.keys():
    return False

  output={}
  definitions=[]
  senses=r['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
# print()
  for item in senses:
    definitions.append(f"👉{item['definitions'][0]}")
  output['definitions'] = "\n".join(definitions)
  
  if r['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
    output['audio']=r['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

  return output

if __name__=='__main__':
  from pprint import pprint as print
  print(getDefinitions('Great Britain'))
  print(getDefinitions('sdsdsdsds'))
