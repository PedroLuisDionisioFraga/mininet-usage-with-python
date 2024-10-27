from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink

class CustomTopo(Topo):
  def build(self):
    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')

    # Connecting hosts to switches with 30 Mbps bandwidth
    self.addLink(h1, s1, bw=30)
    self.addLink(h2, s2, bw=30)
    self.addLink(s1, s2, bw=30)

if __name__ == '__main__':
  topo = CustomTopo()
  net = Mininet(topo=topo, link=TCLink)
  net.start()
  CLI(net)
  net.stop()
