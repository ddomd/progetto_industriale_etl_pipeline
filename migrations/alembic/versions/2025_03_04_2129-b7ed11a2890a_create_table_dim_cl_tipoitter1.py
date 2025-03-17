"""create table dim_CL_TIPOITTER1

Revision ID: b7ed11a2890a
Revises: e9c01ef08d05
Create Date: 2025-03-04 21:29:59.387356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7ed11a2890a'
down_revision: Union[str, None] = 'e9c01ef08d05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("dim_cl_tipoitter1", sa.Column("id", sa.String(50), primary_key=True), sa.Column("nome", sa.Text()))


def downgrade() -> None:
    op.drop_table("dim_cl_tipoitter1")