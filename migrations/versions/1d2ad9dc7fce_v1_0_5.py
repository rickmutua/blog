"""v1.0.5

Revision ID: 1d2ad9dc7fce
Revises: e99ef6fb063c
Create Date: 2017-11-03 17:11:41.700222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d2ad9dc7fce'
down_revision = 'e99ef6fb063c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    op.add_column('reviews', sa.Column('blog_id', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'blogs', ['blog_id'], ['id'])
    op.create_foreign_key(None, 'reviews', 'users', ['user_id'], ['id'])
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'user_id')
    op.drop_column('reviews', 'blog_id')
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###