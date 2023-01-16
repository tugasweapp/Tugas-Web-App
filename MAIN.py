import streamlit as st

tab1, tab2, tab3 = st.tabs(["Identitas", "Menu", "Survei"])

with tab1:
    from PIL import Image
    image = Image.open ('Logo.jpeg')
    st.image (image, caption='Math App by Syahri')
    
    st.title ('Selamat Datang di Web Kelompok 5')
    st.header ('Web Math App')

    st.subheader ('Abdul Dzaky')
    st.subheader ('Annisa Nur Fadhilah')
    st.subheader ('Putri Meilani Syam')
    st.subheader ('Syahri Safitra Kelimutu')
    st.subheader ('Syahrizal Tri Rahadian')

#Menu Pilihan
with tab2:
    add_selectbox = st.selectbox ("Menu", ("Bangun Ruang", "Bangun Datar"))
        
    if (add_selectbox == "Bangun Ruang"):
        option = st.selectbox ('Menu Bangun Ruang', ('Kubus', 'Balok', 'Prisma', 'Limas', 'Tabung', 'Kerucut', 'Bola'))
    else:
        option = st.selectbox ('Menu Bangun Datar', ('Persegi', 'Persegi Panjang', 'Segitiga Sama Sisi', 'Lingkaran', 'Belah Ketupat', 'Layang-Layang','Jajar Genjang','Trapesium'))
            
