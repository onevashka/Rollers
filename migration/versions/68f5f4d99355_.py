"""empty message

Revision ID: 68f5f4d99355
Revises: baea07cd192e
Create Date: 2024-12-05 02:39:54.453204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68f5f4d99355'
down_revision: Union[str, None] = 'baea07cd192e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
