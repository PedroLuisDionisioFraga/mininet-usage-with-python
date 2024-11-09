#!/usr/bin/env python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class CustomTopo(Topo):
  def build(self):
    s1 = self.addSwitch('s1')
    s2 = self.addSwitch('s2')
    s3 = self.addSwitch('s3')
    s4 = self.addSwitch('s4')
    s5 = self.addSwitch('s5')
    s6 = self.addSwitch('s6')
    s7 = self.addSwitch('s7')

    h1 = self.addHost('h1')
    h2 = self.addHost('h2')
    h3 = self.addHost('h3')
    h4 = self.addHost('h4')
    h5 = self.addHost('h5')
    h6 = self.addHost('h6')
    h7 = self.addHost('h7')

    self.addLink(s1, s2)
    self.addLink(s2, h1)
    self.addLink(s2, s4)
    self.addLink(s3, h6)
    self.addLink(s3, s7)
    self.addLink(s3, s4)
    self.addLink(s4, h5)
    self.addLink(s4, s5)
    self.addLink(s5, h4)
    self.addLink(s5, s6)
    self.addLink(s6, h2)
    self.addLink(s6, h3)
    self.addLink(s7, h7)

if __name__ == '__main__':
  topo = CustomTopo()
  net = Mininet(topo=topo, cleanup=True, autoSetMacs=True)
  net.start()
  CLI(net)
  net.stop()