#Menu Bangun Ruang
    if (option == 'Kubus'):
        st.title ('Kubus')
        option = st.selectbox ("Pilih",("Luas","Volume"))
        
        if (option == "Luas"):
            st.title ('Hitung Luas Kubus')
            #Luas Kubus
            st.latex (r'''6*(Sisi*Sisi)''')
            Sisi = st.number_input ("Masukkan nilai sisi")
            tombol = st.button ("Hitung Nilai Luas Kubus")

            if tombol:
               nilai_luas_kubus = 6*(Sisi*Sisi)
               st.success (f"Nilai Luas Kubus adalah {nilai_luas_kubus}")
               st.snow ()      
    
        else:
            st.title ('Hitung Volume Kubus')
            #Volume Kubus
            st.latex (r'''Sisi*Sisi*Sisi''')
            Sisis = st.number_input ("Masukkan nilai sisi")
            tombol = st.button ("Hitung nilai volume kubus")

            if tombol:
                nilai_volume_kubus = Sisis*Sisis*Sisis
                st.success (f"Nilai Volume Kubus adalah {nilai_volume_kubus}")
                st.snow()
            
    elif (option == 'Balok'):
        st.title ('Balok')
        option = st.selectbox ("Pilih",("Luas","Volume"))
    
        if (option == "Luas"):
            st.title ('Hitung Luas Balok')
            #Luas Balok
            st.latex (r'''2*((Panjang*Lebar)+(Lebar*Tinggi)+(Panjang*Tinggi))''')
            Panjang = st.number_input ("Masukkan nilai panjang")
            Lebar = st.number_input ("Masukkan nilai lebar")
            Tinggi = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Luas Balok")

            if tombol:
                nilai_luas_balok = 2*((Panjang*Lebar)+(Lebar*Tinggi)+(Panjang*Tinggi))
                st.success (f"Nilai Luas Balok adalah {nilai_luas_balok}")
                st.snow()
            
        else:
            st.title ('Hitung Volume Balok')
            #Volume Balok
            st.latex (r''' Panjang*Lebar*Tinggi ''')
            Panjangg = st.number_input ("Masukkan nilai panjang")
            Lebarr = st.number_input ("Masukkan nilai lebar")
            Tinggii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung nilai volume balok")

            if tombol:
                nilai_volume_balok = Panjangg*Lebarr*Tinggii
                st.success (f"Nilai Volume Balok adalah {nilai_volume_balok}")
                st.snow()
    
    elif (option == 'Prisma'):
        st.title ('Prisma')
        option = st.selectbox("Pilih",("Luas","Volume"))
    
        if (option == "Luas"):
            st.title ('Hitung Luas Prisma')
            #Luas Prisma
            st.latex (r'''(KelilingSisiAlas*Tinggi)+(2*LuasSisiAlas)''')
            Kelilingsisialas = st.number_input ("Masukkan nilai keliling sisi alas")
            Tinggiii = st.number_input ("Masukkan nilai tinggi")
            Luassisialas = st.number_input ("Masukkan nilai luas sisi alas")
            tombol = st.button ("Hitung Nilai Luas Prisma")

            if tombol:
                nilai_luas_prisma = (Kelilingsisialas*Tinggiii)+(2*Luassisialas)
                st.success (f"Nilai Luas Prisma adalah {nilai_luas_prisma}")
                st.snow()
            
        else:
            st.title ('Hitung Volume Prisma')
            #Volume Prisma
            st.latex (r'''LuasSisiAlas*Tinggi''')
            Luassisialass = st.number_input ("Masukkan nilai luas sisi alas")
            Tinggiiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung nilai volume prisma")

            if tombol:
                nilai_volume_prisma = Luassisialass*Tinggiiii
                st.success (f"Nilai Volume Prisma adalah {nilai_volume_prisma}")
                st.snow()
            
    elif (option == 'Limas'):
        st.title ('Limas')
        option = st.selectbox ("Pilih",("Luas","Volume"))          
    
        if (option == "Luas"):
            st.title ('Hitung Luas Limas')
            #Luas Limas
            st.latex (r'''LuasSisiAlas+LuasSeluruhSisiTegak''')
            Luassisialasss = st.number_input ("Masukkan nilai luas sisi alas")
            Luasseluruhsisitegak = st.number_input ("Masukkan nilai luas seluruh sisi tegak")
            tombol = st.button ("Hitung Nilai Luas Limas")

            if tombol:
                nilai_luas_limas = Luassisialasss+Luasseluruhsisitegak
                st.success (f"Nilai Luas Limas adalah {nilai_luas_limas}")
                st.snow()
    
        else:
            st.title ('Hitung Volume Limas')
            #Volume Limas
            st.latex (r'''1/3*LuasAlas*Tinggi''')
            Luasalas = st.number_input ("Masukkan nilai luas alas")
            Tinggiiiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung nilai volume limas")

            if tombol:
                nilai_volume_limas = 1/3*Luasalas*Tinggiiiii
                st.success (f"Nilai Volume Limas adalah {nilai_volume_limas}")
                st.snow()

    elif (option == 'Tabung'):
        st.title ('Tabung')
        option = st.selectbox("Pilih",("Luas","Volume"))      
            
        if (option == "Luas"):
            st.title ('Hitung Luas Tabung')
            #Luas Tabung
            st.latex (r'''(2*LuasAlas)+(KelilingAlas*Tinggi)''')
            Luasalass = st.number_input ("Masukkan nilai luas alas")
            Kelilingalas = st.number_input ("Masukkan nilai keliling alas")
            Tinggiiiiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Luas Tabung")

            if tombol:
                nilai_luas_tabung = (2*Luasalass)+(Kelilingalas*Tinggiiiiii)
                st.success (f"Nilai Luas tabung adalah {nilai_luas_tabung}")
                st.snow()
            
        else:
            st.title ('Hitung Volume Tabung')
            #Volume Tabung
            st.latex (r'''3.14*(Jari-jari)^2*Tinggi''')
            Jarijari = st.number_input ("Masukkan nilai jari-jari")
            Tiinggiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung nilai Volume Tabung")

            if tombol:
                nilai_volume_tabung = 3.14*Jarijari*Jarijari*Tiinggiii
                st.success (f"Nilai Volume Tabung adalah {nilai_volume_tabung}")
                st.snow()
    
    elif (option == 'Kerucut'):
        st.title ('Kerucut')
        option = st.selectbox("Pilih",("Luas","Volume")) 
    
        if (option == "Luas"):
            st.title ('Hitung Luas Kerucut')
            #Luas Kerucut
            st.latex (r'''(3.14*(Jari-Jari)^2)+(3.14*Jari-Jari*Garis Pelukis)''') 
            Jarijarii = st.number_input ("Masukkan nilai luas jari-jari")
            S = st.number_input ("Masukkan nilai garis pelukis")
            tombol = st.button ("Hitung Nilai Luas Kerucut")

            if tombol:
                nilai_luas_kerucut = (3.14*Jarijarii*Jarijarii)+(3.14*Jarijarii*S)
                st.success (f"Nilai Luas kerucut adalah {nilai_luas_kerucut}")
                st.snow()
            
        else:
            st.title ('Hitung Volume Kerucut')
            #Volume Kerucut
            st.latex (r'''1/3*3.14*(Jari-jari)^3*Tinggi''')
            Jarijariii = st.number_input("Masukkan nilai jari-jari")
            Tinggiiiiiiii = st.number_input("Masukkan nilai tinggi")
            tombol = st.button("Hitung nilai Volume Tabung")

            if tombol:
                nilai_volume_kerucut = 1/3*3.14*Jarijariii*Jarijariii*Jarijariii*Tinggiiiiiiii
                st.success (f"Nilai Volume Kerucut adalah {round (nilai_volume_kerucut, 2)}")
                st.snow()    
            
    elif (option == 'Bola'):
        st.title ('Bola')
        option = st.selectbox("Pilih",("Luas","Volume"))         
         
        if (option == "Luas"):
            st.title ('Hitung Luas Bola')
            #Luas Bola
            st.latex (r'''4*3.14*(jari-jari)^2''') 
            Jarijariiii = st.number_input ("Masukkan nilai jari-jari")
            tombol = st.button ("Hitung Nilai Luas Bola")

            if tombol:
                nilai_luas_bola = 4*3.14*Jarijariiii*Jarijariiii
                st.success (f"Nilai Luas bola adalah {round (nilai_luas_bola, 2)}")
                st.snow()
        
        else:
            st.title ('Hitung Volume Bola')
            #Volume Bola
            st.latex (r'''4/3*3.14*(Jari-jari)^3''')
            Jarijariiiii = st.number_input ("Masukkan nilai jari-jari")
            tombol = st.button("Hitung nilai Volume Bola")

            if tombol:
                nilai_volume_bola = 4/3*3.14*Jarijariiiii*Jarijariiiii*Jarijariiiii
                st.success (f"Nilai Volume Bola adalah {round (nilai_volume_bola, 2)}")
                st.snow()       
    

