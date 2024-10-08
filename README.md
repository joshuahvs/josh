# JOSH

Link tautan menuju web: http://joshua-hans-joshapp.pbp.cs.ui.ac.id/


<details>
<summary><b>Tugas 2</b></summary>

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

</details>

<details>
<summary><b>Tugas 3</b></summary>

# Tugas 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena data dalam sebuah platform harus ditransfer dengan aman dan cepat antara pengguna dan sistem. Hal ini penting untuk menjaga keakuratan aliran informasi dalam sebuah platform. 

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik daripada XML. JSON juga lebih populer dibandingkan dengan XML karena struktur JSON lebih mudah dibaca dan dipahami oleh manusia seperti kita, sehingga lebih mudah dalam pengembangan dan proses debuggingnya. JSON juga lebih ringkas dan efisien karena formatnya lebih sederhana (tidak ada tag pembuka dan penutup seperti XML), sehingga pemrosesan JSON biasanya lebih cepat dibandingkan dengan XML.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirim melalui form memenuhi aturan validasi yang sudah diterapkan. Method akan mengembalikan True jika data valid, dan False jika salah. Kita butuh method ini agar hanya data yang valid yang diproses atau disimpan ke dalam databse, dan menolak data atau input yang tidak sesuai.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
crsf_token adalah token unik yang dihasilkan untuk setiap sesi dan juga disertakan dalam form sebagai cara untuk menverifikasi bahwa permintaan yang diterima oleh sebuah server berasal dari sumber yang sah dan diinisiasi oleh pengguna yang terautentikasi. Kita membutuhkan csrf_token saat membuat form di Django untuk mencegah dari serangan Cross Site Request Forgery (CRSF). Django secara default memeriksa keberadaan crsf_token untuk setiap permintaan POST, kalau tidak ada token ini, maka permintaan akan ditolak, dan pengguna akan menerima pesan kesalahan. Tidak adanya crsf_token juga membuka celah bagi penyerang untuk melakukan serangan CRSF. Penyerang dapat mengirimkan permintaan berbahaya yang tampak sah ke aplikasi web atas nama pengguna yang telah terautentikasi. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Yang pertama saya lakukan adalah folder templates, mengisinya dengan base templates yang dapat digunakan sebagai kerangaka umum, dan juga mengonfigurasi templates di settings.py. 
2. Lalu saya menambahkan id dengan mengimport uuid di models.py yang terletak di main untuk mencegah kerentanan keamanan. Tidak lupa saya melakukan migrations. 
3. Untuk membuat form, saya membuat file baru bernama forms.py dan membuat class bernama joshShopEntryForm, untuk model dan fields nya saya sesuaikan dengan yang ada di models.py
4. Setelah itu di views.py, saya mengimport dan membuat fungsi baru bernama create_item_entry yang akan menambahkan data item secara otomatis ketika form di submit. Saya juga mengubah show_main untuk mengambil seluruh objek yang tersimpan di database untuk ditampilkan di main page. 
5. Selanjutnya saya membuat create_item_entry.html pada templates di main yang mengextend base.html yang akan ditampilkan ketika user mengklik tombol untuk menambah item. Saya juga mengubah main.html untuk menampilkan data baru yang diinput oleh user di form. 
6. Setelah itu, saya juga mengimport fungsi dan menambahkan path url di urls.py di main agar dapat mengakses fungsi create_item_entry yang sudah dibuat. 
7. Selanjutnya, saya juga menambahkan fungsi di views.py yaitu show_xml, show_json yaitu fungsi yang akan mengembalikan data dalam bentuk XML ataupun JSON.
8. Saya juga menambahkan show_xml_by_id, show_json_by_id untuk melakukan filter XML ataupun JSON berdasarkan ID.
9. Setelah membuat semua fungsi tersebut, saya mengimport lagi di urls.py dan menambahkan pathnya agar fungsi dapat digunakan.
10. Setelah itu saya melakukan commit dan push ke github

