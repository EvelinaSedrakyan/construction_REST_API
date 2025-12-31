"""Add JSON metadata with GIN index

Revision ID: 79b313661682
Revises: 2c964c2f6ba2
Create Date: 2025-12-30 18:12:50.394874

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '79b313661682'
down_revision = '2c964c2f6ba2'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        'projects',
        sa.Column('metadata_json', sa.JSON(), nullable=True)
    )

    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")

    op.execute("""
        CREATE INDEX ix_projects_metadata_json_gin
        ON projects
        USING GIN (metadata_json jsonb_path_ops);
    """)

def downgrade():
    op.execute("DROP INDEX IF EXISTS ix_projects_metadata_json_gin;")
    op.drop_column('projects', 'metadata_json')
