"""empty message

Revision ID: fd89e72cc232
Revises: b575156bdecc
Create Date: 2017-05-02 16:10:22.686888

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fd89e72cc232'
down_revision = 'b575156bdecc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contas', sa.Column('valor_fora_ponta', sa.Float(), nullable=False))
    op.add_column('contas', sa.Column('valor_hora_ponta', sa.Float(), nullable=False))
    op.add_column('contas', sa.Column('valor_total', sa.Float(), nullable=False))
    op.drop_column('contas', 'valor')
    op.drop_index('idx_unidadesconsumidoras_localizacao', table_name='unidadesconsumidoras')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_unidadesconsumidoras_localizacao', 'unidadesconsumidoras', ['localizacao'], unique=False)
    op.add_column('contas', sa.Column('valor', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_column('contas', 'valor_total')
    op.drop_column('contas', 'valor_hora_ponta')
    op.drop_column('contas', 'valor_fora_ponta')
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint(u'(srid > 0) AND (srid <= 998999)', name=u'spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    )
    # ### end Alembic commands ###