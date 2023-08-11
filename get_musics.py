from fire_connection import FireConnection
fc = FireConnection()

docs = fc.get_musics()

count = 0
for doc in docs:
    count += 1
    print(count, end='\r')
print()