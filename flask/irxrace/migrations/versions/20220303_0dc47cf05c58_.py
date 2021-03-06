"""empty message

Revision ID: 0dc47cf05c58
Revises: 
Create Date: 2022-03-03 12:48:42.037539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dc47cf05c58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drivers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('email_address', sa.String(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address'),
    sa.UniqueConstraint('username')
    )
    op.create_table('incident',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cars_involved', sa.Integer(), nullable=False),
    sa.Column('number_of_incidents', sa.Integer(), nullable=False),
    sa.Column('repair_time_of_damage', sa.Integer(), nullable=True),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('races',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('starting_position', sa.Integer(), nullable=False),
    sa.Column('ending_position', sa.Integer(), nullable=False),
    sa.Column('qualifying_time', sa.Integer(), nullable=True),
    sa.Column('lap_times', sa.Integer(), nullable=False),
    sa.Column('average_lap_times', sa.Integer(), nullable=False),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ending_position'),
    sa.UniqueConstraint('starting_position')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('license', sa.String(length=1), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('make', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('races')
    op.drop_table('incident')
    op.drop_table('drivers')
    # ### end Alembic commands ###
