"""add content column to posts table

Revision ID: ba8be70e0aca
Revises: 575ca33982c9
Create Date: 2026-10-19 14:19:51.164606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba8be70e0aca'
down_revision: Union[str, Sequence[str], None] = '575ca33982c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts', 
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
