import pdfkit
from myapp import myapp_obj
from flask import request, render_template

@myapp_obj.route('/mindmap')
def contact():
    '''
    Route that exports mindmap as a pdf.

    Returns
    -------
    Renders mindmap.html
    '''
    if 'submit_button' in request.form:
        pdfkit.from_file('mindmap.html', 'out.pdf')
    return render_template('mindmap.html')
