# Networking

## OSI Model

- *Open Systems Interconnection Model*

### Layers

Sr No | Layer           | Data unit          | Examples
------|-----------------|--------------------|-------------------------------------
1    | Physical         | bit                | Ethernet, USB, Wi-Fi, Bluetooth, DSL
2    | Data link        | Frame              | L2TP, PPP, CSMA/CD
3    | Network          | Packet             | **IPv4**, **IPv6**
4    | Transport        | Segment (Datagram) | **TCP**, **UDP**
5    | Session          | Data               | HTTP, FTP, SMTP, DNS, IMAP, SSH, TLS
6    | Presentation     | Data               | ASCII, JPEG
7    | Application      | Data               | Chrome, Mail.app

### Data Units

- Frame
    - Structure: Frame header (e.g. Ethernet) + (Network header + Transport header + data) + Frame footer
    - Source and destination MAC addresses, length, checksum
    - Max Lenght of a frame: 1518 Byte, 12 Byte for mac addresses, 2 Byte for Ethertype and 4 Byte for FCS (Frame Check Sequence).
- Packet
    - Structure: Network header (e.g. IP) + (Transport header + data)
    - Version (IPv4/IPv6), source and destination IP addresses, length flags, TTL, protocol, checksum
- Segment
    - Structure: Transport header (e.g. TCP) + data
    - Source and destination ports, sequence number, ack number, data offsets, flags, checksum

## IP

- *Internet Protocol*
- No concept of connection.
- Packets are passed from one computer to the next, until reaching the destination.
- No delivery guarantee, no receiving ack.
- Sometimes multiple copies of the same packet are passes, taking different paths, and thus arriving at different times.
- Designed to be able to route around connectivity problems.
- Exists two version of this: IPv4 and IPv6, we are migrating to v4 to v6 because there are a lot of Internet Devices.
    - The main difference is that IPv4 is only 32 bit and the IPv6 is 128 bit

## TCP

- *Transmission Control Protocol*
- Built on-top of IP.
- Connection-based.
- Once a connection has been made between two parties, sending data between the two is much like writing to a file on one side and reading from a file on the other.
- Reliable and ordered, i.e., arrival and ordering are guaranteed.
- Takes care of splitting your data info packets and sending those across the network, so you can write bytes as a stream of data.
- Makes sure it doesn't send data too fast for the Internet connection to handle (flow control).
- Hides all complexities of packets and unreliability.
- Sends an ack for every packet received.
- Queues up data until there's enough to send as a packet.
- TCP tends to induce packet loss for UDP packets whenever they share a bottleneck node (same LAN/WAN).

## UDP

- *User Datagram Protocol*
- Built on-top of IP, very thin layer over it.
- Unreliable protocol, usually around 1-5% packet loss.
- No guarantee of ordering.
- Minimizes transmission delay.
- Send a packet to destination IP address and port; the packet will get passed from computer to computer and arrive at destination or get lost.
- Receiver simply listens on specific port and gets notified when a packet arrives, with the sender address:port, and packet size.
- One guarantee over IP – a packet will either arrive as a whole (all of it) at destination or not at all (no partial delivery).
- You need to manually break your data up into packets and send them.
- You need to make sure you don't send data too fast for your Internet connection to handle.
- Good for when you want data to get as quickly as possible from client to server without having to wait for lost data to be resent, usually real-time data.
- Examples: real-time gaming, metrics reporting, video/audio streaming.
