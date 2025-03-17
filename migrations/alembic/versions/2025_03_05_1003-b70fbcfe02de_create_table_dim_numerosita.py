"""create_table_dim_numerosita

Revision ID: b70fbcfe02de
Revises: 66001c46d786
Create Date: 2025-03-05 10:03:26.581133

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b70fbcfe02de"
down_revision: Union[str, None] = "66001c46d786"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_numerosita",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_numerosita")
