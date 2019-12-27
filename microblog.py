from app import create_app, db
from app.models import User, Tests, Ustests, Result,  Opros1

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Opros1': Opros1}