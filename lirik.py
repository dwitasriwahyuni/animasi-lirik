import sys
import time
import winsound

def jalan_lirik():
    try:
        # Memutar lagu di latar belakang
        winsound.PlaySound("lirik.wav", winsound.SND_ASYNC)
    except Exception as e:
        print("⚠️ Gagal memutar musik:", e)

    # 1. ATUR WAKTU TUNGGU DI SINI (dalam detik)
    # Ubah angka 3.0 sesuai durasi intro lagu sebelum lirik pertamanya mulai dinyanyikan
    waktu_intro = 4.0 
    time.sleep(waktu_intro)

    lirik = [
        ("temanku semua pada jahat tante", 0.1),
        ("aku lagi susah mereka gak ada", 0.1),
        ("coba kalau lagi jayaaa", 0.1),
        ("aku dipuja puja tante", 0.1),
        ("sudah terbiasa terjadi tante", 0.1),
        ("teman datang ketika lagi butuh saja", 0.1),
        ("coba kalau lagi susaahhhh", 0.1),
        ("mereka semua menghilaaaaaanggg", 0.1)
    ]
    
    delay = [1.1, 1.4, 1.4, 1.3, 1.6, 1.25, 1.1, 1.0]
    print("~ TAANTEEEMEEEEE ~")
    print("Memutar musik dan animasi lirik...\n")
    
    for i in range(len(lirik)):
        text, speed = lirik[i]
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
        time.sleep(delay[i])

if __name__ == "__main__":
    jalan_lirik()