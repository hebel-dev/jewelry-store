


class Basket():

    def __init__(self, request):
        # if sesion dosent exist the session will be created
        #every sesion is request
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.sesion:
            basket = self.session['session_key'] = {}
        self.basket = basket