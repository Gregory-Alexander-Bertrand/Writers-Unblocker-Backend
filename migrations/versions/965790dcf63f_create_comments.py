"""create-comments

Revision ID: 965790dcf63f
Revises: fdeeac4b29a5
Create Date: 2021-05-21 12:24:29.692582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '965790dcf63f'
down_revision = 'fdeeac4b29a5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('body', sa.String, nullable=False),
        sa.Column('stories_id', sa.Integer),
        sa.Column('user_id', sa.Integer),
    )


def downgrade():
    op.drop_table('comments')
