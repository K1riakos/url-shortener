from flask import Blueprint, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from .models import Url
from .db import db
from uuid import uuid4

views = Blueprint('views', __name__)


# create our form
class URLForm(FlaskForm):
  url = StringField('url', validators=[DataRequired(), Length(min=5)])


@views.route('/')
def home():
  form = URLForm()

  urls = Url.query.all()

  context = {'form': form, 'urls': urls, 'host': request.base_url}

  return render_template('index.html', context=context)

@views.route('/<string:slug>')
def away(slug):
  url = db.one_or_404(db.select(Url).filter_by(short_url=slug))

  u = url.url

  if u is not None:
    if u.find("http://") == -1 and u.find("https://") == -1:
      u = "http://" + u

  return redirect(u)



@views.route('/short', methods=['POST'])
def short():
  url = None
  form = URLForm()
  if form.validate_on_submit():
    slug = uuid4().hex[:6]
    url = form.url.data

    url_ = Url(url=url, short_url=slug)

    db.session.add(url_)
    db.session.commit()

  return redirect('/')