from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from models import User
from .. import db,photos



@main.route('/pitch/comment/new/<id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    #form = CommentForm()
    #pitch = get_pitch(id)

    return render_template('new_review.html')

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))