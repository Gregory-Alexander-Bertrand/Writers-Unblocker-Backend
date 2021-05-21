"""create-users

Revision ID: f64ebde4e9b1
Revises: 
Create Date: 2021-05-21 12:22:45.829667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f64ebde4e9b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String),
    )


def downgrade():
    op.drop_table('users')
