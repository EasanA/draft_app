"""empty message

Revision ID: b702b5ae166e
Revises: c477b524401b
Create Date: 2017-06-27 01:18:41.659662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b702b5ae166e'
down_revision = 'c477b524401b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('scoringindex', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'players', 'score', ['scoringindex'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'players', type_='foreignkey')
    op.drop_column('players', 'scoringindex')
    # ### end Alembic commands ###