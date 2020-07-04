from flask import request, redirect, url_for, render_template, flash, session
from cafe_site import db
from cafe_site import app
from cafe_site.models.reviews import Review
from cafe_site.views.loging import login_required
from flask import Blueprint

review = Blueprint('review', __name__)

@review.route('/board')
@login_required
def show_reviews():
    reviews = Review.query.filter_by(user_id=session['user_id'])
    return render_template('reviews/index.html', reviews=reviews, id="board")



@review.route('/reviews', methods=['POST'])
@login_required
def add_review():
    review = Review(
        star=request.form['star'],
        title=request.form['title'],
        text=request.form['text'],
        user_id=session['user_id']
    )
    db.session.add(review)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('review.show_reviews'))



@review.route('/reviews/new', methods=['GET'])
@login_required
def new_review():
    return render_template('reviews/review.html', id="review")



@review.route('/reviews/<int:id>', methods=['GET'])
@login_required
def show_review(id):
    review = Review.query.get(id)
    if review.user_id != session['user_id']:
        flash('不正な操作が行われました')
        return redirect(url_for('review.show_reviews'))
    return render_template('reviews/show.html', review=review, id="show")


@review.route('/reviews/<int:id>/edit', methods=['GET'])
@login_required
def edit_review(id):
    review = Review.query.get(id)
    if review.user_id != session['user_id']:
        flash('不正な操作が行われました')
        return redirect(url_for('review.show_reviews'))
    return render_template('reviews/edit.html', review=review)


@review.route('/reviews/<int:id>/update', methods=['POST'])
@login_required
def update_review(id):
    review = Review.query.get(id)
    if review.user_id != session['user_id']:
        flash('不正な操作が行われました')
        return redirect(url_for('review.show_reviews'))
    review.star = request.form['star']
    review.title = request.form['title']
    review.text = request.form['text']
    db.session.merge(review)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('review.show_reviews'))


@review.route('/reviews/<int:id>/delete', methods=['POST'])
@login_required
def delete_review(id):
    review = Review.query.get(id)
    if review.user_id != session['user_id']:
        flash('不正な操作が行われました')
        return redirect(url_for('review.show_reviews'))
    db.session.delete(review)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('review.show_reviews'))