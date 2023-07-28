"""add content column to post table

Revision ID: 2e59e7213d1e
Revises: f7ec406a0627
Create Date: 2023-07-27 17:36:18.780983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e59e7213d1e'
down_revision = 'f7ec406a0627'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False)) # pylint: disable=no-member
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content') # pylint: disable=no-member
    pass
