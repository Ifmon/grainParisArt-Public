import locale
from datetime import datetime, timedelta

# Définit la langue locale en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

def getNextDays():
    current_date = datetime.now()
    # Calcul des 7 prochains jours à partir de cette date
    agenda = {}
    for i in range(1, 8):
        date = (current_date + timedelta(days=i))

        agenda[f'jour{i}'] = {"jour": date.strftime('%a').replace('.', ''), "date": date.strftime('%d'), "mois": date.strftime('%b').replace('.', ''), "toText": date.strftime('%Y-%m-%d')}
    return agenda