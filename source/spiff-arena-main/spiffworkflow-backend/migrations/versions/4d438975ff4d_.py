"""empty message

Revision ID: 4d438975ff4d
Revises: 9d5b6c5c31a5
Create Date: 2023-09-21 16:25:44.574756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d438975ff4d'
down_revision = '9d5b6c5c31a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cache_generation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cache_table', sa.String(length=255), nullable=False),
    sa.Column('updated_at_in_seconds', sa.Integer(), nullable=True),
    sa.Column('created_at_in_seconds', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('cache_generation', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_cache_generation_cache_table'), ['cache_table'], unique=False)

    op.create_table('reference_cache',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('generation_id', sa.Integer(), nullable=False),
    sa.Column('identifier', sa.String(length=255), nullable=False),
    sa.Column('display_name', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('file_name', sa.String(length=255), nullable=False),
    sa.Column('relative_location', sa.String(length=255), nullable=False),
    sa.Column('properties', sa.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['generation_id'], ['cache_generation.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('generation_id', 'identifier', 'relative_location', 'type', name='reference_cache_uniq')
    )
    with op.batch_alter_table('reference_cache', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_reference_cache_display_name'), ['display_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_reference_cache_generation_id'), ['generation_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_reference_cache_identifier'), ['identifier'], unique=False)
        batch_op.create_index(batch_op.f('ix_reference_cache_relative_location'), ['relative_location'], unique=False)
        batch_op.create_index(batch_op.f('ix_reference_cache_type'), ['type'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reference_cache', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_reference_cache_type'))
        batch_op.drop_index(batch_op.f('ix_reference_cache_relative_location'))
        batch_op.drop_index(batch_op.f('ix_reference_cache_identifier'))
        batch_op.drop_index(batch_op.f('ix_reference_cache_generation_id'))
        batch_op.drop_index(batch_op.f('ix_reference_cache_display_name'))

    op.drop_table('reference_cache')
    with op.batch_alter_table('cache_generation', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cache_generation_cache_table'))

    op.drop_table('cache_generation')
    # ### end Alembic commands ###