### Hasil Screenshot 
#### XML
![My Image](images/xml.png)
#### XML by ID
![My Image](images/xml%20by%20id.png)
#### JSON
![My Image](images/json.png)
#### JSON by ID
![My Image](images/json%20by%20id.png)

</details>

<details>
<summary><b>Tugas 4</b></summary>

# Tugas 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
`HttpResponseRedirect()` dan `redirect()` adalah dua cara untuk mengarahkan ulang pengguna dari satu URL ke URL lain, namun mereka memiliki perbedaan dalam penggunaan dan fleksibilitas. `HttpResponseRedirect()` merupakan kelas bawaan yang secara langsung mengembalikan respons HTTP 302 dengan URL tujuan yang spesifik, jadi kita memerlukan URL yg lengkap sebagai argumen. Sedangkan, `redirect()` adalah fungsi shortcut yang lebih fleksibel karena dapat menerima berbagai jenis argumen seperti nama view, model, atau URL langsung, dan secara otomatis menentukan jenis redirect yang tepat tanpa memerlukan URL String.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model `Product` dengan `User` di Django dapat kita lakukan menggunakan `ForeignKey`. Agar setiap produk hanya ditampilkan untuk pengguna yang terasosiasi, maka di dalam models.py di class untuk productnya, kita tambahkan field `user = models.ForeignKey(User, on_delete=models.CASCADE)`, yang menunjukkan bahwa setiap produk terkait dengan satu instance `User`. Dengan demikian, setiap kali sebuah produk dibuat, pengguna yang membuatnya dapat diidentifikasi dan dikelola melalui relasi ini. Penggunaan relasi ini memudahkan dalam mengakses data terkait, seperti menampilkan produk yang dimiliki oleh seorang pengguna atau menentukan pengguna yang memiliki akses ke suatu produk tertentu.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses verifikasi identitas pengguna, memastikan bahwa pengguna tersebut memang siapa yang mereka klaim, ini dilakukan biasanya dengan mencocokan username dan password. Authorization adalah proses menentukan hak akses pengguna setelah mereka terautentikasi, yaitu apa yang boleh dan tidak boleh dilakukan oleh pengguna tersebut dalam aplikasi. Ketika pengguna login, ada proses authentication dimana sistem memeriksa kredensial pengguna. Django mengimplementasikan kedua konsep ini melalui sistem autentikasi bawaan yang menyediakan mekanisme login, logout, dan manajemen sesi untuk authentication. Untuk authorization, Django menggunakan sistem izin (permissions), grup pengguna, serta decorator seperti `@login_required` untuk mengontrol akses ke berbagai bagian aplikasi berdasarkan hak yang diberikan kepada pengguna. 

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login melalui sistem sesi (session) yang menggunakan cookies. Nantinya, ketika pengguna berhasil login, Django akan membuat sebuah sesi unik dan menyimpan ID sesi tersebut dalam cookie di browser pengguna. Lalu, setiap kali pengguna melakukan permintaan ke server, cookie ini dikirim kembali sehingga Django dapat mengidentifikasi dan mempertahankan status login pengguna tersebut. Selain untuk autentikasi, cookies juga digunakan untuk berbagai kegunaan lain seperti menyimpan preferensi pengguna, melacak aktivitas untuk analitik, dan mengelola konten yang dipersonalisasi. Namun, tidak semua cookies aman digunakan karena beberapa dapat menyimpan informasi sensitif yang rentan terhadap serangan seperti pencurian data melalui cross-site scripting (XSS) atau manipulasi oleh pihak ketiga. Jadi, penting untuk menggunakan cookies dengan aman dengan menerapkan atribut seperti HttpOnly dan Secure, serta memastikan bahwa data yang disimpan dalam cookies dienkripsi atau tidak mengandung informasi pribadi yang sensitif.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Yang pertama saya lakukan adalah membuat halaman `register.html`, `login.html` di direktori templates pada main app saya, inilah yang nanti akan ditampilkan ketika user ingin register, ataupun login.
2. Setelah itu, saya membuat form agar user bisa melakukan registrasi. Ini saya lakukan dengan cara mengimport `UserCreationForm` sebagai formulir bawaan dan `messages` di views.py untuk menampilkan jika user berhasil dibuat. Setelah itu, saya membuat fungsi register yang nantinya akan merender `register.html`.
3. Setelah membuat fungsi register, saya juga membuat fungsi login dengan mengimport tambahan yaitu `autheticate` dan juga `login`. Saya juga membuat fungsi baru lagi yaitu `login_user` yang nantinya akan merender `login.html`.
4. Agar user yang sudah login bisa logout, saya juga mengimport `logout` dan membuat fungsi `logout_user` yang nantinya akan mengarahkan user kembali ke halaman login page. Di `main.html` saya juga menambahkan button yang akan memanggil fungsi `logout_user` ini.
5. Saya juga menambahkan decorator `@login_required` pada `show_main` agar user harus login dulu baru bisa mengakses main page.
6. Saya mengonfigurasi semua fungsi di urls.py dan menambahkan semua fungsi yang saya sudah buat di `urlpatterns` agar dapat digunakan.
7. Lalu saya menjalankan program dan mencoba membuat user dengan melakukan register.
8. Agar kita dapat tahu kapan user terakhir login, kita butuh cookies. Jadi pada views.py pada saat `login_user` jika valid, maka saya menyetel cookie dan saat user logout, saya akan menghapus cookie tersebut. Untuk menampilkannya saya menambahkan informasi login di `show_main` dan merendernya di `main.html`.
9. Untuk menghubungkan user dengan productnya, saya mengimport User pada models.py, dan menggunakan ForeignKey untuk menghubungkan sebuah product dengan user. 
10. Di views.py saya juga memodifikasi `create_item_entry` untuk mengasosiasikan item dengan user yang sedang login sebelum disimpan ke database. Di `show_main` saya juga filter product yang akan ditampilkan berdasarkan user.
11. Terakhir, saya melakukan migrations dan mengimport `os` dan mengganti variabel `DEBUG` pada `settings.py` agar siap untuk environment production.
12. Tidak lupa saya juga membuat dua akun pengguna dan tiga dummy data di lokal.
</details>


