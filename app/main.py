from flask import Flask, render_template, request, redirect
from app.services.user_service import get_user_by_id, add_user, users, delete_user
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, '..', 'templates')

app = Flask(__name__, template_folder=template_dir)


@app.route('/', methods=['GET', 'POST'])
def home():
    user = None
    error = None

    if request.method == 'POST':
        if 'user_id' in request.form:
            try:
                user_id = int(request.form['user_id'])
                user = get_user_by_id(user_id)

                if not user:
                    error = "User not found"
            except:
                error = "Invalid input"

    return render_template('index.html', user=user, error=error, users=users)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    add_user(name, email)
    return redirect('/')


@app.route('/delete/<int:user_id>')
def delete(user_id):
    delete_user(user_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
