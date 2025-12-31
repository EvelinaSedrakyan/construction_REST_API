"""Add email and description columns

Revision ID: f25a8669188e
Revises: 
Create Date: 2025-12-30 18:02:15.875139

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f25a8669188e'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        'companies',
        sa.Column('email', sa.String(), nullable=True)
    )

    op.add_column(
        'projects',
        sa.Column('description', sa.Text(), nullable=True)
    )


def downgrade():
    op.drop_column('projects', 'description')
    op.drop_column('companies', 'email')
