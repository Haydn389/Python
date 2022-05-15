# lux={'health':490,'health':550,'mana':334,'melee':550,'armor':18.72}
lux=dict(health=550,mana=334,melee=550,armor=18.72)
# lux=dict(zip(['health','mana','melee','armor'],[550,334,550,18.72]))
# lux=dict([('health',490),('health',550),('mana',334),('melee',550),('armor',18.72)])
print("1 ",lux)
print("2 ",lux.items())
print("3 ",lux.values())
print("4 ",lux.keys())
print("5 ",sorted(lux))
def index(x):
    return x[1]
print("6 ",sorted(lux.items(),key=index))
print("7 ",sorted(lux.items(),key=lambda x:x[0]))
print(lux['health'])