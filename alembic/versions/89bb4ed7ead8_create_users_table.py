"""create users table

Revision ID: 89bb4ed7ead8
Revises: bf341d6b6465
Create Date: 2023-07-27 17:16:24.150373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89bb4ed7ead8'
down_revision = 'bf341d6b6465'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', # pylint: disable=no-member
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users') # pylint: disable=no-member
    pass
