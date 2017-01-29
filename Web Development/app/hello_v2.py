from app import webapp


@webapp.route('/hello')
def hello_world_v2():
    return 'Hello, World!'
