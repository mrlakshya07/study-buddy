from flask import Flask, render_template, request, jsonify
import notes
import study_progress_tracker as progress
import pomodoro

app = Flask(__name__)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"success": False, "message": "Both fields are required."}), 400
    
    if users.get(username) == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."}), 401

@app.route('/api/signup', methods=['POST'])
def api_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"success": False, "message": "Both fields are required."}), 400
    
    if username in users:
        return jsonify({"success": False, "message": "Username already taken."}), 409
    
    users[username] = password
    return jsonify({"success": True, "message": "Signup successful! Please login."})

#Notes Routes
@app.route('/notes')
def notes_page():
    action = request.args.get('action', 'view')
    
    if action == 'view':
        all_notes = notes.viewnotes()
        return render_template('notes.html', notes=all_notes, action='view')
    
    elif action == 'add':
        return render_template('notes.html', action='add')
    
    elif action == 'search':
        return render_template('notes.html', action='search')
    
    return "Invalid action", 400

@app.route('/notes/add', methods=['POST'])
def add_note():
    note_text = request.form.get('note', '')
    result = notes.addnotes(note_text)
    all_notes = notes.viewnotes()
    return render_template('notes.html', notes=all_notes, action='view', message=result['message'])

@app.route('/notes/search', methods=['POST'])
def search_notes():
    keyword = request.form.get('keyword', '')
    result = notes.searchnotes(keyword)
    return render_template('notes.html', notes=result.get('results', []), action='search', message=result['message'])

@app.route('/notes/delete', methods=['POST'])
def delete_note():
    note_num = request.form.get('note_num', 0)
    try:
        result = notes.deletenotes(int(note_num))
        all_notes = notes.viewnotes()
        return render_template('notes.html', notes=all_notes, action='view', message=result['message'])
    except:
        return render_template('notes.html', notes=notes.viewnotes(), action='view', message="Error deleting note")

#Pomodoro Routes
@app.route('/pomodoro')
def pomodoro_page():
    return render_template('pomodoro.html')

@app.route('/pomodoro/start', methods=['POST'])
def start_pomodoro_timer():
    minutes = request.form.get('minutes', 0)
    result = pomodoro.start_pomodoro(minutes)
    return jsonify(result)

# Progress Routes
@app.route('/progress')
def progress_page():
    data = progress.load_logged_data()
    history = progress.show_all_history(data)
    plot_url = progress.plot_average_study_time(data)
    return render_template('progress_page.html', data=data, history=history, plot_url=plot_url)

@app.route('/progress/log', methods=['GET', 'POST'])
def log_progress():
    if request.method == 'POST':
        date = request.form.get('date', '')
        hours = request.form.get('hours', '')
        result = progress.log_study_session(date, hours)
        return render_template('progress_log.html', message=result['message'], success=result['success'])
    return render_template('progress_log.html')

if __name__ == "__main__":
    app.run(debug=True)