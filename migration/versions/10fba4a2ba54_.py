"""empty message

Revision ID: 10fba4a2ba54
Revises: 68f5f4d99355
Create Date: 2024-12-05 02:42:03.065811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10fba4a2ba54'
down_revision: Union[str, None] = '68f5f4d99355'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
