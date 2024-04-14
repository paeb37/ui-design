from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for

app = Flask(__name__)

current_id = 11 # starts at 11

data = [
    {
        "id": 1,
        "title": "Card Types",
        "image": "https://nairobiwire.com/wp-content/uploads/2021/10/how-many-clubs-are-there-in-a-deck-of-cards.jpg",
        "summary": "Once rivals in school, two brilliant doctors reunite by chance - each facing life's worst slump and unexpectedly finding solace in each other.",
        "actors": ["Shorter"],
        "genres": ["Medium"],
    },

    {
        "id": 2,
        "title": "Card Mechanics",
        "image": "https://i.pinimg.com/originals/ba/bb/00/babb0057cd7526fc7df4893245449fda.jpg",
        "summary": "A lawyer bound by a centuries-old curse becomes entangled with a civil servant who holds the key to his freedom.",
        "actors": ["Shorter"],
        "genres": ["Shorter"],
    },

    {
        "id": 3,
        "title": "Card Recognition",
        "image": "https://images.fineartamerica.com/images-medium-large-5/illustration-of-magnifying-glass-and-eye-representing-fanatic-studio--science-photo-library.jpg",
        "summary": "The residents of a high-rise apartment fight for their lives against a deadly infectious disease while Sae-bom and Yi-hyun try to find the person because of whom the virus spread.",
        "actors": ["Longer"],
        "genres": ["Medium"],
    },

    {
        "id": 4,
        "title": "Strong Girl Bong-soon",
        "image": "https://lilvakavivlu.files.wordpress.com/2017/08/strong-woman-do-bong-soon.jpg",
        "summary": "A woman born with superhuman strength is hired by the CEO of a gaming company, to be his bodyguard.",
        "actors": ["Park Bo-young", "Park Hyung-sik"],
        "genres": ["Romance", "Comedy"],
    },

    {
        "id": 5,
        "title": "Vincenzo",
        "image": "https://occ-0-2794-2219.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABdM2sXffnidbzI3S9GrfzAerUbMNuHdZSg1cxmrsR8RapRW6drFvlv_ytld6J2httaxSuVg0btWTBkmAXBh5G8LcNmsALGhk2ZmsASCxYCDr2XAabBd3DZpEHGb3U7eMYT9vdw.jpg?r=c8b",
        "summary": "During a visit to his motherland, a Korean-Italian mafia lawyer gives a conglomerate a taste of its own medicine with a side of justice.",
        "actors": ["Song Joong-ki"],
        "genres": ["Crime", "Thriller"],
    },

    {
        "id": 6,
        "title": "Descendants of the Sun",
        "image": "https://1.vikiplatform.com/c/23205c/Descendants-of-the-Sun_1560x872.jpg?x=b",
        "summary": "A love story between Captain Yoo Shi Jin, Korean Special Forces, and Doctor Kang Mo Yeon, surgeon at Haesung Hospital. Together they face danger in a war-torn country.",
        "actors": ["Song Joong-ki", "Song Hye-kyo"],
        "genres": ["Romance", "Thriller"],
    },

    {
        "id": 7,
        "title": "True Beauty",
        "image": "https://giveitashotreview.files.wordpress.com/2021/03/true-beauty-drama-poster.jpg?w=660",
        "summary": "A female student's life changes as she learns make-up techniques. Jugyeong lives hidden behind the make-up from her hurtful past, and Suho also loses joy from his hurtful past. The two rely on each other, sharing their secrets.",
        "actors": ["Moon Ga-young", "Cha Eun-woo", "Hwang In-youp"],
        "genres": ["Romance"],
    },

    {
        "id": 8,
        "title": "My Demon",
        "image": "https://occ-0-2794-2219.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABeL-khUK_CwyMApXmxxiyAZGMAE_hCfQK_cwYQd2MMRX-UviUJL1mKQuOxND8D2kH3c_Ht5tM20rOq3j9oIRCZuxxMxUZ2y0bRqu.jpg?r=51d",
        "summary": "Heiress Do Do Hee is an adversary to many, and Jung Koo Won is a powerful entity; when Jung Koo Won loses his powers, he must collaborate with Do Do Hee to regain them, and sparks fly between them as they embark on their journey.",
        "actors": ["Kim Yoo-jung", "Song Kang"],
        "genres": ["Romance", "Crime"],
    },

    {
        "id": 9,
        "title": "Perfect Marriage Revenge",
        "image": "https://1.vikiplatform.com/c/40179c/f45bf2fe5c.jpg?x=b",
        "summary": "Perfect Marriage Revenge is a 2023 South Korean television series starring Sung Hoon, Jung Yoo-min, Jin Ji-hee, Kang Shin-hyo, and Oh Seung-yoon.",
        "actors": ["Sung Hoon", "Jung Yoo-min"],
        "genres": ["Romance", "Crime"],
    },

    {
        "id": 10,
        "title": "My Man Is Cupid",
        "image": "https://i.ytimg.com/vi/1rbt9fBt-KQ/maxresdefault.jpg",
        "summary": "A love fairy inadvertently falls in love with a woman whose romantic partners always have a near-death experience.",
        "actors": ["Jang Dong-yoon", "Nana"],
        "genres": ["Romance", "Crime"],
    },


]

