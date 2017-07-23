# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# Creation of multiple instances of class media.Movie

toy_story=media.Movie("Toy Story","Taking place in a world where toys pretend"
" to be lifeless whenever humans are present, the film's plot focuses on the"
" relationship between Woody and Buzz Lightyear as they evolve from rivals"
" competing for affection to friends who work together to be reunited with"
" Andy, their owner, as his family prepares to move to a new home."
,"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_"
"5670999f.jpeg?region=0,0,300,450"
,"https://youtu.be/4KPTXpQehio" )

up=media.Movie("Up","By tying thousands of balloons to his home, 78-year-old"
" Carl sets out to fulfill his dream to see the wilds of South America and"
" complete a promise made to his late wife, Ellie."
,"https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Up_%282009_film%29."
"jpg/220px-Up_%282009_film%29.jpg"
,"https://youtu.be/qas5lWp7_R0" )

bambi=media.Movie("Bambi","The story of a deer hailed as the"
" 'Prince of the Forest' at his birth.Bambi must learn to be brave if he is to"
" lead the other deer to safety."
,"https://vignette4.wikia.nocookie.net/disney/images/2/29/Original_Bambi_Poste"
"r.png/revision/latest/scale-to-width-down/516?cb=20140511021641"
,"https://youtu.be/nLvX-erABqY" )

little_mermaid=media.Movie("The Little Mermaid","Based on the Danish fairy"
" tale of the same name by Hans Christian Andersen, The Little Mermaid tells"
" the story of a beautiful mermaid princess who dreams of becoming human."
,"https://resizing.flixster.com/FqODc2N-EiUshfG3j7sLz8IeOPg=/206x305/v1.bTs"
"xMTIwMzg0MztqOzE3NDU0OzEyMDA7MTUzNjsyMDQ4"
,"https://youtu.be/ZGZX5-PAwR8" )

finding_nemo=media.Movie("Finding Nemo","It tells the story of the"
" overprotective Ocellaris clownfish named Marlin who, along with a regal blue"
" tang named Dory, searches for his abducted son Nemo all the way to Sydney"
" Harbour. Along the way, Marlin learns to take risks and comes to terms with"
" Nemo taking care of himself"
,"https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-"
"Finding_Nemo.jpg"
,"https://youtu.be/2zLkasScy7A" )

monsters_inc=media.Movie("Monsters Inc.","The film centers on two monsters"
" employed at the titular energy-producing factory Monsters Inc. top scarer"
" James P. 'Sulley' Sullivan and his one-eyed partner and best friend Mike"
" Wazowski. In the film, employees at Monsters Inc. generate their city's"
" power by scaring children, but they themselves are afraid that the children"
" are toxic to them, and when one child enters the factory, Sulley and Mike"
" must return her home before it is too late."
,"https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG"
,"https://youtu.be/8IBNZ6O2kMk" )

# Groupping all the instances together in a list.
movies = [toy_story, up, bambi, little_mermaid, finding_nemo, monsters_inc]

# fresh_tomatoes.py contains the open_movies_page() function that will take in
# a list of movies and generate an HTML file, producing a website to showcase
# the movies.
fresh_tomatoes.open_movies_page(movies)
