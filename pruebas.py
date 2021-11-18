#Google trans
from googletrans import Translator
translator = Translator()

translation =  translator.translate("""Archer
Les Crâs sont des archers aussi fiers que précis ! Ils font des alliés précieux contre les adeptes de la mêlée franche.

Restant à distance, décochant leurs traits empennés dans le moindre orifice laissé sans surveillance, ils ne laissent aucun répit à leurs adversaires !""", dest='es')


print(f'{translation.text}')
