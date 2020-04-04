import os
from flask import Flask, render_template
app = Flask(__name__)


def valid_projects():
    TOP_DIR='/Users/alfredo/python'
    python_projects = []
    for directory in os.listdir(TOP_DIR):
        index_path = os.path.join(TOP_DIR, directory, 'htmlcov/index.html')
        if os.path.exists(index_path):
            python_projects.append(directory)
    return python_projects


@app.route('/')
def index():
    return render_template('index_coverage.html', files=valid_projects())



from flask import url_for, abort, send_file

@app.route('/<project>')
def project(project):
    TOP_DIR='/Users/alfredo/python'
    if project not in valid_projects():
        # project may be a static file
        for valid_project in valid_projects():
            static_file = os.path.join(TOP_DIR, valid_project, 'htmlcov', project)
            if os.path.exists(static_file):
                return send_file(static_file)
        abort(404, description='Invalid Project, not found!')
    index_file = os.path.join(TOP_DIR, project, 'htmlcov/index.html')
    return send_file(index_file)
    return app.send_static_file(index_file)
    return render_template(index_file)
    #return url_for('static', filename=index_file)

@app.route('/<project>/<path:req_path>')
def project_files(project, req_path):
    TOP_DIR='/Users/alfredo/python'
    abs_path = os.path.join(TOP_DIR, project, 'htmlcov', req_path)
    if os.path.isfile(abs_path):
        return send_file(abs_path)
    else:
        abort(404)
