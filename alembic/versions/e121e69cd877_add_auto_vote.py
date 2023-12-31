"""add auto-vote

Revision ID: e121e69cd877
Revises: 2e59e7213d1e
Create Date: 2023-07-27 17:57:01.072299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e121e69cd877'
down_revision = '2e59e7213d1e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes', # pylint: disable=no-member
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('post_id', 'user_id')
    )
    op.alter_column('posts', 'published', # pylint: disable=no-member
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'published', # pylint: disable=no-member
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
    op.drop_table('votes') # pylint: disable=no-member
    # ### end Alembic commands ###