<details>
<summary><b>Tugas 5</b></summary>

# Tugas 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, maka akan diambil berdasarkan spesifisitasnya, yaitu:
1. **Inline Styles**  
   Gaya yang ditulis langsung pada elemen menggunakan atribut `style`.  
   Contoh: `<div style="color: black;"></div>`
2. **ID Selector**  
   Selector yang menggunakan ID unik.  
   Contoh: `#header { ... }`
3. **Class, Attribute, dan Pseudo-class Selector**  
   Selector yang menggunakan class, atribut, atau pseudo-class.  
   Contoh: `.menu`, `[type="text"]`, `:hover`
4. **Element dan Pseudo-element Selector**  
   Selector yang menggunakan nama tag elemen atau pseudo-element.  
   Contoh: `div`, `p::after`
5. **Universal Selector dan Kombinator**  
   Selector universal (`*`) dan kombinator seperti descendant, child, dll.  
   Contoh: `*`, `div p`

Jika spesifisitas sama, aturan CSS yang ditulis terakhir akan diterapkan.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena memastikan tampilan dan fungsionalitas yang optimal di berbagai perangkat dan ukuran layar, mulai dari smartphone hingga desktop. Dengan meningkatnya penggunaan perangkat mobile, responsive design meningkatkan pengalaman pengguna, memperbaiki SEO, dan memungkinkan akses yang lebih luas. Contoh aplikasi yang sudah menerapkan responsive design adalah **YouTube**, yang menyesuaikan antarmuka mereka secara dinamis sesuai perangkat yang digunakan. Sebaliknya, beberapa aplikasi lama seperti **SIAKNG** atau beberapa portal berita tradisional belum sepenuhnya mengadopsi responsive design, sehingga tampilan mereka kurang optimal pada perangkat mobile dan mengakibatkan pengalaman pengguna yang kurang baik.


### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding merupakan tiga komponen utama dalam model box CSS yang mengatur ruang dan batas suatu elemen. **Margin** adalah ruang di luar border yang memisahkan elemen dengan elemen lain, memberikan jarak antar elemen. **Border** adalah garis yang mengelilingi padding dan konten elemen, dapat disesuaikan ketebalan, jenis, dan warnanya. **Padding** adalah ruang di dalam border yang memisahkan konten elemen dari batasnya, memastikan konten tidak menempel langsung pada border. Ketiganya dapat diimplementasikan menggunakan properti CSS seperti `margin`, `border`, dan `padding`. Contoh cara mengimplementasikannya adalah seperti berikut:

```css
.element {
    margin: 20px;        /* Mengatur jarak luar elemen */
    border: 2px solid #333; /* Mengatur garis border elemen */
    padding: 15px;       /* Mengatur jarak dalam elemen */
}
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid Layout adalah dua sistem tata letak CSS yang memudahkan pengaturan elemen dalam halaman web. **Flexbox** (Flexible Box) dirancang untuk mengelola tata letak satu dimensi, baik dalam baris maupun kolom, memudahkan penyusunan, penyelarasan, dan distribusi ruang antar item secara fleksibel. Flexbox sangat berguna untuk navigasi, menu, atau elemen yang membutuhkan penyesuaian responsif dalam satu arah. **Grid Layout**, di sisi lain, memungkinkan pembuatan tata letak dua dimensi dengan mengatur baris dan kolom secara simultan, cocok untuk desain kompleks seperti layout halaman utama, galeri foto, atau dashboard aplikasi. Dengan memanfaatkan kedua konsep ini, kita dapat menciptakan desain yang responsif, terstruktur, dan mudah disesuaikan sesuai kebutuhan berbagai perangkat.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Yang pertama saya lakukan adalah menambahkan fungsi baru di `views.py` yaitu fungsi `edit_item` dan juga `delete_item` yang masing-masing berfungsi untuk mengedit data produk yang sudah ada dan juga menghapus produk yang ada. 
2. Setelah mengimplementasikan fungsi tersebut, saya mengintegrasikan pathnya di `urls.py` pada main app. 
3. Kemudian saya juga membuat folder static untuk tempat css dan juga gambar-gambar yang akan saya gunakan
4. Setelah itu, saya mengubah `settings.py` untuk agar dapat menggunakan static files yang ada. 
5. Saya mengubah `base.html` untuk dapat menggunakan tailwind css
6. Selanjutnya saya membuat `navbar.html` yang akan saya gunakan pada `main.html`, dan `navbar2.html` yang saya gunakan di `edit_item.html` dan juga `create_item_entry.html`. Saya juga mengubah htmlnya agar sesuai dengan kemauan saya.
7. Setelah itu saya mengedit bagian `main.html` dengan melakukan benchmarking ke website Dolce&Gabanna
8. Saya juga membuat `product_list.html`yang akan menampilkan product yang sudah ditambahkan oleh sang user dan disini saya juga menambahkan button untuk edit dan delete pada setiap produk.
9. Setelah itu, saya mengedit bagian `login.html` dan juga `register.html` agar sesuai dengan kemauan saya.
10. Saya mendesain keseluruhan aplikasi saya dengan menggunakan tailwind css, saya juga mengedit global.css nya untuk mendefinisikan desain keseluruhan aplikasi. 
11. Setelah itu, saya melakukan commit, dan push ke github dan pws. 
</details>



# Tugas 6

### 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Manfaat JavaScript dalam pengembangan aplikasi web adalah membantu membuat aplikasi menjadi lebih interaktif dan dinamis. Dengan JavaScript, kita bisa membuat halaman yang lebih hidup, misalnya dengan menambahkan animasi, validasi form otomatis, dan tombol yang merespon langsung tanpa harus memuat ulang halaman. Selain itu, JavaScript memungkinkan pengolahan data di sisi pengguna (di browser), sehingga pengguna bisa melihat hasil interaksi mereka tanpa perlu menunggu server merespon. JavaScript juga sangat dapat menangani komunikasi asinkron menggunakan AJAX atau `fetch()`, yang memungkinkan kita mengambil data dari server tanpa harus me-refresh seluruh halaman, sehingga pengalaman pengguna menjadi lebih cepat dan lancar.

### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Penggunaan await saat memakai fetch() adalah untuk menunggu hasil dari permintaan data sebelum melanjutkan eksekusi kode. `fetch()` sendiri adalah fungsi asinkron yang digunakan untuk mengambil data dari server, tapi hasilnya tidak langsung didapatkan, melainkan berupa promise (janji bahwa datanya akan datang nanti). Dengan menambahkan await, kita memastikan bahwa kode lain tidak berjalan dulu sebelum data dari server sudah diterima sepenuhnya. Jika kita tidak menggunakan await, kode akan terus berjalan seperti biasa, dan ini bisa menyebabkan error jika kita mencoba memproses data yang sebenarnya belum ada.

### 3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Django menggunakan token CSRF sebagai lapisan keamanan untuk memastikan bahwa setiap permintaan POST berasal dari sumber yang sah. Tapi dalam beberapa kasus, seperti saat menggunakan AJAX untuk mengirimkan data, token CSRF mungkin tidak dikirimkan dengan benar. Dengan menggunakan decorator `csrf_exempt`, kita mengizinkan request AJAX POST masuk tanpa memerlukan pengecekan token CSRF, sehingga tidak diblokir oleh server. Namun, ini harus dilakukan hati-hati karena bisa membuka celah keamanan jika tidak diatur dengan benar.

### 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data tetap dilakukan di backend meskipun sudah ada validasi di frontend adalah untuk keamanan. Validasi di frontend itu penting juga untuk pengalaman pengguna yang lebih baik, tapi data bisa saja dimanipulasi oleh orang yang punya niat buruk menggunakan alat-alat pengembang di browser mereka. Kalau kita hanya mengandalkan validasi di frontend, aplikasi kita akan rentan terhadap serangan seperti injeksi SQL atau XSS (cross-site scripting). Backend perlu memastikan bahwa data yang diterima aman dan sesuai dengan yang diharapkan, karena di sinilah kita bisa benar-benar mengontrol proses sebelum data disimpan atau diproses lebih lanjut.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Yang pertama saya lakukan adalah menambahkan fungsi baru yaitu `add_item_entry_ajax` pada `views.py`. Ini adalah method utama yang digunakan untuk menambahkan item baru menggunakan ajax dan menambahkan item barunya ke dalam basis data.
2. Lalu, saya mengonfigurasi pathnya di `urls.py`
3. Selanjutnya pada `main.html` saya mengganti kode yang menampilkan product list sebelumnya dengan `<div id="item_entry_cards"></div>`. Lalu saya juga menambahkan modal, yaitu form yang akan muncul sebagai pop up ketika nanti saya ingin menambahkan sebuah item.
4. Saya juga menambahkan button baru untuk add new item menggunakan ajax.
5. Lalu saya membuat fungsi javascript pada `main.html`. Fungsi yang saya tambahkan pertama adalah `showModal()` dan juga `hideModal()`. Ini adalah fungsi javascript yang akan membantu menampilkan form modal, dan juga menghide modal.
6. Selanjutnya ada fungsi `getItemEntries()` yang akan me-fetch data dan mengubahnya menjadi object javascrip dan `refreshItemEntries()` yang nantinya akan merefresh data item yang akan ditampilkan di web secara ansikronus.
7. Selanjutnya, saya menambahkan `addItemEntry()` yang mengambil data dari form modal, dan menambahkannya ke database untuk ditampilkan, dan merefresh content (bukan page) dengan memanggil ``refreshItemEntries()`.
8. Saya juga menambahkan beberapa eventListener yang akan memanggil fungsi-fungsi yang sudah saya buat. Misalnya, ketika form di submit, maka akan memanggil fungsi `addItemEntry()`. 
9. Untuk memastikan keamanan program, saya juga melakukan strip_tags untuk membersihkan data baru dan DOMPurify untuk membersihkan data di front end. 