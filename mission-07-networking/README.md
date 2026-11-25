# Mission 7 — How computers communicate

## 1. Task / objective

Explain basic network types and concepts, observe network lookup and connectivity information, and describe what happens when a website opens.

## 2. Work completed

Completed the network-concepts table, ran connectivity and DNS tests from Terminal, and wrote a step-by-step explanation of how a website loads.

## 3. Commands / tools used

- `ping -c 4 example.com` — tested connectivity to a public website.
- `nslookup example.com` — looked up the DNS record for a domain.

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
|---------|------------------------------|---------|
| LAN | A network covering a small area, such as a home, lab or office. Devices connect through a switch or Wi-Fi router. | The Wi-Fi network in my house connecting my laptop, phone and printer. |
| MAN | A network covering a city or large campus area, larger than a LAN but smaller than a WAN. | A university network linking multiple buildings across campus. |
| WAN | A network covering large geographical areas, often connecting many LANs together across cities or countries. | The internet itself is the largest WAN, connecting networks worldwide. |
| DNS | Translates a human-readable domain name into an IP address so the computer knows where to send the request. | Typing `google.com` — DNS translates that to an IP like `142.250.x.x` so my browser can reach the server. |
| Router | Connects networks and forwards data packets between them, choosing the best path for each packet. | My home router connects my LAN to my internet service provider's network. |
| Protocol | A set of rules devices follow to communicate, defining how data is formatted, sent and received. | HTTP is a protocol that web browsers and servers use to exchange web pages. |
| Packet switching | Data is divided into small packets that travel independently across a network and are reassembled at the destination. | Watching a video — the video data is split into packets that may take different routes but arrive and play in order. |
| Client-server | A model where a client requests a service and a server provides it. The client initiates; the server responds. | My browser (client) requests a web page from Google's server, which sends back the page content. |

### Task 7.2 — Observe network information

- **Connectivity test (`ping`):** A connectivity test sends small packets to a server and waits for a reply. It helps you check whether your computer can reach a remote machine and how long the round trip takes (latency). I ran `ping -c 4 example.com` and received replies, confirming my network connection was working.
- **DNS lookup (`nslookup`):** A DNS lookup shows the IP address associated with a domain name and which DNS server answered the query. I ran `nslookup example.com` and it returned an IP address (e.g. `93.184.216.34`), showing the mapping from the name to the numerical address.
- **Role of DNS when browsing:** When I type a website name into my browser, the browser asks a DNS server to translate that name into an IP address. Without DNS, I would need to remember and type numerical IP addresses for every website.

### Task 7.3 — What happens when you open a website

1. **You type the URL:** You enter a website address (e.g. `www.example.com`) into your browser (the client).
2. **DNS resolution:** Your browser asks a DNS server to look up the domain name and return the corresponding IP address.
3. **Connection to the server:** Using the IP address, your browser sends a request across the network. The request travels through your router and across the internet (possibly through multiple routers) to reach the web server.
4. **Server processes the request:** The web server receives the request, finds the requested page or resource, and prepares a response.
5. **Response travels back:** The server sends the response (HTML, CSS, images, etc.) back across the network as packets. These packets may travel different routes but all arrive at your computer.
6. **Browser renders the page:** Your browser receives and reassembles the packets, then renders the HTML, applies the CSS styling, and displays the finished web page on your screen.

Throughout this process, the communication follows the **HTTP/HTTPS protocol**, the data travels as **packets** (packet switching), and the interaction follows the **client-server model** (your browser is the client, the website's computer is the server).

## 5. Difficulties faced

No major difficulties. The `nslookup` output format was initially unfamiliar.

## 6. How I resolved them

I read each line of the `nslookup` output carefully and identified which part was the DNS server address and which was the resolved IP address for the domain.

## 7. Evidence / files

- This README with the concepts table, observations and website-loading explanation.

## 8. Commit details

- **Commit message:** "Explain networking concepts and website communication"
- Pushed to GitHub and verified.
