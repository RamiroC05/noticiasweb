from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_ckeditor import CKEditor
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired,Email,EqualTo
from flask_mysqldb import MySQL
from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
#CONFIGURACION A LA BASE DE DATOS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12344567890'
app.config['MYSQL_DB'] = 'proyecto_noticias'

app.config['SECRET_KEY'] = 'your_secret_key_here'
ckeditor = CKEditor(app)
mysql=MySQL(app)

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

class PostForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion =  StringField('Descripcion', validators=[DataRequired()])
    categoria = SelectField('Categorias', coerce=int, validators=[DataRequired()])
    contenido = CKEditorField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Publicar')


@app.route('/')
def inicio():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM noticias"
    cursor.execute(sql)
    noticias = cursor.fetchall()
    cursor.close()
    return render_template('index.html', noticias = noticias)

@app.route('/cargar', methods=['GET', 'POST'])
def root():
    categorias = listanoticias()

    form = PostForm()
    form.categoria.choices = [(c[0], c[1]) for c in categorias]  

    if form.validate_on_submit():
        #ACÁ OBTENGO LOS DATOS DEL FORMULARIO
        titulo = form.titulo.data
        descripcion = form.descripcion.data
        contenido = clean_html(form.contenido.data)
        categoria_id = form.categoria.data
        
        #GUARDO LOS DATOS OBTENIDOS EN LA BASE DE DATOS
        cursor = mysql.connection.cursor()
        sql = ("INSERT INTO noticias (titulo, descripcion, contenido, id_cat_corresp) VALUES (%s,%s,%s,%s)")
        cursor.execute(sql, (titulo, descripcion, contenido, categoria_id))
        mysql.connection.commit()
        cursor.close


        return redirect(url_for('root'))
    return render_template('index.html', form=form, categorias=categorias)


#CONSULTA A LA BASE DE DATOS PARA LAS CATEGORIAS
def listanoticias():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM categorias"
    cursor.execute(sql)
    categorias = cursor.fetchall()
    return(categorias)

#SECCIÓN DE LOGIN Y REGISTRO
# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"  # Ruta para la página de inicio de sesión
login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."
login_manager.login_message_category = "info"

# Clase de usuario para Flask-Login
class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email

# Cargar usuario para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", [user_id])
    user = cursor.fetchone()
    if user:
        return User(user[0], user[1])
    return None

# Formulario de Registro
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirm', message='Las contraseñas no coinciden')])
    confirm = PasswordField('Confirmar Contraseña', validators=[DataRequired()])
    tipo_usuario = SelectField(
        'Tipo de Usuario',
        choices=[('Admin', 'Admin'), ('Editor', 'Editor'), ('Viewer', 'Viewer')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Registrarse')

# Formulario de Inicio de Sesión
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

# Ruta de Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        contraseña = generate_password_hash(form.contraseña.data)
        tipo_usuario = form.tipo_usuario.data
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO usuarios (email, contraseña) VALUES (%s, %s)", (email, contraseña,tipo_usuario))
        mysql.connection.commit()
        cursor.close()
        flash('Usuario registrado con éxito. Puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Ruta de Inicio de Sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        contraseña = form.password.data
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", [email])
        user = cursor.fetchone()
        cursor.close()
        
        if user and check_password_hash(user[2], contraseña):  # user[2] es la columna de la contraseña hash
            login_user(User(user[0], user[1]))  # user[0] es el ID, user[1] el email
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))  # Ir a la página de inicio o la ruta deseada
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
    
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
