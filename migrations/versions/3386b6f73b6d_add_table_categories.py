"""add table categories

Revision ID: 3386b6f73b6d
Revises: f95ba27d2a6e
Create Date: 2019-11-08 23:25:42.122124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3386b6f73b6d'
down_revision = 'f95ba27d2a6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_categories_name'), ['name'])

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_posts_category_id_categories'), 'categories', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_posts_category_id_categories'), type_='foreignkey')
        batch_op.drop_column('category_id')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_categories_name'), type_='unique')

    # ### end Alembic commands ###