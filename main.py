from flask import Flask, render_template, jsonify, request, redirect, url_for, send_from_directory
from flask_ckeditor import CKEditor
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask_ckeditor import CKEditorField, CKEditorField
from wtforms.validators import DataRequired
from flask_mysqldb import MySQL
from bs4 import BeautifulSoup
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif'}


app = Flask(__name__)
#CONFIGURACION A LA BASE DE DATOS
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'br1'
app.config['MYSQL_PASSWORD'] = '0724-852933bruno'
app.config['MYSQL_DB'] = 'proyecto_noticias'



app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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



@app.route('/', methods=['GET', 'POST'])
def root():
    categorias = listanoticias()
    titulos=listatitulos()

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
    return render_template('index.html', form=form, categorias=categorias, titulos=titulos)


#CONFIGURACION PARA MANEJAR LAS CARGAS DE ARCHIVOS DESDE CKEDITOR
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)  # Esto te mostrará qué archivos están llegando
    if 'upload' not in request.files:
        return jsonify({"uploaded": 0, "error": {"message": "No file part"}}), 400
    file = request.files['upload']
    if file.filename == '':
        return jsonify({"uploaded": 0, "error": {"message": "No selected file"}}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({
            "uploaded": 1,
            "fileName": filename,
            "url": url_for('uploaded_file', filename=filename, _external=True)
        })
    return jsonify({"uploaded": 0, "error": {"message": "Invalid file"}}), 400


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/noticia/<int:id>')
def noticia(id):
    noticia = obtener_noticia_por_id(id)
    return render_template('noticias_detalle.html', noticia=noticia)

def obtener_noticia_por_id(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM noticias WHERE idnoticias = %s"
    cursor.execute(query, (id,))
    noticia = cursor.fetchone()
    cursor.close()
    return noticia
#CONSULTA A LA BASE DE DATOS PARA LAS CATEGORIAS
def listanoticias():
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM categorias"
    cursor.execute(sql)
    categorias = cursor.fetchall()
    return(categorias)

def listatitulos():
    cursor = mysql.connection.cursor()
    titulos = "Select * from noticias"
    cursor.execute(titulos)
    titulos = cursor.fetchall()
    cursor.close()
    return (titulos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
