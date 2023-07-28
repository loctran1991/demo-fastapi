"""add requirement column to posts table

Revision ID: bf341d6b6465
Revises: 69c40f8bf733
Create Date: 2023-07-27 17:14:46.878547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf341d6b6465'
down_revision = '69c40f8bf733'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column( # pylint: disable=no-member
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column( # pylint: disable=no-member
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published') # pylint: disable=no-member
    op.drop_column('posts', 'created_at') # pylint: disable=no-member
    pass
