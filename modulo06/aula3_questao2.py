urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dominios = []

for i in range(len(urls)):
    dominios.append(urls[i][4:-4])

print(dominios)