@app.route('/')
def welcome():
    items = data[:3] # take first 3

    return render_template('welcome.html', items=items) # home page

@app.route('/search', methods=['POST', 'GET'])
def search():

    search_query = request.form['searchQuery']
    # search_query = request.args.get('query', '')  # Default to an empty string if 'query' parameter is not provided
    # look for the titles with matching

    items = []

    for drama in data: # each drama entry
        # need to return where exactly it matched

        # check the title, actors, genre

        # then, in the return statement, have a field called "title", "actors", or "genre"
        # to figure out where it matched
        # and then return the matching text?

        # may use JS instead
        # how to account for multiple matches?

        matchFound = False

        if search_query.lower() in drama['title'].lower(): # if it's in the title
            matchFound = True
        
        for actor in drama['actors']:
            if search_query.lower() in actor.lower(): # matches the actor name
                matchFound = True
                break

        for genre in drama['genres']:
            if search_query.lower() in genre.lower(): # matches the genre
                matchFound = True
                break

        # for each item, edit the corresponding items to be in syntax
        if matchFound:
            items.append(drama)

    # print("hello beautiful")
    # print(items)

    return render_template('search_results.html', items=items, query=search_query)

'''
View a particular kdrama
'''
@app.route('/view/<int:id>', methods=['GET']) # GET request because just requesting info from server
def view(id):
    item = None

    print(data)

    for drama in data:
        if drama['id'] == int(id): # str by default
            item = drama
            break
    
    # matching item by actor
    itemActor = None
    itemGenre = None

    if item: # item exists
        actors = item['actors']
        genres = item['genres']

        for actor in actors: # for each actor in this particular kdrama
            for drama in data: # check if existing match in data
                if drama['id'] != int(id):
                    for actor2 in drama['actors']: # (BUT CANNOT BE THE SAME ITEM)
                        if actor.lower() == actor2.lower():
                            itemActor = drama
                            break

        for genre in genres: # for each actor in this particular kdrama
            for drama in data: # check if existing match in data
                if drama['id'] != int(id) and genre in drama['genres']: # (BUT CANNOT BE THE SAME ITEM)
                    itemGenre = drama
                    break

    # print(item)
    # print(item)

    return render_template('kdrama.html', item=item, itemActor=itemActor, itemGenre=itemGenre)

'''
Access the add a new kdrama page OR add a new kdrama
'''
@app.route('/add', methods=['POST', 'GET']) # GET request because just requesting info from server
def add_drama():
    global current_id
    global data
    
    if request.method == 'POST':
        # Access the form data
        title = request.form.get('title')
        image_url = request.form.get('image')
        summary = request.form.get('summary')
        actors = request.form.get('actors')
        genres = request.form.get('genres')

        # Optional: Process the comma-separated actors and genres into lists
        actors_list = [actor.strip() for actor in actors.split(',')]
        genres_list = [genre.strip() for genre in genres.split(',')]

        # Parse the form data
        new_item = {
            "id": current_id,
            "title": title,
            "image": image_url,
            "summary": summary,
            "actors": actors_list,
            "genres": genres_list
        }

        current_id += 1

        data.append(new_item)

        return jsonify({"id": new_item["id"]}) # item id of the new item
    else:
        return render_template('add_drama.html')
    
'''
Edit a kdrama
'''
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_kdrama(id):
    item = next((drama for drama in data if drama['id'] == id), None) # shorthand to find the drama by id

    if not item:
        return "Item not found", 404
    
    if request.method == 'POST':
        # Process the form data and update the item
        item['title'] = request.form['title']
        item['image'] = request.form['image']
        item['summary'] = request.form['summary']
        item['actors'] = request.form['actors'].split(',')
        item['genres'] = request.form['genres'].split(',')
        # Redirect to the view page to see changes
        return redirect(url_for('view', id=id)) # redirect them to the view/id URL
    
    else:# For a GET request, render the edit form with the item data
        return render_template('edit_drama.html', item=item)

if __name__ == '__main__':
   app.run(debug = True)