# Inventory Vespa

**Deskripsi**

Inventory Vespa adalah aplikasi berbasis Python yang dirancang untuk membantu dealer Vespa dalam mengelola stok unit mereka secara efisien. Aplikasi ini memungkinkan dealer untuk melacak jumlah unit, harga, dan spesifikasi masing-masing Vespa, serta menghasilkan laporan penjualan. Dengan menggunakan aplikasi ini, dealer dapat membuat keputusan yang lebih baik terkait pembelian dan penjualan Vespa.

**Fitur Utama**

* Login : Sebagai Admin masukkan terlebih dahulu username dan password yang valid agar tidak sembarang orang bisa mengaksesnya
* Read  : Menampilkan seluruh stok Vespa yang ada serta dapat mengurutkannya sesuai harga dan sesuai tahun
* Create: Menambah unit Vespa baru yang dimana menginput nama unit baru (unique field), jumlah stok, harga, tahun, dan jenis mesin
* Update: Mengubah informasi data pada unit Vespa (mengganti harga dan stok)
* Delete: Menghapus suatu unit dengan menginput nama unitnya yang merupakan unique field

** Alur **
* User diarahkan ke start menu dimana diberi opsi untuk login atau keluar dari program
* Bila masuk ke login dan menginput username dan passwordnya, akan diarahkan ke main menu
* Main menu akan berisi opsi Menampilkan daftar vespa, menambah vespa, menghapus vespa, mengganti detail vespa, dan log out
* pada sub menu menampilkan daftar vespa ada opsi menampilkan keseluruhan list unit vespa, menampilkan unit spesifik, mengurutkan sesuai harga, mengurutkan sesuai tahun, dan balik ke main menu
* pada sub menu menambah vespa ada pilihan untuk menginput unit baru ke dalam list vespa dan kembali ke main menu
* pada sub menu menghapus vespa ada pilihan untuk menghilangkan unit vespa dan kembali ke main menu
* pada sub menu mengganti detail vespa ada opsi mengganti harga, mengganti stok vespa, dan kembali ke main menu
* pada sub menu log out akan dikembalikan lagi ke start menu
