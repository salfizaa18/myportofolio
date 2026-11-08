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

# TUGAS 4
### AI Disclosure
Pada tugas 4 ini saya menggunakan ChatGpt untuk membantu saya dalam memahami konsep yang belum saya ketahui dan bingungkan.
Hal yang dibantu:
1. Penjelasan mengapa link education tidak muncul di navbar
2. Penempatan use_natural_foreign_keys=True yang tepat di JSON
3. Penjelasan group di django

Dalam proses pengerjaannya, saya tetap berusaha memahami konsep yang diberikan terlebih dahulu sebelum mengimplementasikannya secara mandiri. Dengan demikian, AI saya gunakan sebagai alat bantu untuk memahami konsep dan membantu menjawab kebingungan yang saya temui selama pengerjaan.

# TUGAS 5
### 1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
= Debouncing merupakan suatu teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan input selama waktu tertentu. Pada fitur pencarian yang menggunakan AJAX, debouncicng penting karena tanpa teknik ini setiap perubahan input dapat langsung mengirim request ke server. Misalnya ketika pengguna mengetik "program", dapat terjadi beberapa request untuk “p”, “pr”, “pro”, “prog”, dan seterusnya. Dengan debouncing, request hanya dikirim setelah pengguna berhenti mengetik selama beberapa saat, sehingga jumlah request berkurang, beban server dan database lebih ringan, serta fitur pencarian menjadi lebih efisien.

### 2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
= await digunakan untuk menunggu proses asynchronous dari fetch() selesai sebelum kode dilanjutkan ke baris berikutnya. Misalnya const response = await fetch(url) akan menunggu sampai server memberikan response, sehingga hasilnya dapat langsung digunakan untuk mengambil data dengan response.json(). Jika tidak menggunakan await, hasil dari fetch() masih berupa Promise, bukan response yang sudah selesai diterima. Akibatnya kita tidak bisa langsung menggunakan hasil tersebut seperti response biasa dan perlu menggunakan cara lain seperti .then() untuk menangani hasil request setelah selesai.

### 3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!
= XSS (Cross-Site Scripting) adalah serangan ketika penyerang memasukkan kode JavaScript berbahaya ke dalam halaman web sehingga kode tersebut dapat dijalankan oleh browser pengguna. Data yang ditampilkan melalui AJAX/JavaScript dapat lebih rentan karena developer harus secara manual menentukan bagaimana data tersebut dimasukkan ke halaman. Misalnya, penggunaan innerHTML untuk memasukkan data yang berasal dari user dapat menyebabkan data dianggap sebagai HTML dan berpotensi menjalankan kode berbahaya. Sementara itu, data yang ditampilkan melalui template Django seperti {{ data }} secara default akan melalui proses escaping, sehingga karakter HTML berbahaya tidak langsung dianggap sebagai kode. Namun, AJAX sendiri bukan penyebab XSS; kerentanannya bergantung pada bagaimana data yang diterima diproses dan ditampilkan oleh JavaScript.

### AI Disclosure
Pada tugas 5 ini saya menggunakan Claude untuk membantu saya dalam memahami konsep yang belum saya ketahui dan bingungkan. Hal yang dibantu:
1. Pemberikan massage commit yang detail dan sesuai yang ditambahkan
2. Penjelasan cara menggunakan async dan await dengan fetch()
3. Penjelasan cara menggunakan setTimeout dan clearTimeout untuk membuat debounce di kolom pencarian
4. Penjelasan cara mengirim token CSRF lewat header yang berbeda dengan {% csrf_token %}
5. Penjelasan cara kerja escapeHtml di JavaScript dan strip_tags di forms.py

Dalam pengerjaannya saya tetap berusaha memahami dan mengerjakan secara mandiri. Misalnya dalam implementasi AJAX untuk menampilkan data Education (loading state, search, dan modal tambah data), saya membuatnya sendiri dengan melihat pola dari template pada tutorial 5 di bagian get_projects_json, fetchProjects, dan modal form Project, lalu menyesuaikannya ke bagian Education yang saya kerjakan. Untuk pengiriman token CSRF lewat header saat menggunakan fetch() dan penerapan proteksi XSS (escapeHtml serta strip_tags), saya berusaha untuk memahami terlebih dahulu sebelum mengimplementasikannya secara mandiri. Dengan demikian, AI saya gunakan sebagai alat bantu dalam memahami konsep dan menjawab kebingungan.

