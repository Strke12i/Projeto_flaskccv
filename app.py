from flask import Flask,render_template,flash,redirect, url_for,request,send_from_directory
import os
from rede_neural import classificar
import random

app = Flask(__name__)


def fakehash(file):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y', 'Z']
    f=file[:-4]
    ext=file[-4:]
    i=0
    st=''
    while i<len(f):
        st+=alpha[random.randint(1,len(alpha)-1)]
        i+=1

    if ext=='jpeg':
        ext='.'+ext

    has=st+ext
    return has



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def grafico():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        name=fakehash(uploaded_file.filename)
        uploaded_file.save("static/images/"+name)
        anm=classificar("static/images/"+name)
        print(anm)
    return render_template('grafico.html',img="static/images/"+name,animal=anm)



if __name__=='__main__':
    app.run()
