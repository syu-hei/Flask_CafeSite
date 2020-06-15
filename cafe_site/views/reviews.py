from flask import request, redirect, url_for, render_template, flash, session
from cafe_site import db
from cafe_site import app
from cafe_site.models.reviews import Review



@app.route('/board')
def show_reviews():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    reviews = Review.query.order_by(Review.id.desc()).all()
    return render_template('reviews/index.html', reviews=reviews, id="board")



@app.route('/reviews/new', methods=['GET'])
def new_review():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('reviews/review.html', id="review")



@app.route('/reviews', methods=['POST'])
def add_review():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    review = Review(
        star=request.form['star'],
        title=request.form['title'],
        text=request.form['text']
    )
    db.session.add(review)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_reviews'))



@app.route('/reviews/<int:id>', methods=['GET'])
def show_review(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    review = Review.query.get(id)
    return render_template('reviews/show.html', review=review, id="show")


@app.route('/reviews/<int:id>/edit', methods=['GET'])
def edit_review(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    review = Review.query.get(id)
    return render_template('reviews/edit.html', review=review)


@app.route('/reviews/<int:id>/update', methods=['POST'])
def update_review(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    review = Review.query.get(id)
    review.star = request.form['star']
    review.title = request.form['title']
    review.text = request.form['text']
    db.session.merge(review)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_reviews'))


@app.route('/reviews/<int:id>/delete', methods=['POST'])
def delete_review(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_reviews'))