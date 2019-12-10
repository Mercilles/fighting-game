import sys
import os
import time
import random



print('''   
╔╦╗┬ ┬┌┬┐┬ ┬┌─┐┬┌─┐┬ ┬┌┬┐┌─┐┬─┐
║║║└┬┘ │ ├─┤├┤ ││ ┬├─┤ │ ├┤ ├┬┘
╩ ╩ ┴  ┴ ┴ ┴└  ┴└─┘┴ ┴ ┴ └─┘┴└─


''')

prompt = '->'

print(''' Moin, Ich bin Fightmaster, du befindest dich hier in der Fabelwesenfightarena.
Ich werde dich, falls du willst, auf deinem Weg zum Meister begleiten. Aber bevor es losgeht
muss ich wissen wie du heisst. 

''')
print('''Dein Name ''')
player = input(prompt)

print(f''' Also {player}
Bist du bereit für deinen ersten Fight?

\tj = Ja
\tn = Nein''')

ready = input(prompt)

if ready == 'j':
    print('''Ab in den Kampf
        Du hast 15 Wesen zur Auswahl, von denen du 15 für deinen Kampf aussuchen darfst.
        Ein Match geht auf Maximal 5 Runden, der erste der drei Kämpfe für sich entscheidet, gewinnt das Spiel''')

    creature1 = 'Drache'
    creature2 = 'Zyklop'
    creature3 = 'Fee'
    creature4 = 'Skelettreiter'
    creature5 = 'Sensenmann'
    creature6 = 'Baby Yoda'
    creature7 = 'Minotaurus'
    creature8 = 'Einhorn'
    creature9 = 'Hydra'
    creature10 = 'Greif'
    creature11 = 'Bill Cipher'
    creature12 = 'Sirene'
    creature13 = 'Finsterer Magier'
    creature14 = 'Troll'
    creature15 = 'Krampus'




fabelwesen = (
    creature1,
    creature2,
    creature3,
    creature4,
    creature5,
    creature6,
    creature7,
    creature8,
    creature9,
    creature10,
    creature11,
    creature12,
    creature13,
    creature14,
    creature15
)

prompt = '->'
ascii_dragon = ''' 
  ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___   
 ~~ ~--__          ......====\\~~    .:::.    ~~//====......          __--~ ~~ 
         ~\ ...::::~~~~~~  //|||    .:::::.    |||\\  ~~~~~~::::... /~         
        -~~\_            //  |||***.(:::::).***|||  \\            _/~~-        
             ~\_        // *******.:|\^^^/|:.******* \\        _/~             
                \      / ********.::(0: :0)::.******** \      /                
                 \   /  ********.::::\\|//::::.********  \   /                 
                  \ /   *******.:::::(o o):::::.*******   \ /                  
                   /.   ******.::::'*|V_V|***`::.******   .\                   
                     ~~--****.:::'***|___|*****`:.****--~~                     
                           *.::'***//|___|\\*****`.*                           
                           .:'  **/##|___|##\**    .                           
                          .    (v(VVV)___(VVV)v)

'''

creature1 = {
  'ascii_art' : ascii_dragon,
  'name': 'Dragon',
  'attacks' : [{'spitfire': 35}, {'tailwhip': 25}, {'nosedive': 40}],
  'hp' : 230
}
ascii_cyclops = '''
        _......._
       .-'.'.'.'.'.'.`-.
     .'.'.'.'.'.'.'.'.'.`.
    /.'.'               '.\
    |.'    _.--...--._     |
    \    `._.-.....-._.'   /
    |     _..- .-. -.._   |
 .-.'    `.   ((@))  .'   '.-.
( ^ \      `--.   .-'     / ^ )
 \  /         .   .       \  /
 /          .'     '.  .-    \
( _.\    \ (_`-._.-'_)    /._\)
 `-' \   ' .--.          / `-'
     |  / /|_| `-._.'\   |
     |   |       |_| |   /-.._
 _..-\   `.--.______.'  |
      \       .....     |
       `.  .'      `.  /
         \           .'
          `-..___..-`
'''
creature2 = {
    'ascii_art' : ascii_cyclops,
   'name': 'Cyclops',
   'attacks': [{'stone throw': 30}, {'vibration stomp': 15}, {'fist punch': 35}],
   'hp': 270
}

ascii_fairy  = '''
         ,_  .--.
             , ,   _)\/    ;--.
     . ' .    \_\-'   |  .'    \
    -= * =-   (.-,   /  /       |
     ' .\'    ).  ))/ .'   _/\ /
         \_   \_  /( /     \ /(
         /_\ .--'   `-.    //  \
         ||\/        , '._//    |
         ||/ /`(_ (_,;`-._/     /
         \_.'   )   /`\       .'
              .' .  |  ;.   /`
             /      |\(  `.(
            |   |/  | `    `
            |   |  /
            |   |.'
         __/'  /
     _ .'  _.-`
  _.` `.-;`/
 /_.-'` / /
       | /
      ( /
     /_/
'''

creature3 = {
    'ascii_art' : ascii_fairy,
    'name': 'Fairy',
    'attacks': [{'magic bright': 65}, {'Braincontrol': 45}, {'teamheal': +50}],
    'hp': 100
}

creature4 = {
    'name': 'Skelletreiter',
    'attacks': [{'sword thrust': 30}, {'horse kick': 30}, {'shrill scream': 35}],
    'hp': 170
}


