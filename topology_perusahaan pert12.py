#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel


def topology():

    print("=== Membuat Network ===")

    net = Mininet(
        controller=RemoteController,
        switch=OVSSwitch,
        autoSetMacs=True
    )

    # ==========================
    # Controller
    # ==========================
    print("Menambahkan Controller...")

    c0 = net.addController(
        'c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6653
    )

    # ==========================
    # Switch
    # ==========================
    print("Membuat Switch...")

    s1 = net.addSwitch('s1', protocols='OpenFlow13')
    s2 = net.addSwitch('s2', protocols='OpenFlow13')
    s3 = net.addSwitch('s3', protocols='OpenFlow13')
    s4 = net.addSwitch('s4', protocols='OpenFlow13')

    # ==========================
    # Host Otomatis
    # ==========================
    print("Membuat Host Secara Otomatis...")

    hosts = []

    for i in range(1, 10):

        host = net.addHost(
            f'h{i}',
            ip=f'10.0.0.{i}/24'
        )

        hosts.append(host)

    # ==========================
    # Server
    # ==========================
    print("Menambahkan Server...")

    server = net.addHost(
        'server',
        ip='10.0.0.100/24'
    )

    # ==========================
    # Link Antar Switch
    # ==========================
    print("Membuat Link Antar Switch...")

    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s1, s4)

    # ==========================
    # Divisi Keuangan
    # ==========================
    print("Menghubungkan Divisi Keuangan...")

    for host in hosts[0:3]:
        net.addLink(host, s2)

    # ==========================
    # Divisi SDM
    # ==========================
    print("Menghubungkan Divisi SDM...")

    for host in hosts[3:6]:
        net.addLink(host, s3)

    # ==========================
    # Divisi Operasional
    # ==========================
    print("Menghubungkan Divisi Operasional...")

    for host in hosts[6:9]:
        net.addLink(host, s4)

    # ==========================
    # Server ke Core
    # ==========================
    print("Menghubungkan Server...")

    net.addLink(server, s1)

    # ==========================
    # Build Network
    # ==========================
    print("Menjalankan Network...")

    net.build()

    c0.start()

    s1.start([c0])
    s2.start([c0])
    s3.start([c0])
    s4.start([c0])

    print("\n====================================")
    print(" Topologi Tree Berhasil Dibuat ")
    print("====================================\n")

    print("\n==============================")
    print("AUTOMATIC CONNECTIVITY TEST")
    print("==============================")

    loss = net.pingAll()

    print("\n===================================")
    print(" AUTOMATIC SECURITY ")
    print("===================================")

    print("Memblokir akses Divisi Operasional ke Server...")

    for host in ['h7', 'h8', 'h9']:
        net.get(host).cmd("iptables -A OUTPUT -d 10.0.0.100 -j DROP") 

        if loss == 0:
            print("\nSemua Host Berhasil Terhubung\n")
        else:
            print("\nMasih Ada Packet Loss\n") 
    print("\n===================================")
    print(" SECURITY TEST ")
    print("===================================")

    print("\nKeuangan -> Server")
    print(net.get('h1').cmd("ping -c 2 10.0.0.100"))

    print("\nSDM -> Server")
    print(net.get('h4').cmd("ping -c 2 10.0.0.100"))

    print("\nOperasional -> Server")
    print(net.get('h7').cmd("ping -c 2 10.0.0.100"))
    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
