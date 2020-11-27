import requests, sys, bs4
from fire_connection import FireConnection

# open firebase connection
fc = FireConnection()

print('Searching...')
res = requests.get('https://www.letras.mus.br/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('.song-name')
hrefs = [link.get('href') for link in links]

print('Saving data...')
for i in range(len(hrefs)):
    res = requests.get('https://www.letras.mus.br' + hrefs[i])
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    lyrics = soup.select('.cnt-letra > p')
    lyrics = [str(lyric) for lyric in lyrics] # convert tag soup object to list of strings
    lyrics = " ".join(lyrics)

    #pegar título
    title = soup.select('h1')[0].get_text()
    #pegar compositor
    compositor = soup.select('.letra-info_comp > a')[0].get_text()
    if  compositor == 'Sabe de quem é a composição? Envie pra gente.':
        compositor = 'Hinário Adventista'
    else:
        compositor = soup.select('.letra-info_comp')[0].get_text().strip()
        compositor = compositor.removeprefix('Composição:')
        compositor = compositor.removesuffix('. Essa informação está errada? Nos avise.')
        
    #salvar no firebase (pyrebase)    
    fc.save_music(title,compositor,lyrics,"Não informado")
    #print(lyrics)
    
print("Done.")

