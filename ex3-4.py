from http.client import HTTPConnection

# 1.연결
connection = HTTPConnection('www.example.com')

# 2.요청 보내기
connection.request('GET','/')

# 3. 응답 받기
response = connection.getresponse()
print(response.status,response.reason)


# 4.Body 읽어오기
body = response.read()
print(body)

#
# 에러 받아보기
#

connection.request('GET','/babo.html')
response = connection.getresponse()
print(response.status, response.reason)