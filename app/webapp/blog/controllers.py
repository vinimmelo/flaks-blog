from sqlalchemy import func
from flask import render_template, Blueprint, flash, redirect, url_for
from .models import db, Post, Tag, Comment, User, tags
from .forms import CommentForm


blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder='../templates/blog',
    url_prefix="/blog"
)


def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all()
    top_tags = db.session.query(
        Tag, func.count(tags.c.post_id).label('total')
    ).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()

    return recent, top_tags
