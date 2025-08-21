import psutil
import netifaces
from scapy.all import sniff, IP

class SystemMonitor:
    def get_system_stats(self):
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent,
            "network": self.get_network_stats()
        }
    
    def get_network_stats(self):
        interfaces = netifaces.interfaces()
        stats = {}
        for interface in interfaces:
            addrs = netifaces.ifaddresses(interface)
            stats[interface] = addrs.get(netifaces.AF_INET, [])
        return stats
    
    def packet_callback(self, packet):
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            print(f"Packet: {ip_src} -> {ip_dst}")
    
    def start_sniffing(self):
        sniff(prn=self.packet_callback, store=0, count=100)
