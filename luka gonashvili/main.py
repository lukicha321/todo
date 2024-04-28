from flask import Flask, request, render_template



app = Flask(__name__)
app.config['DEBUG'] = True


tasks =[]

@app.route('/', methods=['GET', 'POST'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="TODOs", tasks=tasks)


app.run()

'''
bonusi:
1. idk
2. sikvdilit
3. nestani
4. mokled sheezlo daewera ori dgistvis didi wignia ise idealuri wignia
'''