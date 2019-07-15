def render_template(template_name, **context):
    template_path = os.path.join(os.path.dirname(__file__),
                                 '..', 'templates')
    jinja_env = Environment(loader=FileSystemLoader(template_path),
                            autoescape=True)

    def datetimeformat(value):
        return datetime.fromtimestamp(value).strftime('%H:%M / %d-%m-%Y')

    jinja_env.filters['datetimeformat'] = datetimeformat
    t = jinja_env.get_template(template_name)
    return Response(t.render(context), mimetype='text/html')