"""create table dim_CL_ATECO_2007

Revision ID: 66001c46d786
Revises: b7ed11a2890a
Create Date: 2025-03-04 21:30:10.718884

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66001c46d786'
down_revision: Union[str, None] = 'b7ed11a2890a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("dim_cl_ateco_2007", sa.Column("id", sa.String(50), primary_key=True), sa.Column("nome", sa.Text()))


def downgrade() -> None:
    op.drop_table("dim_cl_ateco_2007")
