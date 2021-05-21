"""create-prompts

Revision ID: fdeeac4b29a5
Revises: cc7de980f66c
Create Date: 2021-05-21 12:24:10.979858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdeeac4b29a5'
down_revision = 'cc7de980f66c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'prompts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('prompt', sa.String, nullable=False),
        sa.Column('genre', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('prompts')
