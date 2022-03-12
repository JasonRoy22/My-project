"""add foreign key

Revision ID: 71e3068fd431
Revises: 
Create Date: 2022-03-03 13:49:08.194504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71e3068fd431'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE drivers
        ADD CONSTRAINT fk_drivers_cars
        FOREIGN KEY (car_id)
        REFERENCES cars (id);
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP FOREIGN KEY fk_drivers_cars;
        """
    )
