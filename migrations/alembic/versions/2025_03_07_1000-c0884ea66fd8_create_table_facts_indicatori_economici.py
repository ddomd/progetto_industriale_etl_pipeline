"""create_table_facts_indicatori_economici

Revision ID: c0884ea66fd8
Revises: 5951f7fe2d88
Create Date: 2025-03-07 10:00:49.863557

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0884ea66fd8"
down_revision: Union[str, None] = "5951f7fe2d88"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "facts_indicatori_economici",
        sa.Column(
            "FREQ",
            sa.String(50),
            sa.ForeignKey("dim_cl_freq.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "REF_AREA",
            sa.String(50),
            sa.ForeignKey("dim_cl_itter107.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "DATA_TYPE",
            sa.String(50),
            sa.ForeignKey("dim_cl_tipo_dato29.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "ECON_ACTIVITY_NACE_2007",
            sa.String(50),
            sa.ForeignKey("dim_cl_ateco_2007.id", ondelete="CASCADE"),
        ),
        sa.Column(
            "TIME_PERIOD",
            sa.String(10),
        ),
        sa.Column(
            "OBS_VALUE",
            sa.FLOAT(),
        ),
    )


def downgrade() -> None:
    op.drop_table("facts_indicatori_economici")
