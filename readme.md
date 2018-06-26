[ccc.txt]
Dataset yang sudah dipreprocess.
Format :
P blabla.com
L bla1.com
L bla2.com
Artinya , website blabla.com memiliki link ke bla1.com dan bla2.com.

[urlextract.py]
Input 	: ccc.txt
Output 	: lala.txt

Algoritma :

1. Buka file dataset yang telah terpreprocess
2. Baca satu line
3. Jika huruf pertama di line tersebut P (maka ini website parent)
	currentDomain := domain URL saat ini
	Inisialisasi set nodeDict[currentDomain]
	Inisialisasi set setOfLink
4. Jika huruf pertama di line tersebut L (maka ini website child)
	Cek, apakah domain URL ini domain terlarang, jika terlarang, skip link ini
	Cek, apakah domain URL ini sama dengan currentDomain, jika iya, website ini punya link ke dirinya sendiri, skip.
	Tambahkan domain ini ke setOfLink
	nodeDict[currentDomain] := nodeDict[currentDomain] union setOfLink
	Jika domain ini belum tercantum di inDegree
		inisialisasi set indegree[domain] 
	Jika sudah tercantum
		tambahkan currentDomain ini ke indegree[domain]
5. Ulangi langkah ke-2 sampai seluruh line selesai diproses
6. Inisialisasi dictionary indegreeQty
   Dictionary indegreeQty adalah key-value. Dimana key adalah nama website x, 
   value adalah jumlah website yang memiliki link mengarah ke website x.	
7. Iterasi seluruh elemen set indegree
	indegreeQty[x] = jumlah elemen dari indegree[x]
8. Urutkan indegreeQty berdasarkan value dari indegreeQty
9. Tampilkan pasangan key-value dari indegreeQty , terurut berdasarkan value.
	
[setOfLink]
Himpunan, berisi link yang ditunjuk oleh website x.
Website x adalah website P terakhir yang ditemui.
Contoh

P google.com
L wikipedia.org
L twitter.com
L twitter.com

setOfLink = [wikipedia.org , twitter.com]
Catatan : Sifat himpunan, tidak mengenal item duplikat.

nodeDict[x]
Himpunan, berisi link yang ditunjuk oleh website x
Contoh
P google.com
L wikipedia.org
L twitter.com
L twitter.com
P google.com
L detik.com
L kaskus.com
nodeDict[google.com] = [wikipedia.org, twitter.com, detik.com, kaskus.com]

indegree[x]
Himpunan, berisi website-website yang memiliki link yang menunjuk ke website x
Contoh 
P google.com
L wikipedia.org
P youtube.com
L wikipedia.org
P twitter.com
L wikipedia.org
indegree[wikipedia.org] = [google.com, youtube.com, twitter.com[
	

[lala.txt]
Daftar node, diurutkan berdasarkan jumlah indegree terbesar
Node 		: Website x
Indegree	: Jumlah website lain yang memiliki link mengarah ke website x. Website dijamin unik


[Result]
aquatek.gr : Pembatas, antara 1 dan 0.
