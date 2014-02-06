from gaesessions import SessionMiddleware
def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key="bulghuralsdjljewouteiouwoiu343247897w38924728394732432879472")
    return app