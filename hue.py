import requests as r, json, time, random as rand

from HueApi import HueApi

Hapi = HueApi()

resp = json.loads(r.get(Hapi.get(), verify=False).text)

for n in range(10):
  cmd = Hapi.put(rand.randrange(254), rand.randrange(254), rand.randrange(65534))
  res = r.put(cmd[0], json=cmd[1], verify=False)
  time.sleep(3)