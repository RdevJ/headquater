"""empty message

Revision ID: 77d8305fa35d
Revises: 5f01c349a7d4
Create Date: 2021-11-11 22:53:53.509309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77d8305fa35d'
down_revision = '5f01c349a7d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('label', sa.String(length=255), nullable=True))
    op.drop_column('answer', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('answer', 'label')
    # ### end Alembic commands ###
