import os, json

songs= json.loads(open('data.json',encoding='utf-8').read())
template= open('ok.html',encoding='utf-8').read()

data1='<img class="img slider__img" src="assets/thumb.jpg" alt="cover">'
data2=''

i=0
for song in songs:
    if i==0:
        i=1
    else:
        data1+=f'\n<img class="img slider__img" src="https://i.ytimg.com/vi/{songs[song][3]}/default.jpg" alt="cover">'

    data2+=f'\n<li class="player__song"><img class="player__img img" src="https://i.ytimg.com/vi/{songs[song][3]}/default.jpg" alt="cover"><p class="player__context "><b class="player__song-name"> {songs[song][0]}</b><span class="flex"><span class="player__title">{songs[song][1]}</span><span class="player__song-time"></span></span></p><audio class="audio" src="https://f003.backblazeb2.com/file/mah-music/songs/{song}.{songs[song][2]}" preload="none" crossorigin="anonymous" spotify="{songs[song][4]}" youtube="{songs[song][3]}"></audio></li>'
    
finaldata=template.replace('<!-- data1 here -->',data1).replace('<!-- data2 here -->',data2)

with open('ohk.html','w',encoding='utf-8') as f:
    f.write(finaldata)