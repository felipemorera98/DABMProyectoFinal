from flask import Flask,render_template,request
import mysql.connector



app=Flask(__name__,template_folder="templates")

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/datos_web",methods=['POST'])
def datos_web():
    users=[]
    user_path="templates/usuarios.csv"
    usuario=request.form["Usuario"]
    contraseña=request.form["Contraseña"]
    with open(user_path,"r") as file:
        for linea in file:
            users.append(linea.strip("\n"))

    login=f"{usuario},{contraseña}"

    if login in users:
        return render_template("datos.html",usuario=usuario)
    else:   
        return render_template("Error.html",usuario=usuario)


@app.route("/proyecto",methods=['POST'])
def proyecto():
    datos=[]
    datos=MYSQL_Leer()
    ID=int(request.form["ID"])-1
    P_Arterial=datos[ID][1]
    F_Cardiaca=datos[ID][2]
    F_Respiratoria=datos[ID][3]
    O_Sangre=datos[ID][4]
    EKG=datos[ID][5]
    return render_template("datos.html",P_Arterial=P_Arterial,F_Cardiaca=F_Cardiaca,F_Respiratoria=F_Respiratoria,O_Sangre=O_Sangre,EKG=EKG)

@app.route("/regresar_datos",methods=['POST'])
def regresar_datos():
    return render_template("inicio.html")


def MYSQL_Leer():
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_esp32")
    datos=[]
    cursor1=conexion1.cursor()
    tabla="select ID,P_Arterial,F_Cardiaca,F_Respiratoria,O_Sangre,EKG from `1101697027`"
    cursor1.execute(tabla)
    for fila in cursor1:
        datos.append(fila) 
    conexion1.close()
    return datos
    

if __name__=="__main__":
    app.run(debug=True)