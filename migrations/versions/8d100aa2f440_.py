"""empty message

Revision ID: 8d100aa2f440
Revises: a5cffa318ac2
Create Date: 2025-03-24 11:22:34.611583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d100aa2f440'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('apellidos', sa.String(), nullable=False),
    sa.Column('ciudad', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('genero', sa.String(), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=False),
    sa.Column('altura', sa.Integer(), nullable=False),
    sa.Column('color_ojos', sa.String(), nullable=False),
    sa.Column('color_pelo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('clima', sa.String(), nullable=False),
    sa.Column('gravedad', sa.Integer(), nullable=False),
    sa.Column('terreno', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('personaje_favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Usuarios_id', sa.Integer(), nullable=False),
    sa.Column('personaje_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Usuarios_id'], ['Usuarios.id'], ),
    sa.ForeignKeyConstraint(['personaje_id'], ['personaje.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planeta_favorito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Usuarios_id', sa.Integer(), nullable=False),
    sa.Column('planeta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Usuarios_id'], ['Usuarios.id'], ),
    sa.ForeignKeyConstraint(['planeta_id'], ['planeta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('planeta_favorito')
    op.drop_table('personaje_favorito')
    op.drop_table('planeta')
    op.drop_table('personaje')
    op.drop_table('Usuarios')
    # ### end Alembic commands ###
