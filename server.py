from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
from datetime import datetime
import time

app = Flask(__name__)

start_time = datetime.now()
current_time = start_time

def get_elapsed_time():
    current_time_function = datetime.now()
    elapsed_time = current_time_function - start_time
    return elapsed_time.total_seconds() / 60

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

# keep track of the user's score (out of five)
score = 0
attempted = dict() # keep track of the problems the user has attempted
# and whether they got it right
# if they got it right and they retry, then deduct 1 from score
# if they got it wrong and retry, do nothing

# key value pair:
# 1: True # for problem 1, either True for success or False for incorrect

@app.route('/')
def start():
    current_time = datetime.now()
    items = data[:3] # take first 3

    return render_template('start.html', items=items, current_time=current_time) # home page

@app.route('/home', defaults={'reset': None})
@app.route('/home/<reset>') # reset in case they go back home after finishing the test
def welcome(reset):
    global score
    global attempted

    if reset:
        score = 0
        attempted = dict()

    items = data[:3] # take first 3

    current_time = datetime.now()
    elapsed_time = get_elapsed_time();

    return render_template('welcome.html', items=items, current_time=current_time, elapsed_time=elapsed_time) # home page

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
@app.route('/learn/<int:id>', methods=['GET']) # GET request because just requesting info from server
def learn(id):
    item = None
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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

    return render_template('kdrama.html', item=item, itemActor=itemActor, itemGenre=itemGenre, current_time=current_time, elapsed_time=elapsed_time)

'''
Access Types
'''

@app.route('/type/<int:id>', methods=['GET']) # GET request because just requesting info from server
def type(id):
    item = None
    number = 0
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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
    number = id

    return render_template('types.html', item=item, itemActor=itemActor, itemGenre=itemGenre, number=number, current_time=current_time, elapsed_time=elapsed_time)

@app.route('/overview/<int:id>', methods=['GET']) # GET request because just requesting info from server
def overview(id):
    item = None
    number = 0
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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
    number = id

    return render_template('overviews.html', item=item, itemActor=itemActor, itemGenre=itemGenre, number=number, current_time=current_time, elapsed_time=elapsed_time)

@app.route('/example/<int:id>', methods=['GET']) # GET request because just requesting info from server
def example(id):
    item = None
    number = 0
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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
    number = id

    return render_template('examples.html', item=item, itemActor=itemActor, itemGenre=itemGenre, number=number, current_time=current_time, elapsed_time=elapsed_time)

@app.route('/mechanic/<int:id>', methods=['GET']) # GET request because just requesting info from server
def mechanic(id):
    item = None
    number = 0
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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
    number = id

    return render_template('mechanics.html', item=item, itemActor=itemActor, itemGenre=itemGenre, number=number, current_time=current_time, elapsed_time=elapsed_time)

@app.route('/recognition/<int:id>', methods=['GET']) # GET request because just requesting info from server
def recognition(id):
    item = None
    number = 0
    current_time = datetime.now()
    elapsed_time = get_elapsed_time();
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
    number = id

    return render_template('recognitions.html', item=item, itemActor=itemActor, itemGenre=itemGenre, number=number, current_time=current_time, elapsed_time=elapsed_time)


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


# BRANDON'S CODE FOR LEARNING / QUIZ
@app.route('/quiz1/<int:state>', methods=['GET'])  # GET request because just requesting info from server
def quiz1(state):  # Now function takes both 'id' and 'state' as arguments
    quiz_state = state  # You can now use the 'state' variable inside your function
    # result = "" # only for the correct/incorrect part

    return render_template('quiz1.html', state=quiz_state)

@app.route('/quiz2/<int:state>', methods=['GET'])  # GET request because just requesting info from server
def quiz2(state):  # Now function takes both 'id' and 'state' as arguments
    quiz_state = state  # You can now use the 'state' variable inside your function
    # result = "" # only for the correct/incorrect part

    return render_template('quiz2.html', state=quiz_state)

@app.route('/quiz3/<int:state>', methods=['GET'])  # GET request because just requesting info from server
def quiz3(state):  # Now function takes both 'id' and 'state' as arguments
    quiz_state = state  # You can now use the 'state' variable inside your function
    # result = "" # only for the correct/incorrect part

    return render_template('quiz3.html', state=quiz_state)

@app.route('/test/<int:state>', methods=['GET'])  # GET request because just requesting info from server
def test(state):  # Now function takes both 'id' and 'state' as arguments
    quiz_state = state  # You can now use the 'state' variable inside your function
    # result = "" # only for the correct/incorrect part

    return render_template('test.html', state=quiz_state)

@app.route('/submit/<int:problem_number>', methods=['POST'])
def submit(problem_number):
    global score

    number = request.form['number']
    print(number)

    correct_ans = None
    correct = False

    problem_number = int(problem_number)

    if problem_number in attempted: # if they tried this problem already
        if attempted[problem_number]: # only if they got it correct, then deduct the point
            score -= 1
    
    if problem_number == 1:
        correct_ans = 0
    elif problem_number == 2:
        correct_ans = 0
    elif problem_number == 3:
        correct_ans = 3
    elif problem_number == 4:
        correct_ans = -5
    elif problem_number == 5:
        correct_ans = -1
    
    if int(number) == int(correct_ans): # show at the end
        score += 1
        correct = True
    
    # return redirect(url_for('index'))  # Redirect back to the form page, or wherever you need.
    return render_template('test_result.html', problem_number=problem_number, your_ans=number, correct_ans=correct_ans, correct=correct, score=score)

if __name__ == '__main__':
   app.run(debug = True)