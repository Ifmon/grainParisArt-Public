from flask import Flask, render_template, request
from datetime import datetime
from flask_caching import Cache
import asyncio

# IMPORT DES MODULES 
from modules.date import getNextDays
from modules.scraping import scrap_infoFilm, get_data, cleanFilms
from modules.urlGenerator import decalageDate

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=3600)
def home():
    date = getNextDays()

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0071.html"
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C2954.html",
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0050.html"
        }, 
        {
            "salle" : "Épée de bois",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=W7504.html"
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0076.html"
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0089.html"
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0013.html"
        },
        {
            "salle" : "Le Grand Action",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0072.html"
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0099.html"
        },
        { 
            "salle" : "Le Champo",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0073.html"
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0020.html"
        },
        {
            "salle" : "Reflet Medicis",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0074.html"
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0159.html"
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : "https://www.allocine.fr/seance/salle_gen_csalle=C0026.html"
        }
    ]

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)

    return render_template('index.html', page_actuelle='home', films=filmsClean, date=date)


@app.get('/jour<int:id>')
@cache.cached(timeout=3600)
def jour():
    date = getNextDays()

    films = []

    cinemas = [
        {
            "salle" : "Écoles Cinéma Club",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0071.html#shwt_date=", id)
        },
        {
            "salle" : "MK2 Bibliothèque",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C2954.html#shwt_date=l",id)
        },
        {
            "salle" : "MK2 Beaubourg",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0050.html#shwt_date=",id)
        }, 
        {
            "salle" : "Épée de bois",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=W7504.html#shwt_date=",id)
        }, 
        {
            "salle" : "Cinéma du Panthéon",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0076.html#shwt_date=",id)
        },
        {
            "salle" : "Max Linder Panorama",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0089.html#shwt_date=",id)
        },
        {
            "salle" : "Luminor Hotel de Ville",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0013.html#shwt_date=",id)
        },
        {
            "salle" : "Le Grand Action",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0072.html#shwt_date=",id)
        },
        {
            "salle" : "MK2 Parnasse", 
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0099.html#shwt_date=",id)
        },
        { 
            "salle" : "Le Champo",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0073.html#shwt_date=",id)
        },
        {
            "salle" : "Filmothèque du Quartier Latin",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0020.html#shwt_date=",id)
        },
        {
            "salle" : "Reflet Medicis",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0074.html#shwt_date=",id)
        },
        {
            "salle" : "UGC Ciné Cité Les Halles",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0159.html#shwt_date=",id)
        },
        {
            "salle" : "UGC Ciné Cité Bercy",
            "url" : decalageDate("https://www.allocine.fr/seance/salle_gen_csalle=C0026.html#shwt_date=",id)
        }
    ]

    films = get_data(cinemas)
    filmsClean = cleanFilms(films)

    return render_template(f'jours/jour{id}.html', page_actuelle=f'jour{1}', films=filmsClean, date=date)

"""
@app.route('/process')
def process():
    # Simule un traitement long
    time.sleep(5)
    return jsonify(status='success', message='Traitement terminé')
"""
if __name__ == '__main__':
    app.run(debug=True) 