creature5 = {
    'name': 'Sensenmann',
    'attacks': [{'sickle slash': 50}, {'death wish': 55}, {'deathly wind': 35}],
    'hp': 150
}

  
ascii_babyyoda = '''

 <'-\________                                             ________/-'>
  \  _________\__________ /----¨¨¨¨¨¨¨¨¨----\  __________/_________ /
   \__       \__________/^   __         __   ^\_________/        __/
      \          \    \/   <__.> . . <.__>   \/     /           /      
       \______    \___ |        /-⎵-\        |  __/    _______/       
              \________\        .---.        /________/    
                        /---\_____________/---\
                        \         /           /
                         \______ /___________/
'''

creature6 = {
    'ascii_art' : ascii_babyyoda,
    'name': 'Baby Yoda',
    'attacks': [{'force stroke': 80}, {'Lasersword cut': 60}, {'protective shield': 5}],
    'hp': 130
}
ascii_minotaurus = '''
     .      .
     |\____/|
    (\|----|/)
     \ 0  0 /
      |    |
   ___/\../\____
  /     --       \
 /  \         /   \
|    \___/___/(   |
\   /|  }{   | \  )
 \  ||__}{__|  |  |
  \  |;;;;;;;\  \ / \_______
   \ /;;;;;;;;| [,,[|======'
     |;;;;;;/ |     /
     ||;;|\   |
     ||;;/|   /
     \_|:||__|
      \ ;||  /
      |= || =|
      |= /\ =|
      /_/  \_\
'''

creature7 = {
    'ascii_art' : ascii_minotaurus,
    'name': 'Minotaurus',
    'attacks': [{'axe swing': 35}, {'header': 20}, {'axe smash': 50}],
    'hp': 200
    
}
ascii_unicorn = '''
                |))    |))
 .             |  )) /   ))
 \\   ^ ^      |    /      ))
  \\(((  )))   |   /        ))
   / G    )))  |  /        ))
  |o  _)   ))) | /       )))
   --' |     ))`/      )))
    ___|              )))
   / __\             ))))`()))
  /\@   /             `(())))
  \/   /  /`_______/\   \  ))))
       | |          \ \  |  )))
       | |           | | |   )))
       |_@           |_|_@    ))
      /_/           /_/_/ 
'''

creature8 = {
    'ascii_art' : ascii_unicorn,
    'name' : 'Unicorn',
    'attacks': [{'hornmagic': 40},{'impaler': 50},{'brutal kick': 35}],
    'hp': 170
}

creature9 = {
    'name': 'Hydra',
    'attacks': [{'venom injection': 40}, {'head smash': 30}, {'triple bite': 45}],
    'hp': 180 
}
ascii_griffin = '''

          _____,    _..-=-=-=-=-====--,
     _.'a   /  .-',___,..=--=--==-'`
    ( _     \ /  //___/-=---=----'
     ` `\    /  //---/--==----=-'
  ,-.    | / \_//-_.'==-==---='
 (.-.`\  | |'../-'=-=-=-=--'
  (' `\`\| //_|-\.`;-~````~,        _
       \ | \_,_,_\.'        \     .'_`\
        `\            ,    , \    || `\\
          \    /   _.--\    \ '._.'/  / |
          /  /`---'   \ \   |`'---'   \/
         / /'          \ ;-. \
      __/ /           __) \ ) `|
    ((='--;)         (,___/(,_/
    '''
creature10 = {
    'ascii_art' : ascii_griffin,
    'name': 'Greif',
    'attacks': [{'beak shredder': 45}, {'scar-claw': 40}, {'eagle scream': 35}],
    'hp': 200
}

creature11 = {
    'name': 'Bill Cipher',
    'attacks': [{'laser eye': 60},{'multi punch': 20}, {'illuminati smash': 80}],
    'hp': 230

}

creature12 = {
    'name' : 'Sirene',
    'attacks': [{'shrill shredder': 25},{'water fountain': 30}, {'Death Song': 50}],
    'hp' : 120
}
ascii_dark_wizard = '''

              o
                   O       /`-.__
                          /  \�'^|
             o           T    l  *
                        _|-..-|_
                 O    (^ '----' `)
                       `\-....-/^
             O       o  ) "/ " (
                       _( (-)  )_
                   O  /\ )    (  /\
                     /  \(    ) |  \
                 o  o    \)  ( /    \
                   /     |(  )|      \
                  /    o \ \( /       \
            __.--'   O    \_ /   .._   \
           //|)\      ,   (_)   /(((\^)'\
              |       | O         )  `  |
              |      / o___      /      /
             /  _.-''^^__O_^^''-._     /
           .'  /  -''^^    ^^''-  \--'^
         .'   .`.  ^```----```^  .`. \
       .'    /   `'--..____..--'^   \ \
      /  _.-/                        \ \
  .::'_/^   |                        |  `.
         .-'|                        |    `-.
   _.--'`   \                        /       `-.
  /          \                      /           `-._
  `'---..__   `.                  .�_.._   __       \
           ```.              .'      `'^  `''---'^
                  `-..______..-'
'''

creature13 = {
    'ascii_art' : ascii_dark_wizard,
    'name': 'Dark Wizard',
    'attacks': [{'black hole': 45}, {'dark matter': 50}, {'Soul eater': 35}],
    'hp': 100,
    'ascii_pics' : 'ascii_magician'
}

creature14 = {
    'name': 'Goblin',
    'attacks': [{'fist punch': 25}, {'hammer swing': 30}, {'stone swing': 20}],
    'hp' : 250

}

creature15 = {
    'name' : 'Krampus',
    'attacks': [{'devil kick': 35}, {'gift steal': 60}, {'deadly bite': 45}],
    'hp' : 140
}




