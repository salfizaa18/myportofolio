Nama: Salwa Hafiza Aqila

NPM: 2506624392

Kelas: PBP A

Umur: 19 Tahun

# TUGAS 1
### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
= Iya, saya menggunakan <section> untuk membagi website myportofolio menjadi beberapa bagian yaitu profile, education, experience, dan skills. Elemen <section> membantu saya membuat struktur HTML yang saya buat menjadi lebih terorganisir dan mudah dipahami, sehingga setiap bagian website myportofolio memiliki fungsi dan struktur yang jelas.

### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
= Tantangan yang saya temukan adalah menyesuaikan tampilan layout website agar tetap nyaman dilihat pada layar mobile yang lebih kecil. Pada tampilan desktop, Experience menggunakan dua kolom, tetapi saya mengubahnya menjadi satu kolom pada layar dengan lebar maksimal 600px menggunakan media query. Dengan begitu, setiap informasi Experience tetap mudah dibaca meskipun dilihat lewat mobile.

### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
= Batasan yang saya rasakan adalah informasi masih harus diperbarui secara manual melalui kode HTML. Pada proyek selanjutnya, saya ingin menambahkan suatu informasi baru melalui database dan halaman admin agar dapat dikelola dan diperbarui secara dinamis tanpa mengubah kode HTML nya secara langsung.

### AI Disclosure
Pada tugas 1 ini saya menggunakan Chatgpt untuk membantu saya dalam memahami konsep yang belum saya ketahui dan bingungkan. 
Hal yang dibantu:
1. Penempatan section yang mau ditambahkan
2. Penggunakan CSS untuk mengatur tampilan website, seperti cara mengatur jarak antar elemen, posisi dan layout
3. Penggunaan border, padding, dan border-radius untuk membuat dan mengatur tampilan kotak pada section
Namun, dalam pengerjaannya, saya tetap berusaha memahami dan mengerjakan secara mandiri. Misalnya dalam penambahan section baru, saya membuatnya sendiri dengan melihat pola dari template pada tutorial 1 di bagian index html. Untuk pengeditan tampilan website menggunakan CSS serta pembuatan kotak di bagian section, saya berusaha untuk memahami terlebih dahulu sebelum mengimplementasikannya secara mandiri. Dengan demikian, AI saya gunakan sebagai alat bantu dalam memahami konsep dan menjawab kebingungan.

Referensi lain yang saya gunakan untuk membuat animasi text:
https://youtube.com/shorts/UYZW5Upwrt0?si=TrPduqvLpzsE3Ax5

# TUGAS 2
### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
= Alur yang terjadi dimulai saat pengguna membuka halaman portofolio, request dari browser diterima oleh urls.py proyek dan diarahkan ke urls.py aplikasi. Selanjutnya, URL tersebut memanggil view yang mengambil data melalui model dari database. Data yang diperoleh kemudian dikirim ke template untuk ditampilkan dalam bentuk HTML, lalu hasilnya dikirim kembali ke browser sehingga halaman portofolio dapat dilihat pengguna.

### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
= Hal ini dilakukan agar data terpisah dari template. Dengan begitu, data lebih mudah ditambah, diubah, serta dikelola melalui database tanpa harus mengubah kode HTML. Hal ini membuat apllikasi lebih mudah untuk dipelihara dan dikembangkan, terutama jika jumlah data semakin banyak atau ingin menambahkan fitur baru.

### 3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
= Makemigrations digunakan untuk membuat file migration berdasarkan perubahan pada model, sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database.
Contohnya jika pada model experience ditambahkan field baru seperti foto = models.ImageField(upload_to="experience_photos/", blank=True, null=True). Maka jalankan python manage.py makemigrations dan python manage.py migrate untuk membuat catatan perubahan struktur database serta menerapkan perubahan tersebut ke database.

### AI Disclosure
Pada tugas 2 ini saya menggunakan Chatgpt untuk membantu saya dalam memahami konsep yang belum saya ketahui dan bingungkan. 
Hal yang dibantu:
1. Pembuatan hover effect
2. Pembuatan animasi gradient pada background
Dalam proses pengerjaannya, saya tetap berusaha memahami konsep yang diberikan terlebih dahulu sebelum mengimplementasikannya secara mandiri. Dengan demikian, AI saya gunakan sebagai alat bantu untuk memahami konsep dan membantu menjawab kebingungan yang saya temui selama pengerjaan.

# TUGAS 3
### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!
= ModelForm digunakan karena dapat membuat form berdasarkan model Django secara otomatis. Jadi, kita tidak perlu menulis field html satu per satu secara manual. Modelform juga melakukan validasi otomatis mengikuti aturan pada model. Selain itu, ketika model berubah (nambah/ hapus field), form dapat ikut menyesuaikan tanpa harus merombak ulang html.
{% csrf_token %} wajib ditambahkan karena Django memiliki perlindungan bawaan yang bernama CSRF (Cross-Site Request Forgery). Tanpa adanya perlindungan ini, website lain dapat membuat form tersembunyi yang otomatis submit POST ke website kita. Selain itu {% csrf_token %} menyisipkan token acak dan unik per session sebagai hidden input yang akan dicocokkan dengan yang tersimpan di sisi server. Kalau tidak ada/ tidak cocok, request akan ditolak.

### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
= JSON lebih banyak digunakan karena memiliki format yang lebih sederhana, singkat, dan mudah dibaca, baik oleh manusia maupun program. Struktur JSON juga sesuai dengan tipe data yang umum digunakan pemrograman, seperti object, array, string, dan number.
Selain itu, JSON biasanya menghasilkan ukuran data yang lebih kecil dibandingkan XML sehingga lebih efisien. JSON juga didukung dengan sangat baik oleh JavaScript dan berbagai platform web modern.

### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
= Ketika client mengakses URL, request akan diteruskan ke fungsi view yang sesuai. View kemudian mengambil data portofolio dari model Django. Data tersebut selanjutnya dilakukan proses serialization agar object Django dapat diubah menjadi representasi data yang terstruktur dan dapat dikonversi ke format JSON. Setelah itu, data dikembalikan kepada client dalam bentuk JSON response. Serialization diperlukan karena object Django merupakan objek python yang tidak dapat langsung dikirim sebagai JSON. Dengan serialization, data dari model dapat diubah menjadi format yang dapat direpresentasikan dalam JSON sehingga dapat dikirim dan diproses oleh client.

### AI Disclosure
Pada tugas 3 ini saya menggunakan ChatGpt untuk membantu saya dalam memahami konsep yang belum saya ketahui dan bingungkan. 
Hal yang dibantu:
1. Penjelasan mengenai perbedaan antara method http GET dan POST
2. Penjelasan mengenai perbedaan antara objek dan QuerySet Django
3. Penjelasan mengenai alasan penggunaan {% csrf_token %} pada setiap form
4. Penjelasan proses serialization pada model Django
Dalam proses pengerjaannya, saya tetap berusaha memahami konsep yang diberikan terlebih dahulu sebelum mengimplementasikannya secara mandiri. Dengan demikian, AI saya gunakan sebagai alat bantu untuk memahami konsep dan membantu menjawab kebingungan yang saya temui selama pengerjaan.