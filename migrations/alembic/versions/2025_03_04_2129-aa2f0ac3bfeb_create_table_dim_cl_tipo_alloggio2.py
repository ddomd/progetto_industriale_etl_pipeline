"""create table dim_CL_TIPO_ALLOGGIO2

Revision ID: aa2f0ac3bfeb
Revises: 047c6bef0d80
Create Date: 2025-03-04 21:29:27.363943

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aa2f0ac3bfeb"
down_revision: Union[str, None] = "047c6bef0d80"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "dim_cl_tipo_alloggio2",
        sa.Column("id", sa.String(50), primary_key=True),
        sa.Column("nome", sa.Text()),
    )


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_alloggio2")
