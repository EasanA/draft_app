"""empty message

Revision ID: 24828d6ba633
Revises: aea3270207cc
Create Date: 2017-07-04 00:41:31.323249

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '24828d6ba633'
down_revision = 'aea3270207cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('pitcher_cg_per_gs', sa.Float(), nullable=True))
    op.add_column('score', sa.Column('pitcher_shutout_per_gs', sa.Float(), nullable=True))
    op.drop_column('score', 'pitcher_cg')
    op.drop_column('score', 'pitcher_shutout')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('pitcher_shutout', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('score', sa.Column('pitcher_cg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('score', 'pitcher_shutout_per_gs')
    op.drop_column('score', 'pitcher_cg_per_gs')
    # ### end Alembic commands ###
