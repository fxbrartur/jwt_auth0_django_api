import http.client


conn = http.client.HTTPSConnection("dev-352za0lu0zfx5z5w.us.auth0.com")

payload = "{\"client_id\":\"uAuZlnLhKLunye1xaGV6rxVz3hes1QNX\",\"client_secret\":\"3pkodZ0HRUq2stpaEzCIpUdpJf4vRJScONtUyNo60wulvMcoIPSn6b0TWkM2CX2Q\",\"audience\":\"https://assessment/api\",\"grant_type\":\"client_credentials\"}"

headers = {'content-type': "application/json"}

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
