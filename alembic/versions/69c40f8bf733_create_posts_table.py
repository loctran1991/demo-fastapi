"""create posts table

Revision ID: 69c40f8bf733
Revises: 
Create Date: 2023-07-27 17:12:09.948159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69c40f8bf733'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, # pylint: disable=no-member
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None: 
    op.drop_table('posts') # pylint: disable=no-member
    pass
