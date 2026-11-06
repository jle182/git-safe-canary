import requests, pickle
r = requests.post(url, data=payload, verify=False)
obj = pickle.loads(blob)
