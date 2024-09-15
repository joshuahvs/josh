# JOSH

Link tautan menuju web: http://joshua-hans-joshapp2.pbp.cs.ui.ac.id/

# Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
1. Saya membuat repository github lalu saya melakukan cloning terhadap repo yang saya buat di github ke komputer lokal saya.
2. Setelah itu, saya menginstall dan menginisiasi proyek Django. Tapi, sebelum itu, saya mengaktifkan virtual environment untuk isolasi dependensi dan mempermudah pengolaan versi python.
3. Lalu saya menyiapkan dependensi yang dibutuhkan oleh proyek dalam sebuah file bernama requirements.txt dan menginstall semua dependensi tersebut.
4. Setelah itu, saya membuat menginisiasi proyek django dengan menjalankan perintah 'django-admin startproject josh_app .'
5. Setelah itu, saya mengedit ALLOWED_HOST agar saya dapat melihat hasil dari kode saya di local host komputer saya. 
6. Lalu, saya menambahkan file .gitignore dan memasukkan file-file yang tidak akan dimasukkan ke versi kontrol Git.
7. Selanjutnya saya membuat aplikasi main dan mendaftarkannya ke INSTALLED_APPS di dalam projek saya.
8. Di dalam direktori main akan ada models, urls, dan views. Saya juga membuat folder templates yang akan menyimpan templates untuk ditampilkan.
9. Di dalam templates, saya membuat main.html yang berisi konten yang akan ditampilkan di web (npm, name, class, description)
10. Selanjutnya saya mengisi bagian models.py di main app. Saya menambahkan kelas baru bernama joshShop yang memiliki atribut name (CharField), price(IntegerField), description (TextField), dan quantity (IntegerField).
11. Setelah itu, saya mengisi bagian views.py, saya import render, lalu saya membuat fungsi show_main yang berisi context yang akan ditampilkan dan merender datanya dengan template main.html
12. Selanjutnya, lalu saya mengerjakan urls.py di main app agar saya dapat menggunakan fungsi yang saya buat di views.py
13. Setelah itu, saya juga melakukan konfigurasi di urls.py di direktori josh_app (proyek).
14. Setelah itu, saya melakukan add, commit dan push ke repo github
15. Selanjutnya, saya membuat proyek baru di PWS
16. Lalu saya menambahkan URL deployment PWS ke dalam ALLOWED_HOST yang berada di settings.py direktori josh_app.
17. Selanjutnya saya melakukan project command dan push ke PWS.

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![My Image](images/PBP%20bagan.jpg)



### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Dengan menggunakan git, kita dapat mengola dan melacak semua perubahan kode dalam pengembangan perangkat lunak yang memungkinkan kita untuk kembali ke versi sebelumnya jika diperlukan. Git juga memungkinkan kita untuk melakukan branching yang memungkinkan pengembangan fitur baru secara terpisah dari kode utama jadi tidak mengganggu versi stabil dan menggabungkan kode dari berbagai branch setelah fitur selesai dikembangkan. Kita juga dapat menyimpan kode secara remote di GitHub untuk mempermudah sinkronisasi dan backup kode.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena memiliki arsitektur yang terstruktur dan mudah dipahami. Django menggunakan arsitektur Model-Template-View(MTV), ini memberikan kerangka kerja yang jelas dan terorganisir, membantu pemula memahami bagaimana memisahkan logika, tampilan, dan pengolaan data. Selain itu, Django juga memiliki dokumentasi yang baik, serta komunitas yang besar sehingga ada banyak sumber daya belajar seperti tutorial dan dukungan dari komunitas online. 

### 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara objek di kode Python dan tabel relasional di basis data. Django ORM memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan objek Python tanpa menulis langsung query SQL, sehingga data di basis data dapat dikelola seperti objek Python.



# Tugas 3