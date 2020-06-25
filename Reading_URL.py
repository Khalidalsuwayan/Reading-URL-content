import urllib.request

with urllib.request.urlopen('https://www.python.org/') as response:
    url = response.read()
print(url)
file = open("text.txt", "w")
file.write(str(url))
file.close()