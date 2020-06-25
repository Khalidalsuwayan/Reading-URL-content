import urllib.request

with urllib.request.urlopen('https://s-m.com.sa/tr/d.html') as response:
    url = response.read()
print(url)
file = open("text.txt", "w")
file.write(str(url))
file.close()