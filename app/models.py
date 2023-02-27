from django.db import models

# Create your models here.

# CLASE ESTADOS
# class Estado(models.Model):
#     descripcion = models.CharField(max_length=20, null=False, blank=False)
#     def __str__(self) -> str:
#         return super().__str__()

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    id_cli = models.OneToOneField('Empresa', models.DO_NOTHING, db_column='id_cli', primary_key=True)
    fk_id_emp = models.IntegerField()
    nombre = models.CharField(max_length=128)
    cedula = models.IntegerField()
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    siglas = models.CharField(max_length=2)
    direccion = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    sitio = models.CharField(max_length=128)
    mensaje = models.CharField(max_length=128)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'empresa'


class Modulo(models.Model):
    id_mod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'modulo'


class Sistema(models.Model):
    id_sis = models.AutoField(primary_key=True)
    tipo = models.IntegerField()
    espera = models.IntegerField()
    tiempo = models.TimeField()
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sistema'


class Tramites(models.Model):
    id_tra = models.OneToOneField('Turnos', models.DO_NOTHING, db_column='id_tra', primary_key=True)
    fk_id_turnos = models.IntegerField()
    fk_id_mod = models.IntegerField()
    nombre = models.CharField(max_length=128)
    siglas = models.CharField(max_length=2)
    prioridad = models.IntegerField()
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tramites'


class Turnos(models.Model):
    id_turnos = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='id_turnos', primary_key=True)
    fk_id_cli = models.IntegerField()
    nombre = models.CharField(max_length=128)
    tiem_esp = models.TimeField()
    tiem_ate = models.TimeField()
    anulado = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'turnos'


class Usuario(models.Model):
    id = models.OneToOneField(Empresa, models.DO_NOTHING, db_column='id', primary_key=True)
    fk_id_emp = models.IntegerField()
    fk_id_sis = models.IntegerField()
    nombre = models.CharField(max_length=128)
    cedula = models.IntegerField()
    email = models.CharField(max_length=40)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuario'