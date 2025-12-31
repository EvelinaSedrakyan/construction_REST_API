"""Add index on project budget

Revision ID: 2c964c2f6ba2
Revises: f25a8669188e
Create Date: 2025-12-30 18:04:40.594487

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2c964c2f6ba2'
down_revision = 'f25a8669188e'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index(
        'ix_projects_budget',
        'projects',
        ['budget']
    )

def downgrade():
    op.drop_index(
        'ix_projects_budget',
        table_name='projects'
    )
