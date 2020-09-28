from flask import Flask, render_template, request, redirect, session, flash
import random
app =Flask(__name__)
app.secret_key='greatnumbergame'

@app.route('/')
def index():
    session['number']= random.randrange(0,101)
    print(session['number'])
    return render_template('game.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    while session['guess'] != session['number']:
        if session['guess'] < session['number']:
            session['answer']=2
        elif session['guess'] > session['number']:
            session['answer']=3
        else:
            break
        return render_template('game.html')
    if session['guess'] == session['number']:
            session['answer']=1
    return redirect('/')


@app.route('/playagain')
def play_again(): 
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)