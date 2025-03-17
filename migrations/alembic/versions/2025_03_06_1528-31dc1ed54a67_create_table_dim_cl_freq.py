"""create_table_dim_cl_freq

Revision ID: 31dc1ed54a67
Revises: b70fbcfe02de
Create Date: 2025-03-06 15:28:51.025665

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "31dc1ed54a67"
down_revision: Union[str, None] = "b70fbcfe02de"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_freq",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_freq")
