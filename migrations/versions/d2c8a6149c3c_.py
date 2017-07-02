"""empty message

Revision ID: d2c8a6149c3c
Revises: eb41dcde8fa4
Create Date: 2017-06-21 23:17:54.217086

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd2c8a6149c3c'
down_revision = 'eb41dcde8fa4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('batters')
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
    op.create_table('batters',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('position', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('HitterAB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterBB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterCS', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterDouble', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterErrors', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterGIDP', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterHBP', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterHR', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterHit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterK', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterPA', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterR', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterRBI', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterSB', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterSingle', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterTriple', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('HitterXBH', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Hitteravg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('Hitterobp', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('Hitterops', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('Hitterslg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherBB', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherER', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherERA', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherG', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherHRA', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherHit', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherIP', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherK', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherK9', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherL', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherQS', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherS', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherW', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('PitcherWHIP', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='batters_pkey')
    )
    # ### end Alembic commands ###