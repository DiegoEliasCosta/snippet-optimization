import requests

answer_id = '18837389'

url = 'https://api.stackexchange.com/2.2/answers/'+answer_id+'?order=desc&sort=activity&site=stackoverflow&filter=withbody'

resp = requests.get(url)

print resp.json()['items'][0]['body']
	

