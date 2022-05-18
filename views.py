
import email
import bcrypt
from flask_login import LoginManager, UserMixin,current_user,login_manager
from flask import Flask, redirect, render_template, request,flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField
from wtforms.validators import DataRequired
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from wtforms import StringField,SubmitField,PasswordField,FileField,TextAreaField,EmailField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
from flask_login import UserMixin,login_manager, login_required,login_user,logout_user,LoginManager,current_user
from flask_mail import Message , Mail
import os
from flask import render_template
from  quote import  quote
from quote import request
from werkzeug.utils import secure_filename


from crypt import methods
# from quote import app 

from email.mime import image

from flask_login import LoginManager, UserMixin,current_user,login_manager

from flask import Flask, redirect, render_template, request,flash, session, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField
from wtforms.validators import DataRequired
# from flask_migrate import Migrate

from wtforms import StringField,SubmitField,PasswordField,FileField,TextAreaField,EmailField
from wtforms.validators import DataRequired

import os





app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY']='my secrecte key'


app.config["UPLOAD_FOLDER"]="static/uploads"
app.config["MAIL_DEFAULT_SENDER"]="brian108otieno@gmail.com"
app.config["MAIL_USERNAME"]="brian108otieno@gmail.com"
app.config["MAIL_PORT"]= 465
app.config["MAIL_SERVER"]='smtp.gmail.com', 465
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=True
app.config['MAIL_USERNAME']=os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD']=os.environ.get('EMAIL_PASS')





mail=Mail(app)
mail=Mail(app)




bcrypt=Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)




class posts(db.Model):
    id = db.Column(db.String, primary_key = True)
    blogs = db.Column(db.String(50) , primary_key = False)
    post = db.Column(db.String(50), primary_key = False)



class postss(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(25),nullable =False) 
    post = db.Column(db.String(50),nullable =False)
 

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    post=db.Column(db.String(700),nullable=False)
    poster=db.Column(db.Integer,db.ForeignKey('user.id'))






class UserForm (FlaskForm) :
    post = StringField(' enter title of your post',validators = [DataRequired()])
    title = StringField('Enter your blogpostpost here',validators = [DataRequired()])
   
    submit = SubmitField('submit')




# class User(db.Model,UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     username=db.Column(db.String(40),nullable=False)
#     email=db.Column(db.String(40),nullable=False)
#     password=db.Column(db.String(40),nullable=False)
#     # postman=db.relationship('Post',backref="postman")

class UpdateForm(FlaskForm) :   
    name = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    cnfpass=PasswordField("Confirm Password",validators=[DataRequired()])
    submit = SubmitField('login')




class RegisterFrm(FlaskForm):
    name=StringField("username",validators=[DataRequired()])
    email=EmailField("Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    cnfpass=PasswordField("Confirm Password",validators=[DataRequired()])
    submt=SubmitField('Register')

  




class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    password=db.Column(db.String(40),nullable=False)
    postman=db.relationship('Post',backref="postman")



class Images(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    uploader_id=db.Column(db.Integer,db.ForeignKey('user.id'))


class UploadForm(FlaskForm):
    file=FileField('Appartment',validators=[DataRequired()])
    submt=SubmitField('Upload Now')    






@app.route('/register',methods=['POST','GET'])
def register():
    frm=RegisterFrm()
    if frm.validate_on_submit():
        if frm.cnfpass.data==frm.cnfpass.data:
         hash_pwd = bcrypt.generate_password_hash(frm.password.data)
         hash_pwd=bcrypt.generate_password_hash(frm.password.data)
         user = User(username = frm.name.data,password = hash_pwd, email = frm.email.data)
         newuser= User(username=frm.name.data,email=frm.email.data,password=hash_pwd)
         session['name']= frm.name.data
         db.session.add(user)
         db.session.add(newuser)
         db.session.commit()
         msg=Message(subject=" POSTER APP REGISTRATION",recipients=[frm.email.data],body=frm.name.data+" Thank you for registering")
         mail.send('msg')
        
         
            # return redirect(url_for('login'))
        
    return render_template('register.html',form=frm)



@app.route('/login', methods = ['POST','GET'])
def login():
    updateUser =UpdateForm()
  
    if updateUser.validate_on_submit():
        if updateUser.cnfpass.data==updateUser.password.data:
           hash_pwd = bcrypt.generate_password_hash(updateUser.password.data)
        user = User(username = updateUser.data, email = updateUser.data, password = hash_pwd)
        session['name'] = updateUser.name.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('display'))

    return render_template('login.html', form = updateUser)
   



@app.route('/display')
def display():
    qr_all = postss.query.all()

    return render_template('display.html', data = qr_all)





@app.route('/update', methods = ['POST','GET'])
def index():

    dataForm =UserForm()


    if dataForm.validate_on_submit():
        addpost = postss(post = dataForm.post.data, title = dataForm.title.data)
        db.session.add(addpost)
        db.session.commit()

        return redirect(url_for('display'))
    return render_template('update.html',form = dataForm)    

# trace


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




@app.route("/image",methods=["POST","GET"])
def uploadimage():
    # user=current_user
    frm=UploadForm()
    if frm.validate_on_submit():
        file=request.files["file"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],secure_filename(file.filename)))
        upload=Images(name=secure_filename(file.filename))
        db.session.add(upload)
        db.session.commit()
        return redirect(url_for("viewimage"))
    return render_template("image.html",form=frm)




    

@app.route("/allimages",methods=["POST","GET"])
def viewallimages():
    allimages=Images.query.all()
    return render_template("allimages.html",images=allimages)

@app.route("/viewimage",methods=["POST","GET"])
def viewimage():
    allimages=Images.query.all()
    return render_template("imageview.html",images = allimages)

@app.route('/')
def home():
    quotes=[]
    req=request.Request()
    data=req.request("http://quotes.stormconsultancy.co.uk/random.json",500)
    quotes.append(quote.Quote(data["id"],data["quote"],data["author"]))
        


    return render_template('index.html',datum=quotes ,)




#trace



# if __name__=='__main__':
#     app.run(debug=1)




