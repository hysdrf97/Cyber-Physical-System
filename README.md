# 🌾 Smart Agriculture MQTT — Tugas Praktikum Cyber Physical System

**Nama:** Firda Aisyah  
**NIM:** 235150307111031  
**Mata Kuliah:** Cyber Physical System  
**Dosen:** Sabriansyah Rizqika Akbar, S.T., M.Eng., Ph.D.  
**Universitas Brawijaya — 2026**

---

## 📋 Deskripsi

Implementasi sistem komunikasi MQTT berbasis **Smart Agriculture** menggunakan Python dan Mosquitto Broker. Sistem mensimulasikan pemantauan lahan pertanian (Kebun A, B, dan C) dengan berbagai sensor (kelembaban tanah, suhu, cahaya, pH, kelembaban udara) yang berjalan sepenuhnya secara lokal di **Linux WSL** tanpa perangkat fisik.

---

## 🗂️ Struktur Folder

```
mqtt_smart_agriculture/
├── broker/
│   └── mosquitto.conf              # Konfigurasi Mosquitto Broker
├── skenario1_dasar/
│   ├── publisher_skenario1.py      # Pub: kelembaban tanah kebun_a (QoS 0)
│   └── subscriber_skenario1.py     # Sub: topik spesifik
├── skenario2_qos/
│   ├── publisher_skenario2.py      # Pub: suhu dengan QoS 0, 1, 2
│   └── subscriber_skenario2.py     # Sub: tampilkan level QoS
├── skenario3_multi_topik/
│   ├── publisher_skenario3.py      # Pub: 5 topik kebun_a & kebun_b
│   └── subscriber_skenario3.py     # Sub: subscribe ke banyak topik
├── skenario4_wildcard_plus/
│   ├── publisher_skenario4.py      # Pub: semua sensor kebun_a + kirim kebun_b
│   └── subscriber_skenario4.py     # Sub: farm/kebun_a/+
├── skenario5_wildcard_hash/
│   ├── publisher_skenario5.py      # Pub: semua kebun semua sensor
│   └── subscriber_skenario5.py     # Sub: farm/#
└── README.md
```

---

## ⚙️ Prasyarat

### 1. Install Mosquitto Broker
```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
```

### 2. Install Python & Paho-MQTT
```bash
python3 --version       # pastikan Python 3 tersedia
pip3 install paho-mqtt
```

### 3. Cek port 1883 (pastikan kosong)
```bash
ss -tlnp | grep 1883
```

---

## 🚀 Cara Menjalankan

> ⚠️ **Urutan wajib: Broker → Subscriber → Publisher**  
> Gunakan 3 terminal WSL secara bersamaan.

### Terminal 1 — Jalankan Broker (wajib pertama)
```bash
cd mqtt_smart_agriculture/broker
mosquitto -c mosquitto.conf -v
```

### Terminal 2 — Jalankan Subscriber
```bash
cd mqtt_smart_agriculture/skenario1_dasar   # ganti nomor skenario
python3 subscriber_skenario1.py
```

### Terminal 3 — Jalankan Publisher
```bash
cd mqtt_smart_agriculture/skenario1_dasar   # ganti nomor skenario
python3 publisher_skenario1.py
```

---

## 📡 Ringkasan Skenario

| Skenario | Topik | QoS | Pesan | Keterangan |
|----------|-------|-----|-------|------------|
| S1: Dasar | `farm/kebun_a/soil_moisture` | 0 | 5 | Komunikasi dasar pub-sub |
| S2: QoS | `farm/kebun_a/temperature` | 0, 1, 2 | 3 | Uji 3 level QoS |
| S3: Multi Topik | 5 topik kebun_a & b | 1 | 15 | Subscribe banyak topik |
| S4: Wildcard `+` | `farm/kebun_a/+` | 1 | 4 | Satu level wildcard |
| S5: Wildcard `#` | `farm/#` | 0 | 7 | Semua topik di bawah farm/ |

---

## 🌿 Struktur Topik MQTT

```
farm/
├── kebun_a/
│   ├── soil_moisture   (kelembaban tanah)
│   ├── temperature     (suhu udara)
│   ├── light           (intensitas cahaya)
│   └── ph              (kadar pH tanah)
├── kebun_b/
│   ├── soil_moisture
│   ├── temperature
│   └── ph
└── kebun_c/
    └── humidity        (kelembaban udara)

Wildcard:
  farm/kebun_a/+  →  semua sensor kebun_a saja
  farm/#          →  semua kebun, semua sensor
```

---

## 📝 Catatan Penting

- **DeprecationWarning** pada `mqtt.Client()` adalah peringatan, bukan error. Program tetap berjalan normal.
- **QoS 2** memerlukan `loop_start()` pada publisher agar handshake 4 langkah selesai sebelum `disconnect()`.
- **Subscriber harus dijalankan sebelum publisher** agar tidak ada pesan yang terlewat (terutama QoS 0).
- Broker boleh tetap berjalan saat berpindah antar skenario, cukup stop subscriber lama dengan `Ctrl+C`.

---

## 🛠️ Lingkungan Pengujian

| Komponen | Versi |
|----------|-------|
| OS | Windows + Linux WSL (Ubuntu) |
| Python | 3.x |
| Paho-MQTT | 1.6+ |
| Mosquitto | 2.0.18 |
| Port | 1883 (localhost) |