# TUGAS 6
### 1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!
= REST adalah gaya arsitektur untuk merancang Web API. REST tidak hanya berkaitan dengan penggunaan JSON, tetapi juga bagaimana resource diatur melalui URL dan bagaimana HTTP method digunakan sesuai fungsinya. Misalnya, GET untuk membaca, POST untuk membuat, PUT/PATCH untuk mengubah, dan DELETE untuk menghapus data. Jadi, mengembalikan JSON saja belum cukup untuk disebut RESTful jika struktur URL dan penggunaan HTTP method belum mengikuti prinsip REST. PUT digunakan untuk memperbarui seluruh data, sedangkan PATCH hanya memperbarui bagian tertentu. Pada proyek ini, modal edit Education menggunakan PUT karena form selalu mengirimkan kelima field. Sementara itu, PATCH lebih cocok jika hanya ingin mengubah satu field, seperti tahun selesai.

### 2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
= Serializer berfungsi mengubah objek model menjadi data yang dapat dikirim dalam format JSON (serialization) dan memvalidasi input dari klien sebelum disimpan ke database (deserialization). Pada proyek ini, EducationSerializer mengatur field yang ditampilkan, membersihkan input menggunakan strip_tags, serta menentukan field tertentu sebagai read-only. Dibandingkan merakit dictionary secara manual menggunakan JsonResponse seperti pada Tutorial 05, serializer membuat pengelolaan data dan validasi lebih terpusat, mengurangi pengulangan kode, serta otomatis memberikan response 400 jika input tidak valid.

### 3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?
= Authentication digunakan untuk mengenali identitas pengguna, sedangkan authorization menentukan hak akses yang dimiliki pengguna tersebut. Pada DRF, SessionAuthentication mengisi request.user, kemudian permission class IsPortfolioOwnerOrEditorOrReadOnly menentukan apakah pengguna boleh melakukan request tertentu. Hak akses harus diperiksa di server karena menyembunyikan tombol di template hanya membatasi tampilan, bukan akses sebenarnya. Pengguna masih bisa mengirim request langsung melalui Postman atau Console browser. Pada proyek ini, hal ini dibuktikan melalui test test_guest_and_regular_user_cannot_write, yang menunjukkan bahwa guest dan pengguna biasa mendapat response 403 ketika mencoba POST, PUT, PATCH, dan DELETE.

### 4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?
= Ketika menggunakan SessionAuthentication, browser otomatis mengirimkan cookie session saat melakukan request ke website. Hal ini dapat dimanfaatkan penyerang untuk membuat browser pengguna yang sedang login mengirimkan request tanpa sepengetahuannya. Karena itu, request yang mengubah data tetap memerlukan token CSRF untuk memastikan request berasal dari sumber yang memiliki token valid. Pada proyek ini, token dikirim melalui header X-CSRFToken yang diambil dari cookie csrftoken. Test menggunakan force_authenticate tidak cukup karena melewati proses autentikasi session sehingga pemeriksaan CSRF tidak dijalankan. Oleh karena itu, saya menggunakan APIClient(enforce_csrf_checks=True) dan .login() untuk menguji perlindungan tersebut. Hasilnya, POST dan PATCH tanpa token ditolak dengan response 403, sedangkan request dengan token berhasil.

### AI Disclosure
Pada Tugas 6, saya menggunakan Claude untuk membantu memahami beberapa hal yang belum saya pahami, seperti:
1. Membuat commit message yang detail dan sesuai dengan perubahan.
2. Memahami alur request DRF, autentikasi, permission, serializer, serta perbedaan PUT dan PATCH.
3. Mengubah AJAX pada education.html agar menggunakan API DRF, termasuk fitur edit melalui PUT.
4. Membuat pengujian berdasarkan peran, validasi, star, dan CSRF menggunakan APIClient.
5. Memahami penerapan serializer, permission class, dan API view untuk Education.

Dalam pengerjaannya, saya tetap berusaha memahami dan mengerjakan secara mandiri. Saya mengikuti pola dari Tutorial 07 pada fitur Project, kemudian menyesuaikannya untuk Education. Saya juga mencoba serializer melalui manage.py shell, menguji endpoint lewat Browsable API dan Console browser, serta memeriksa request melalui tab Network. Ketika menemukan error, saya berusaha mencari penyebab dan memperbaikinya. Jadi, AI saya gunakan sebagai alat bantu untuk memahami konsep dan mengatasi kesulitan selama pengerjaan.