#Menu Bangun Datar
    if (option == 'Persegi'):
        st.title ('Persegi')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ('Hitung Luas Persegi')
            #Luas Persegi
            st.latex (r'''Sisi*Sisi''')
            Sisiss = st.number_input ("Masukkan nilai sisi ")
            tombol = st.button ("Hitung Nilai Luas Persegi")

            if tombol:
                nilai_luas_persegi = Sisiss*Sisiss
                st.success (f"Nilai Luas Persegi adalah {nilai_luas_persegi}")
                st.snow()
            
        else:
            st.title ('Hitung Keliling Persegi')
            #Keliling Persegi
            st.latex (r'''4*Sisi''')
            Sisisss = st.number_input ("Masukkan nilai sisi")
            tombol = st.button ("Hitung nilai Keliling Persegi")

            if tombol:
                nilai_keliling_persegi = 4*Sisisss
                st.success (f"Nilai Keliling Persegi adalah {nilai_keliling_persegi}")
                st.snow()
            
    elif (option == 'Persegi Panjang'):
        st.title ('Persegi Panjang')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ("Hitung Luas Persegi Panjang")
            #Luas Persegi Panjang
            st.latex (r'''Panjang*Lebar''')
            Panjanggg = st.number_input ("Masukkan nilai panjang")
            Lebarrr = st.number_input ("Masukkan nilai lebar")
            tombol = st.button ("Hitung Nilai Luas Persegi Panjang")
        
            if tombol:
                nilai_luas_persegi_panjang = Panjanggg*Lebarrr
                st.success (f"Nilai Luas Persegi Panjang adalah {nilai_luas_persegi_panjang}")
                st.snow()
        else:
            st.title ("Hitung Keliling Persegi Panjang")
            #Keliling Persegi Panjang
            st.latex (r'''2*(Panjang+Lebar)''')
            Panjangggg = st.number_input ("Masukkan nilai panjang")
            Lebarrrr = st.number_input ("Masukkan nilai lebar")
            tombol = st.button ("Hitung Nilai Keliling Persegi Panjang")
        
            if tombol:
                nilai_keliling_persegi_panjang = 2*(Panjangggg+Lebarrrr)
                st.success(f"Nilai Keliling Persegi Panjang adalah {nilai_keliling_persegi_panjang}")
                st.snow()

    elif (option == 'Segitiga Sama Sisi'):
        st.title ('Segitiga Sama Sisi')
        option = st.selectbox("Pilih",("Luas","Keliling"))
        
        if (option == "Luas"):
            st.title ("Hitung Luas Segitiga")
            #Luas Segitiga
            st.latex (r'''(Alas*Tinggi)/2''')
            Alas = st.number_input ("Masukkan nilai alas")
            Tinggiiiiiiiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Luas Segitiga")
        
            if tombol:
                nilai_luas_segitiga = (Alas*Tinggiiiiiiiii)/2
                st.success (f"Nilai Luas Segitiga adalah {nilai_luas_segitiga}")
                st.snow()
        else:
            st.title ("Hitung Keliling Segitiga")
            #Keliling Segitiga
            st.latex (r'''Sisi*Sisi*Sisi''')
            Sisissss = st.number_input ("Masukkan nilai sisi")
            tombol = st.button ("Hitung Nilai Keliling Segitiga")
        
            if tombol:
                nilai_keliling_segitiga = Sisissss*Sisissss*Sisissss
                st.success (f"Nilai Keliling Segitiga adalah {nilai_keliling_segitiga}")
                st.snow()

    elif (option == 'Lingkaran'):
        st.title ('Lingkaran')
        option = st.selectbox("Pilih",("Luas","Keliling"))
        
        if (option == "Luas"):
            st.title ("Hitung Luas Lingkaran")
            #Luas Lingkaran
            st.latex (r'''3.14*(Jari-jari)^2''')
            Jarijariiiiii = st.number_input ("Masukkan nilai jari-jari")
            tombol = st.button ("Hitung Nilai Luas Lingkaran")
        
            if tombol:
                nilai_luas_lingkaran = 3.14*Jarijariiiiii*Jarijariiiiii
                st.success (f"Nilai Luas Lingkaran adalah {round (nilai_luas_lingkaran,2)}")
                st.snow()
        else:
            st.title ("Hitung Keliling Lingkaran")
            #Keliling Lingkaran
            st.latex (r'''3.14*Diameter''')
            Diameter = st.number_input ("Masukkan nilai diameter")
            tombol = st.button ("Hitung Nilai Keliling Lingkaran")
        
            if tombol:
                nilai_keliling_lingkaran = 3.14*Diameter
                st.success(f"Nilai Keliling Lingkaran adalah {round (nilai_keliling_lingkaran,2)}")
                st.snow()
                
    elif (option == 'Belah Ketupat'):
        st.title ('Belah Ketupat')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ("Hitung Luas Belah Ketupat")
            #Luas Belah Ketupat
            st.latex (r'''(Diameter1+Diameter2)/2''')
            Diameter1 = st.number_input ("Masukkan nilai Diameter1")
            Diameter2 = st.number_input ("Masukkan nilai Diameter2")
            tombol = st.button ("Hitung Nilai Luas Belah Ketupat")
        
            if tombol:
                nilai_luas_belah_ketupat = (Diameter1+Diameter2)/2
                st.success (f"Nilai Luas Belah Ketupat adalah {nilai_luas_belah_ketupat}")
                st.snow()
    
        else:
            st.title ("Hitung Keliling Belah Ketupat")
            #Keliling Belah Ketupat
            st.latex (r'''4*Sisi''')
            Sisisssss = st.number_input ("Masukkan nilai sisi")
            tombol = st.button ("Hitung Nilai Keliling Belah Ketupat")
        
            if tombol:
                nilai_keliling_belah_ketupat = 4*Sisisssss
                st.success (f"Nilai Keliling Belah Ketupat adalah {nilai_keliling_belah_ketupat}")
                st.snow()
            
    elif (option== 'Layang-Layang'):
        st.title ('Layang-Layang')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ("Hitung Luas Layang-Layang")
            #Luas Layang-Layang
            st.latex (r'''(Diameter1+Diameter2)/2''')
            Diameterr = st.number_input ("Masukkan nilai diameter1")
            Diameterrr = st.number_input ("Masukkan nilai diameter2")
            tombol = st.button ("Hitung Nilai Luas Layang-Layang")
        
            if tombol:
                nilai_luas_layang_layang = (Diameterr+Diameterrr)/2
                st.success (f"Nilai Luas Layang-Layang adalah {nilai_luas_layang_layang}")
                st.snow()
                
        else:
            st.title ("Hitung Keliling Layang-Layang")
            #Keliling Layang-Layang
            st.latex (r'''2*(Sisi1+Sisi2)''')
            Sisi1 = st.number_input ("Masukkan nilai sisi 1")
            Sisi2 = st.number_input ("Masukkan nilai sisi 2")
            tombol = st.button("Hitung Nilai Keliling Layang-Layang")
        
            if tombol:
                nilai_keliling_layang_layang = 2*(Sisi1+Sisi2)
                st.success (f"Nilai Keliling Layang-Layang adalah {nilai_keliling_layang_layang}")
                st.snow()
                
    elif (option == 'Jajar Genjang'):
        st.title ('Jajar Genjang')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ("Hitung Luas Jajar Genjang")
            #Luas Jajar Genjang
            st.latex (r'''Alas*Tinggi''')
            Alass = st.number_input ("Masukkan nilai alas")
            Tinggiiiiiiiiii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Luas Jajar Genjang")
        
            if tombol:
                nilai_luas_jajar_genjang = Alass*Tinggiiiiiiiiii
                st.success (f"Nilai Luas Jajar Genjang adalah {nilai_luas_jajar_genjang}")
                st.snow()
                
        else:
            st.title ("Hitung Keliling Jajar Genjang")
            #Keliling Jajar Genjang
            st.latex (r'''2*(Alas+SisiMiring)''')
            Alasss = st.number_input ("Masukkan nilai alas")
            Sisimiring = st.number_input ("Masukkan nilai sisi miring")
            tombol = st.button ("Hitung Nilai Keliling Jajar Genjang")
        
            if tombol:
                nilai_keliling_jajar_genjang = 2*(Alasss+Sisimiring)
                st.success (f"Nilai Keliling Jajar Genjang adalah {nilai_keliling_jajar_genjang}")
                st.snow()
                
    elif (option == 'Trapesium'):
        st.title ('Trapesium')
        option = st.selectbox("Pilih",("Luas","Keliling"))
    
        if (option == "Luas"):
            st.title ("Hitung Luas Trapesium")
            #Luas Trapesium
            st.latex (r'''((SisiBawah+SisiAtas)/2)*Tinggi''')
            Sisiatas = st.number_input ("Masukkan nilai sisi atas")
            Sisibawah = st.number_input ("Masukkan nilai sisi bawah")
            Tiinggi = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Luas Trapesium")
        
            if tombol:
                nilai_luas_trapesium = ((Sisibawah+Sisiatas)/2)*Tiinggi
                st.success (f"Nilai Luas Trapesium adalah {nilai_luas_trapesium}")
                st.snow()
                
        else:
            st.title ("Hitung Keliling Trapesium")
            #Keliling Trapesium
            st.latex (r'''SisiAtas+SisiBawah+SisiMiring+Tinggi''')
            Sisiatass = st.number_input ("Masukkan nilai sisi atas")
            Sisibawahh = st.number_input ("Masukkan nilai sisi bawah")
            Sisimiringg = st.number_input ("Masukkan nilai sisi miring")
            Tiinggii = st.number_input ("Masukkan nilai tinggi")
            tombol = st.button ("Hitung Nilai Keliling Trapesium")
        
            if tombol:
                nilai_keliling_trapesium = Sisiatass+Sisibawahh+Sisimiringg+Tiinggii
                st.success (f"Nilai Keliling Trapesium adalah {nilai_keliling_trapesium}")
                st.snow()       

with tab3:
    add_selectbox = st.selectbox ("Menu", ("Kritik", "Saran","Kepuasan"))
        
    if (add_selectbox == "Kritik"):
        Kritik = st.text_input ("Masukkan Kritik Anda")
    elif (add_selectbox == "Saran"):
        Saran = st.text_input ("Masukkan Saran Anda")
    else:
        Kepuasan = st.select_slider (
            'Menurut Anda bagaimana Web ini?',
            options=["Tidak Bermanfaat", "Cukup Bermanfaat", "Bermanfaat", "Sangat Bermanfaat"])

           
    