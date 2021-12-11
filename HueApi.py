from creds import user, url

endpoint = ["https://", url, "/api/", user]

class HueApi:

  def __init__(self):
    self.user = user
    self.url = url
    self.api = ''.join(endpoint)

  def get(self):
    return ''.join([self.api, "/lights/1"])

  def put(self, sat, bri, hue):
    args = { "on":"true", "sat": sat, "bri": bri, "hue": hue }
    return [''.join([self.api, '/lights/1/state']), args]

