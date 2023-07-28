"""add foreign-key to posts table

Revision ID: f7ec406a0627
Revises: 89bb4ed7ead8
Create Date: 2023-07-27 17:28:46.656837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7ec406a0627'
down_revision = '89bb4ed7ead8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), nullable=False))# pylint: disable=no-member
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", # pylint: disable=no-member
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
        
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts") # pylint: disable=no-member
    op.drop_column('posts', 'owner_id') # pylint: disable=no-member
    pass
