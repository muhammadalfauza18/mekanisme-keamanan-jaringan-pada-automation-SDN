# 🔐 Mekanisme Keamanan Jaringan pada Automation SDN

Implementasi mekanisme keamanan jaringan pada lingkungan **Software Defined Networking (SDN)** menggunakan **Mininet**, **Ryu Controller**, dan **OpenFlow**. Project ini bertujuan untuk mengotomatisasi pengelolaan keamanan jaringan melalui controller SDN sehingga proses monitoring, filtering, dan pengendalian lalu lintas jaringan dapat dilakukan secara terpusat.

---

## 📖 Deskripsi

Software Defined Networking (SDN) merupakan paradigma jaringan modern yang memisahkan **Control Plane** dan **Data Plane**, sehingga administrator dapat mengelola seluruh jaringan melalui sebuah controller.

Pada project ini diterapkan beberapa mekanisme keamanan untuk meningkatkan keamanan komunikasi antar host pada jaringan enterprise, seperti:

- Monitoring lalu lintas jaringan
- Pengelolaan Flow Rule secara otomatis
- Filtering paket
- Kontrol akses jaringan
- Otomasi konfigurasi jaringan

---

## 🎯 Tujuan

- Mempelajari implementasi keamanan pada SDN.
- Mengotomatisasi konfigurasi jaringan menggunakan Python.
- Mengimplementasikan controller berbasis Ryu.
- Menganalisis lalu lintas jaringan menggunakan OpenFlow.
- Meningkatkan keamanan jaringan melalui mekanisme filtering dan flow management.

---

## 🛠️ Teknologi

- Python 3
- Mininet
- Ryu SDN Framework
- Open vSwitch
- OpenFlow 1.3
- Ubuntu Linux

---

## 📂 Struktur Project

```
mekanisme-keamanan-jaringan-pada-automation-SDN/
│
├── controller/
│   ├── security_controller.py
│   ├── simple_switch.py
│   └── flow_manager.py
│
├── topology/
│   └── enterprise_topology.py
│
├── scripts/
│
├── screenshots/
│
├── README.md
└── requirements.txt
```

> Struktur dapat disesuaikan dengan isi repository.

---

## 🔐 Fitur

- SDN Controller berbasis Ryu
- Enterprise Network Topology
- Dynamic Flow Management
- Automatic Flow Installation
- Packet Filtering
- Network Monitoring
- Access Control
- Traffic Management
- OpenFlow Rule Automation

---

## 🌐 Topologi

Topologi menggunakan konsep Enterprise Network yang terdiri dari:

- 1 SDN Controller
- Beberapa OpenFlow Switch
- Client Host
- Server
- OpenFlow 1.3

Ilustrasi sederhana:

```
                 +----------------+
                 | Ryu Controller |
                 +--------+-------+
                          |
                     OpenFlow 1.3
                          |
                    +-----+-----+
                    |  Switch 1 |
             +------+-----+------+
             |                  |
        Switch 2            Switch 3
       /   |   \           /   |   \
     h1   h2  h3        h4  h5  Server
```

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/muhammadalfauza18/mekanisme-keamanan-jaringan-pada-automation-SDN.git
```

Masuk ke folder project

```bash
cd mekanisme-keamanan-jaringan-pada-automation-SDN
```

---

### 2. Install Mininet

```bash
sudo apt update
sudo apt install mininet
```

---

### 3. Install Ryu

```bash
pip install ryu
```

---

### 4. Jalankan Controller

```bash
ryu-manager controller/security_controller.py
```

---

### 5. Jalankan Topologi

```bash
sudo python3 topology/enterprise_topology.py
```

---

### 6. Pengujian

Uji konektivitas jaringan:

```bash
pingall
```

Melihat Flow Table:

```bash
sudo ovs-ofctl dump-flows s1
```

Melihat status switch:

```bash
sudo ovs-vsctl show
```

---

## 📊 Pengujian

Pengujian dilakukan dengan beberapa skenario:

- Ping antar host
- Packet filtering
- Flow installation
- Flow deletion
- Controller response
- Monitoring traffic

Parameter yang diamati:

- Packet Loss
- RTT (Round Trip Time)
- Flow Rule
- Connectivity
- Controller Performance

---


## 📚 Konsep yang Dipelajari

- Software Defined Networking (SDN)
- OpenFlow Protocol
- Open vSwitch (OvS)
- Ryu Controller
- Enterprise Network
- Network Automation
- Flow Rule Management
- Network Security
- Access Control
- Packet Filtering

---


## 📄 Lisensi

Project ini dibuat untuk keperluan pembelajaran, penelitian, dan pengembangan akademik.

Silakan digunakan sebagai referensi dengan tetap mencantumkan sumber.

---

## ⭐ Dukungan

Jika repository ini bermanfaat, silakan berikan ⭐ pada repository GitHub ini sebagai bentuk apresiasi.
