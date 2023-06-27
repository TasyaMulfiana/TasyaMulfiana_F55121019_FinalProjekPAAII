# TasyaMulfiana_F55121019_FinalProjekPAAII
Tugas Final Projek PAA II

Analisis algoritma Bubble Sort dan Insertion Sort:
Bubble Sort:
Worst Case: Array terurut secara terbalik. Dalam kasus ini, setiap elemen harus dipindahkan ke posisi yang benar, sehingga memiliki kompleksitas waktu O(n^2).
Best Case: Array sudah terurut dengan benar. Dalam kasus ini, algoritma akan melewati iterasi pertama tanpa ada pertukaran elemen, sehingga memiliki kompleksitas waktu O(n).
Average Case: Array memiliki urutan acak. Dalam kasus ini, Bubble Sort akan memerlukan pertukaran elemen dan iterasi berulang hingga array terurut dengan benar. Kompleksitas waktu rata-rata pada kasus ini juga O(n^2), meskipun dengan faktor konstan yang lebih rendah daripada worst case.

Insertion Sort:
Worst Case: Array terurut secara terbalik. Dalam kasus ini, setiap elemen harus dipindahkan ke posisi yang benar dengan membandingkannya dengan semua elemen di sebelahnya, sehingga memiliki kompleksitas waktu O(n^2).
Best Case: Array sudah terurut dengan benar. Dalam kasus ini, algoritma akan melewati iterasi pertama tanpa ada pergeseran elemen, sehingga memiliki kompleksitas waktu O(n).
Average Case: Array memiliki urutan acak. Dalam kasus ini, Insertion Sort akan memindahkan setiap elemen ke posisi yang benar dengan membandingkannya dengan elemen-elemen di sebelahnya. Kompleksitas waktu rata-rata pada kasus ini juga O(n^2), meskipun dengan faktor konstan yang lebih rendah daripada worst case.

Analisis algoritma TSP dan Djikstra:
TSP:
Worst Case: Kasus terburuk terjadi ketika jumlah node yang harus dikunjungi sangat besar, Kompleksitas waktu algoritma TSP yang digunakan pada kode program ini adalah O(n^2 * 2^n), Ketika jumlah node n meningkat, kompleksitas waktu akan meningkat secara eksponensial. Jadi, dalam worst case, algoritma TSP akan memerlukan waktu yang sangat lama untuk menemukan jalur terpendek.
Best Case: Kasus terbaik terjadi ketika hanya ada sedikit node yang harus dikunjungi dan Ketika jumlah node n sedikit kompleksitas waktu akan cenderung lebih baik.
Average Case: Rata-rata kasus tergantung pada jumlah node dan sisi yang terlibat dan Algoritma TSP cenderung memerlukan waktu yang cukup lama dalam kasus rata-rata karena kompleksitas eksponensialnya.

Dijkstra:
Worst Case: Kasus terburuk terjadi ketika graf memiliki banyak node dan sisi, Kompleksitas waktu algoritma Dijkstra yang digunakan pada kode program ini adalah O((V + E) log V), di mana V adalah jumlah node dan E adalah jumlah sisi, Ketika jumlah node dan sisi meningkat, kompleksitas waktu akan meningkat secara linier. Jadi, dalam worst case, algoritma Dijkstra akan memerlukan waktu yang lebih lama jika graf memiliki banyak node dan sisi.
Best Case: Kasus terbaik terjadi ketika graf memiliki sedikit node dan sisi, atau jalur terpendek langsung dari titik awal ke titik akhir, Ketika jumlah node dan sisi sedikit, kompleksitas waktu akan cenderung lebih baik dan Algoritma Dijkstra cenderung memberikan hasil yang lebih cepat dalam kasus terbaik dibandingkan dengan algoritma TSP.
Average Case: Rata-rata kasus tergantung pada kompleksitas graf dan jarak antara titik awal dan titik akhir dan Algoritma Dijkstra cenderung memberikan hasil yang lebih cepat dalam kasus rata-rata dibandingkan dengan algoritma TSP, terutama jika jarak antara titik awal dan titik akhir tidak terlalu jauh.
