"""empty message

Revision ID: baea07cd192e
Revises: 0d48718af8be
Create Date: 2024-12-05 02:37:12.827125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'baea07cd192e'
down_revision: Union[str, None] = '0d48718af8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
