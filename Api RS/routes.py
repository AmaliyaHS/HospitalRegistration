from flask import *
from functions import *

app = Flask(__name__)

@app.route("/profil", methods=["GET","POST"])
def profil():
    if request.method == "GET": return get_profil()
    else: return postProfil()

@app.route("/detail", methods=["GET","POST"])
def detail():
    if request.method == "GET": return get_detail()
    else: return postDetail()

@app.route("/layanan", methods=["GET","POST"])
def layanan():
    if request.method == "GET": return get_layanan()
    else: return postLayanan()

@app.route("/bed", methods=["GET","POST"])
def bed():
    if request.method == "GET": return get_bed()
    else: return postBed()

@app.route("/tenaga", methods=["GET","POST"])
def tenaga():
    if request.method == "GET": return get_tenaga()
    else: return postTenaga()

@app.route("/profil/<int:profil_id>", methods=["GET","DELETE","PUT"])
def profil_detail(profil_id):
    if request.method == "GET": return get_by_idProfil(profil_id)
    elif request.method == "DELETE": return deleteProfil(profil_id)
    else: return updateProfil(profil_id)

@app.route("/detail/<int:detail_id>", methods=["GET","DELETE","PUT"])
def detail_detail(detail_id):
    if request.method == "GET": return get_by_idDetail(detail_id)
    elif request.method == "DELETE": return deleteDetail(detail_id)
    else: return updateDetail(detail_id)

@app.route("/layanan/<int:layanan_id>", methods=["GET","DELETE","PUT"])
def layanan_detail(layanan_id):
    if request.method == "GET": return get_by_idLayanan(layanan_id)
    elif request.method == "DELETE": return deleteLayanan(layanan_id)
    else: return updateLayanan(layanan_id)

@app.route("/bed/<int:bed_id>", methods=["GET","DELETE","PUT"])
def bed_detail(bed_id):
    if request.method == "GET": return get_by_idBed(bed_id)
    elif request.method == "DELETE": return deleteBed(bed_id)
    else: return updateBed(bed_id)

@app.route("/tenaga/<int:tenaga_id>", methods=["GET","DELETE","PUT"])
def tenaga_detail(tenaga_id):
    if request.method == "GET": return get_by_idTenaga(tenaga_id)
    elif request.method == "DELETE": return deleteTenaga(tenaga_id)
    else: return updateTenaga(tenaga_id)

if __name__ == "__main__":
    app.run(debug=True)
