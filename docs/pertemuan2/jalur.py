peta = {
             'Dumai': ['Duri'],
             'Duri': ['Pasar Minggu'],
             'Pasar Minggu': ['Kandis'],
             'Kandis': ['Minas'],
             'Minas': ['Pekanbaru'],
             'Pekanbaru': ['Minas'],
             'Minas': ['Kandis'],
             'Kandis': ['Pasar Minggu'],
             'Pasar Minggu': ['Duri'],
             'Duri': ['Dumai'],
             'Dumai': ['Duri']
        }

def mencari_jalur_terpendek(peta, jalanawal, jalantujuan, jalur=[]):
        jalur = jalur + [jalanawal]
        if jalanawal == jalantujuan:
            return jalur
            if not peta.has_key(jalanawal):
                    return None
        jalurpendek = None
        for node in peta[jalanawal]:
            if node not in jalur:
                newjalur = mencari_jalur_terpendek(peta, node, jalantujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
    
print("Jalur Dari Dumai Sampai Pekanbaru")
print("(Dumai,Duri,Pasar Minggu,Kandis,Minas,Pekanbaru)")
print("\n")
jalanawal = raw_input("Masukan Daerah Asal : ")
jalantujuan = raw_input("Masukan Daerah Tujuan : ")
hasil = mencari_jalur_terpendek(peta, jalanawal, jalantujuan, jalur=[])
print "Jalur Terpendek", hasil