"""Create User model

Revision ID: 566c1bf537b6
Revises: 
Create Date: 2022-05-16 17:58:39.955985

"""
from alembic import op
import sqlalchemy as sa


revision = '566c1bf537b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('usermodel',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),  
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('usermodel')
