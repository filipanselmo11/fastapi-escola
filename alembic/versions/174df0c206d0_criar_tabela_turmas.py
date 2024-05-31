"""Criar tabela turmas

Revision ID: 174df0c206d0
Revises: 6f63cb369267
Create Date: 2024-05-31 10:42:57.575868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '174df0c206d0'
down_revision: Union[str, None] = '6f63cb369267'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('turmas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('serie', sa.String(length=30), nullable=True),
    sa.Column('codigo', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('turmas')
    # ### end Alembic commands ###