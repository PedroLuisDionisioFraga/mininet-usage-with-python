# Practical Work with Mininet
This practical work uses Mininet to create and test virtual networks in two topology configurations: a linear topology and a custom topology implemented in Python.

## Exercise 1: Linear Topology with Eight Hosts
Objective
Create a linear topology with eight hosts, run connectivity and performance tests, and capture the results.

### Steps to Execution
1. **Create the Linear Topology**:\
    **a**. Command to create the topology with 30 Mbps:bandwidth, default Mininet controller and standardized MAC addresses:
    ```bash
    sudo mn --topo=linear,8 --mac --link=tc,bw=30
    ```
2. **Inspect Interface Information, MAC Addresses, IP and Ports**:\
    **a**. Commands to view topology information:
    ```bash
    nodes      # Lista todos os nós da rede
    net        # Exibe as conexões entre os nós
    h1 ifconfig  # Exibe detalhes da interface do hos
    ```
3. **Create Topology Diagram**:
    ```mermaid
    graph TD
      c0[Controlador c0] --> s1
      s1[Switch s1] --> h1[Host h1]
      s1 --> s2[Switch s2]
      s2 --> h2[Host h2]
      s2 --> s3[Switch s3]
      s3 --> h3[Host h3]
      s3 --> s4[Switch s4]
      s4 --> h4[Host h4]
      s4 --> s5[Switch s5]
      s5 --> h5[Host h5]
      s5 --> s6[Switch s6]
      s6 --> h6[Host h6]
      s6 --> s7[Switch s7]
      s7 --> h7[Host h7]
      s7 --> s8[Switch s8]
      s8 --> h8[Host h8]
    ```
4. **Perform Ping Tests**:\
    **a**. Test connectivity between nodes with the command:
      ```bash
      pingall # Pings between all nodes
      ```
    **b**. Use tcpdump to view packets, example for h1:
    ```bash
    xterm h1
    tcpdump -i h1-eth0
    ```
    ![Ping Test](docs/images/tcpdump.png)
5. **TCP Testing with iPerf**:\
    **a**. On h1, configure the TCP server on port 5555:
    ```bash
    xterm h1
    iperf -s -p 5555
    ```
    **b**. On h2, run the client to test bandwidth, reporting per second for 5 seconds:
    ```bash
    xterm h2
    iperf -c 10.0.0.1 -p 5555 -i 1 -t 5
    ```
    ![TCP Test](docs/images/tcp_connection.png)
    **c**. To test bandwidths of 1, 5, 10, 15, 20, and 25 Mbps, recreate the topology with each value using:
    ```bash
    sudo mn -c
    sudo mn --top=linear,8 --mac --link=tc,bw=<value>
    ```

## Exercise 2: Custom Topology in Python
Implement a custom topology in Python, inspect the interfaces, create a diagram, configure MAC rules and verify connectivity.

