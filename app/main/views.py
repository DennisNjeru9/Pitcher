from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required


@main.route('/pitch/comment/new/<id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    #form = CommentForm()
    #pitch = get_pitch(id)

    return render_template('new_review.html')