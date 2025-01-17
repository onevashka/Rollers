"""empty message

Revision ID: 1f73eac32974
Revises: 10fba4a2ba54
Create Date: 2024-12-05 02:43:22.761650

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f73eac32974'
down_revision: Union[str, None] = '10fba4a2ba54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
