"""empty message

Revision ID: 9de18a7e20ee
Revises: b702b5ae166e
Create Date: 2017-06-28 17:08:35.596835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9de18a7e20ee'
down_revision = 'b702b5ae166e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'scoringindex',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('players', 'scoringindex',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
