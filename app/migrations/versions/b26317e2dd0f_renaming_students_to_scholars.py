"""Renaming students to scholars

Revision ID: b26317e2dd0f
Revises: 361dae855898
Create Date: 2022-12-11 17:44:51.420141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26317e2dd0f'
down_revision = '361dae855898'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')