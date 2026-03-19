from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import tempfile

app = Flask(__name__)


# -------- FORMULARIO --------
@app.route("/")
def form():
    return render_template("form.html")


# -------- GENERAR PDF --------
@app.route("/generar", methods=["POST"])
def generar():

    fecha = request.form["fecha"]
    cocinamos = request.form["Cocinamos"]
    viandas = request.form["viandas"]
    stock = request.form["stock"]
    comprar = request.form["comprar"]
    novedades = request.form["Novedades"]
    jornada = request.form["Jornada"]
    comentarios = request.form["Comentarios"]
    kits = request.form["Kits"]
    bidones = request.form["Bidones"]
    llaves = request.form["Llaves"]

    pdf = FPDF()
    pdf.add_page()

    # Titulo
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, "Minuta del Voluntariado", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Fecha: {fecha}", ln=True)

    pdf.ln(5)

    # Cocina
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Cocina", ln=True)

    pdf.set_font("Arial", "", 12)
    texto = f"El dia {fecha} cocinamos {cocinamos} y de eso se armaron {viandas} viandas."
    pdf.multi_cell(0, 8, texto)

    pdf.multi_cell(0, 8, f"Se utilizo del stock: {stock}")
    pdf.multi_cell(0, 8, f"Faltaria comprar: {comprar}")

    pdf.ln(5)

    # Actividad
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Actividad del dia", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"En el CC: {novedades}")
    pdf.multi_cell(0, 8, f"En la plaza: {jornada}")

    pdf.ln(5)

    # Entregas
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Entregas", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Kits entregados: {kits}")
    pdf.multi_cell(0, 8, f"Bidones de bebida servidos: {bidones}")

    pdf.ln(5)

    # Administracion
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Administracion", ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, f"Las llaves quedaron a cargo de: {llaves}")
    pdf.multi_cell(0, 8, f"Comentarios: {comentarios}")

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

    pdf.output(temp.name)

    return send_file(temp.name, as_attachment=True, download_name="minuta.pdf")


# -------- VER TEXTO PARA COPIAR --------
@app.route("/ver_texto", methods=["POST"])
def ver_texto():

    fecha = request.form["fecha"]
    cocinamos = request.form["Cocinamos"]
    viandas = request.form["viandas"]
    stock = request.form["stock"]
    comprar = request.form["comprar"]
    novedades = request.form["Novedades"]
    jornada = request.form["Jornada"]
    comentarios = request.form["Comentarios"]
    kits = request.form["Kits"]
    bidones = request.form["Bidones"]
    llaves = request.form["Llaves"]

    texto = f"""Cocina:

El día {fecha} cocinamos {cocinamos} y se pudieron armar {viandas} viandas, de ahí se utilizó {stock} y necesitaríamos comprar {comprar} ya que no hay más.

Actividad del día:

En el CC {novedades} y en la plaza {jornada}, hoy entregamos {kits} kits de higiene, y se sirvieron {bidones} bidones de jugo.

Administración:

Las llaves se las quedó {llaves} y {comentarios}
"""

    return render_template("texto.html", texto=texto)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)