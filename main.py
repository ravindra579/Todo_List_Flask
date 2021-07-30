
from docopt import docopt
import subprocess
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from todo import app
from todo.models import db, User, Todo
    
def _init_db():

    # Database initialisation
    db.create_all()

    # Filling the database with records for User and Todo models
    records = [
        User(username='user1',
             password=generate_password_hash('user1')),
        User(username='user2',
             password=generate_password_hash('user2')),
        Todo(user_id=1, description='task 1'),
        Todo(user_id=1, description='task 2'),
        Todo(user_id=1, description='task 3'),
        Todo(user_id=1, description='task 4'),
        Todo(user_id=1, description='task 5'),
        Todo(user_id=2, description='task 6'),
        Todo(user_id=2, description='task 7'),
        Todo(user_id=2, description='task 8')
        ]
    
    db.session.bulk_save_objects(records)
    db.session.commit()
    
    
if __name__ == '__main__':
    args = docopt(__doc__)
    if args['initdb']:
        _init_db()
        print 'Todo: Database initialized (database/todos.db)."
    else:
        app.run(use_reloader=True)
