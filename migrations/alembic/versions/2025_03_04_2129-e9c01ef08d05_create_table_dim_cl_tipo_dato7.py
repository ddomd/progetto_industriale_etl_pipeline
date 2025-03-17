"""create table dim_CL_TIPO_DATO7

Revision ID: e9c01ef08d05
Revises: aa2f0ac3bfeb
Create Date: 2025-03-04 21:29:40.835287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9c01ef08d05'
down_revision: Union[str, None] = 'aa2f0ac3bfeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("dim_cl_tipo_dato7", sa.Column("id", sa.String(50), primary_key=True), sa.Column("nome", sa.Text()))


def downgrade() -> None:
    op.drop_table("dim_cl_tipo_dato7")
