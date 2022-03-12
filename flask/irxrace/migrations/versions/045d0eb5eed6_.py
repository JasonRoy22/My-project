"""empty message

Revision ID: 045d0eb5eed6
Revises: f4c1368b428e
Create Date: 2022-03-05 08:50:45.491962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045d0eb5eed6'
down_revision = 'f4c1368b428e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race info')
    op.add_column('cars', sa.Column('driver_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cars', 'drivers', ['driver_id'], ['id'])
    op.add_column('drivers', sa.Column('username', sa.String(length=128), nullable=False))
    op.add_column('drivers', sa.Column('car_id', sa.Integer(), nullable=True))
    op.add_column('drivers', sa.Column('date_created', sa.DateTime(), nullable=True))
    op.drop_constraint('drivers_name_key', 'drivers', type_='unique')
    op.create_unique_constraint(None, 'drivers', ['username'])
    op.create_foreign_key(None, 'drivers', 'cars', ['car_id'], ['id'])
    op.drop_column('drivers', 'name')
    op.add_column('incident', sa.Column('race_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'incident', 'races', ['race_id'], ['id'])
    op.add_column('races', sa.Column('best_lap_time', sa.Integer(), nullable=False))
    op.add_column('races', sa.Column('car_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'races', 'cars', ['car_id'], ['id'])
    op.drop_column('races', 'best_lap_times')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('races', sa.Column('best_lap_times', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'races', type_='foreignkey')
    op.drop_column('races', 'car_id')
    op.drop_column('races', 'best_lap_time')
    op.drop_constraint(None, 'incident', type_='foreignkey')
    op.drop_column('incident', 'race_id')
    op.add_column('drivers', sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'drivers', type_='foreignkey')
    op.drop_constraint(None, 'drivers', type_='unique')
    op.create_unique_constraint('drivers_name_key', 'drivers', ['name'])
    op.drop_column('drivers', 'date_created')
    op.drop_column('drivers', 'car_id')
    op.drop_column('drivers', 'username')
    op.drop_constraint(None, 'cars', type_='foreignkey')
    op.drop_column('cars', 'driver_id')
    op.create_table('race info',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"race info_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('starting_position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('ending_position', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('qualifying_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('average_lap_times', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('best_lap_time', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='race info_pkey')
    )
    # ### end Alembic commands ###
