from flask import *
import sqlite3
import json

def get_profil():
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM profil;")
    data = [{
        "id"    :data[0],
        "nama"  :data[1],
        "kab"   :data[2],
        "alamat"   :data[3],
        "telepon"  :data[4]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_detail():
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM detail;")
    data = [{
        "id"    :data[0],
        "jenis"  :data[1],
        "kelas"   :data[2],
        "status"   :data[3],
        "kepemilikan"  :data[4],
        "direktur"  :data[5],
        "luas tanah"  :data[6],
        "luas bangunan"  :data[7]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_layanan():
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM layanan;")
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "pelayanan"   :data[2]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_bed():
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM tempat_tidur;")
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "kelas"   :data[2],
        "jumlah"   :data[3]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_tenaga():
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM tenaga;")
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "grup"   :data[2],
        "sdm"   :data[3],
        "jumlah"  :data[4]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_by_idProfil(profil_id):
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute(f'''SELECT * FROM profil WHERE Id = {profil_id};''')
    data = [{
        "id"    :data[0],
        "nama"  :data[1],
        "kab"   :data[2],
        "alamat"   :data[3],
        "telepon"  :data[4]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_by_idDetail(detail_id):
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute(f'''SELECT * FROM detail WHERE Id = {detail_id};''')
    data = [{
        "id"    :data[0],
        "jenis"  :data[1],
        "kelas"   :data[2],
        "status"   :data[3],
        "kepemilikan"  :data[4],
        "direktur"  :data[5],
        "luas tanah"  :data[6],
        "luas bangunan"  :data[7]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_by_idLayanan(layanan_id):
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute(f'''SELECT * FROM layanan WHERE Id = {layanan_id};''')
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "pelayanan"   :data[2]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_by_idBed(bed_id):
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute(f'''SELECT * FROM tempat_tidur WHERE Id = {bed_id};''')
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "kelas"   :data[2],
        "jumlah"   :data[3]
    } for data in query]
    return make_response(jsonify(data), 200)

def get_by_idTenaga(tenaga_id):
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    query = cur.execute(f'''SELECT * FROM tenaga WHERE Id = {tenaga_id};''')
    data = [{
        "id"    :data[0],
        "nomor"  :data[1],
        "grup"   :data[2],
        "sdm"   :data[3],
        "jumlah"  :data[4]
    } for data in query]
    return make_response(jsonify(data), 200)

def updateProfil(profil_id):
    data = request.get_json()
    nama = data["nama"]
    kab  = data["kab"]
    alamat  = data["alamat"]
    telepon  = data["telepon"]
    conn = sqlite3.connect("ppb.sqlite")
    cur  = conn.cursor()
    query= cur.execute('''UPDATE profil SET Nama=?, Kab=?, Alamat=?, Telepon=? WHERE Id =?;''', (nama, kab, alamat, telepon, profil_id))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def updateDetail(detail_id):
    data = request.get_json()
    jenis = data["jenis"]
    kelas  = data["kelas"]
    status  = data["status"]
    kepemilikan  = data["kepemilikan"]
    direktur = data["direktur"]
    luas_tanah  = data["luas tanah"]
    luas_bangunan  = data["luas bangunan"]
    conn = sqlite3.connect("ppb.sqlite")
    cur  = conn.cursor()
    query= cur.execute('''UPDATE detail SET Jenis=?, Kelas=?, Status=?, Kepemilikan=?, Direktur=?, Luas_Tanah=?, Luas_Bangunan=? WHERE Id =?;''', (jenis, kelas, status, kepemilikan, direktur, luas_tanah, luas_bangunan, detail_id))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def updateLayanan(layanan_id):
    data = request.get_json()
    nomor = str(data["nomor"])
    pelayanan = str(data["pelayanan"])
    conn = sqlite3.connect("ppb.sqlite")
    cur  = conn.cursor()
    query= cur.execute('''UPDATE layanan SET Nomor=?, Pelayanan=? WHERE Id =?;''', (nomor, pelayanan, layanan_id))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def updateBed(bed_id):
    data = request.get_json()
    nomor = str(data["nomor"])
    kelas  = str(data["kelas"])
    jumlah  = str(data["jumlah"])
    conn = sqlite3.connect("ppb.sqlite")
    cur  = conn.cursor()
    query= cur.execute('''UPDATE tempat_tidur SET Nomor=?, Kelas=?, Jumlah=? WHERE Id =?;''', (nomor, kelas, jumlah, bed_id))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def updateTenaga (tenaga_id):
    data = request.get_json()
    nomor = str(data["nomor"])
    grup  = str(data["grup"])
    sdm  = str(data["sdm"])
    jumlah = str(data["jumlah"])
    conn = sqlite3.connect("ppb.sqlite")
    cur  = conn.cursor()
    query= cur.execute('''UPDATE tenaga SET Nomor=?, Grup=?, SDM=?, Jumlah=? WHERE Id =?;''', (nomor, grup, sdm, jumlah, tenaga_id))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def deleteProfil(profil_id):
    conn  = sqlite3.connect("ppb.sqlite")
    cur   = conn.cursor()
    query = cur.execute(f'''DELETE FROM profil WHERE Id = {profil_id};''')
    conn.commit()
    return make_response(jsonify({"result": True}), 201)

def deleteDetail(detail_id):
    conn  = sqlite3.connect("ppb.sqlite")
    cur   = conn.cursor()
    query = cur.execute(f'''DELETE FROM detail WHERE Id = {detail_id};''')
    conn.commit()
    return make_response(jsonify({"result": True}), 201)

def deleteLayanan(layanan_id):
    conn  = sqlite3.connect("ppb.sqlite")
    cur   = conn.cursor()
    query = cur.execute(f'''DELETE FROM layanan WHERE Id = {layanan_id};''')
    conn.commit()
    return make_response(jsonify({"result": True}), 201)

def deleteBed(bed_id):
    conn  = sqlite3.connect("ppb.sqlite")
    cur   = conn.cursor()
    query = cur.execute(f'''DELETE FROM tempat_tidur WHERE Id = {bed_id};''')
    conn.commit()
    return make_response(jsonify({"result": True}), 201)

def deleteTenaga(tenaga_id):
    conn  = sqlite3.connect("ppb.sqlite")
    cur   = conn.cursor()
    query = cur.execute(f'''DELETE FROM tenaga WHERE Id = {tenaga_id};''')
    conn.commit()
    return make_response(jsonify({"result": True}), 201)

def postProfil():
    data = request.get_json()
    nama = data["nama"]
    kab  = data["kab"]
    alamat  = data["alamat"]
    telepon  = data["telepon"]
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    cur.execute(
        '''INSERT INTO profil (Nama, Kab, Alamat, Telepon) VALUES (?, ?, ?, ?)''',
        (nama, kab, alamat, telepon))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def postDetail():
    data = request.get_json()
    jenis = data["jenis"]
    kelas  = data["kelas"]
    status  = data["status"]
    kepemilikan  = data["kepemilikan"]
    direktur = data["direktur"]
    luas_tanah  = data["luas tanah"]
    luas_bangunan  = data["luas bangunan"]
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    cur.execute(
        '''INSERT INTO detail (Jenis, Kelas, Status, Kepemilikan, Direktur, Luas_Tanah, Luas_Bangunan) VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (jenis, kelas, status, kepemilikan, direktur, luas_tanah, luas_bangunan))
    conn.commit()
    
    return make_response(jsonify({"result": True}), 200)

def postLayanan():
    data = request.get_json()
    nomor = str(data["nomor"])
    pelayanan = str(data["pelayanan"])
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    cur.execute(
        '''INSERT INTO layanan (Nomor, Pelayanan) VALUES (?, ?)''',
        (nomor, pelayanan))
    conn.commit()

    return make_response(jsonify({"result": True}), 200)

def postBed():
    data = request.get_json()
    nomor = str(data["nomor"])
    kelas  = str(data["kelas"])
    jumlah  = str(data["jumlah"])
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    cur.execute(
        '''INSERT INTO tempat_tidur (Nomor, Kelas, Jumlah) VALUES (?, ?, ?)''',
        (nomor, kelas, jumlah))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)

def postTenaga():
    data = request.get_json()
    nomor = str(data["nomor"])
    grup  = str(data["grup"])
    sdm  = str(data["sdm"])
    jumlah = str(data["jumlah"])
    conn = sqlite3.connect("ppb.sqlite")
    cur = conn.cursor()
    cur.execute(
                '''INSERT INTO tenaga (Nomor, Grup, SDM, Jumlah) VALUES (?, ?, ?, ?)''',
                (nomor, grup, sdm, jumlah))
    conn.commit()
    return make_response(jsonify({"result": True}), 200)