"""empty message

Revision ID: eabcdcf71e9b
Revises: fa5287a7fc0d
Create Date: 2021-10-29 21:12:38.259869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eabcdcf71e9b'
down_revision = 'fa5287a7fc0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tag_article_id_fkey', 'tag', type_='foreignkey')
    op.drop_column('tag', 'article_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tag', sa.Column('article_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('tag_article_id_fkey', 'tag', 'article', ['article_id'], ['id'])
    # ### end Alembic commands ###