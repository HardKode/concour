from flask import Flask, render_template, g, request, url_for
from googleplaces import GooglePlaces, types, lang
from google_key import GOOGLE_MAP_API_KEY
from database import connect_db, get_db


google_places = GooglePlaces(GOOGLE_MAP_API_KEY)

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/', methods=['GET', 'POST'])
def geolocation():

    q_place = ''
    query_result = ''

    if request.method == 'POST':
        q_place =  request.form['q_place'] # query address

        # # You may prefer to use the text_search API, instead.
        # query_result = google_places.nearby_search(location=q_place,
        #                                        radius=30000, types=[types.TYPE_SCHOOL], language=lang.FRENCH
        #                                        )
        # print("===============================================================================================")
        #
        # for place in query_result.places:
        #     place.get_details()
        #     print(place.url)
        #
        print(q_place)

    return render_template('geolocation.html', q_query=q_place)

@app.route('/tourisme', methods=['GET', 'POST'])
def tourisme():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select service, url, address,  lat, lng  from tourisme where service = ? ', [q_place])
        result = cur.fetchall()

        return render_template('tourisme.html', results=result)

    cur = db.execute('select service, url, address,  lat, lng  from tourisme')
    results = cur.fetchall()

    return render_template('tourisme.html', results=results)




@app.route('/immersion', methods=['GET', 'POST'])
def immersion():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select name, lat, lng  from immersion_schools where name = ? ', [q_place])
        result = cur.fetchall()

        return render_template('immersion.html', results=result)

    cur = db.execute('select  name, lat, lng  from immersion_schools')
    results = cur.fetchall()

    return render_template('immersion.html', results=results)



@app.route('/min_school', methods=['GET', 'POST'])
def min_school():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select name, lat, lng  from minority_schools where name = ? ', [q_place])
        result = cur.fetchall()

        return render_template('min_school.html', results=result)

    cur = db.execute('select  name, lat, lng  from minority_schools')
    results = cur.fetchall()

    return render_template('min_school.html', results=results)


@app.route('/education_programme', methods=['GET', 'POST'])
def education_programme():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select service, url, address,  lat, lng  from education_programme where service = ? ', [q_place])
        result = cur.fetchall()

        return render_template('education_programme.html', results=result)

    cur = db.execute('select service, url, address,  lat, lng  from education_programme')
    results = cur.fetchall()
    return render_template('education_programme.html', results=results)


@app.route('/loisir_sports', methods=['GET', 'POST'])
def loisir_sports():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select service, url, address,  lat, lng  from loisir_sport where service = ? ', [q_place])
        result = cur.fetchall()

        return render_template('loisir_sports.html', results=result)

    cur = db.execute('select service, url, address,  lat, lng  from loisir_sport ')
    results = cur.fetchall()
    return render_template('loisir_sports.html', results=results)



@app.route('/service_minicipaux', methods=['GET', 'POST'])
def service_minicipaux():
    db = get_db()

    if request.method == 'POST':
        q_place = request.form['q_place']  # query address

        cur = db.execute('select service, url, address,  lat, lng  from education_programme where service = ? ', [q_place])
        result = cur.fetchall()

        return render_template('service_minicipaux.html', results=result)

    cur = db.execute('select service, url, address,  lat, lng  from education_programme')
    results = cur.fetchall()
    return render_template('service_minicipaux.html', results=results)


@app.route('/test', methods=['GET', 'POST'])
def test():
       db = get_db()

       if request.method == 'POST':
           q_place = request.form['q_place']  # query address

           cur = db.execute('select service, url, address,  lat, lng  from education_programme where service = ? ', [q_place])
           result = cur.fetchall()

           return render_template('test.html', results=result)

       cur = db.execute('select service, url, address,  lat, lng  from education_programme')
       results = cur.fetchall()
       return render_template('test.html', results=results)
















if __name__ == '__main__':
    app.run(debug=True)
