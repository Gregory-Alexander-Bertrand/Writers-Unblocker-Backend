"""create-stories

Revision ID: cc7de980f66c
Revises: f64ebde4e9b1
Create Date: 2021-05-21 12:23:48.849946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc7de980f66c'
down_revision = 'f64ebde4e9b1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stories',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('story', sa.String, nullable=False),
        sa.Column('prompts_id', sa.Integer),
        sa.Column('user_id', sa.Integer),
    )


def downgrade():
    op.drop_table('stories')
