import requests, bs4
print('Searching...')
res = requests.get('https://www.letras.mus.br/ministerio-jovem/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('.song-name')
hrefs = [link.get('href') for link in links]

for i in range(50):
    res = requests.get('https://www.letras.mus.br' + hrefs[i])
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lyrics = soup.select('.cnt-letra > p')
    #pegar título
    title = soup.select('h1')[0].get_text()
    #pegar compositor
    compositor = soup.select('.letra-info_comp')[0].get_text()
    if  compositor == 'Sabe de quem é a composição? Envie pra gente.':
        compositor = 'Ministério Jovem'
    else:
        compositor = compositor.removeprefix('  Composição:')
    #salvar no firebase (pyrebase)
    #pegar ano
    print(title)
    print(compositor)

