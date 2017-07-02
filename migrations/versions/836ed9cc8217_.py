"""empty message

Revision ID: 836ed9cc8217
Revises: 860eaf7f7255
Create Date: 2017-06-14 14:14:09.750694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836ed9cc8217'
down_revision = '860eaf7f7255'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('batterscore')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batterscore',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('PA', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('AB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Hit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Single', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Double', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Triple', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HR', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('BB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('SB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('CS', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('K', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('R', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('RBI', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Errors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('GIDP', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HBP', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('XBH', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='batterscore_pkey')
    )
    # ### end Alembic commands ###
