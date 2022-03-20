"""empty message

Revision ID: b58b6960f046
Revises: f72debe806d7
Create Date: 2022-03-20 22:46:14.713393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b58b6960f046'
down_revision = 'f72debe806d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'date')
    # ### end Alembic commands ###
