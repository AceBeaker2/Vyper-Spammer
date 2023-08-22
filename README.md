
# Vyper Spammer

A service inspired by Kian Brose to abuse referral giveaways

Kian made a video about this, you should watch it [here](https://www.youtube.com/KianBrose)

## Deployment

To use this you need to buy a domain. Then add the following DNS records:

I'll assume that you are running this with

- Public ip: 210.210.210.210 (You can find yours here https://4.ident.me/)
- Localhost ip: 192.168.0.10 (Open a console and write `ip a` or `ifconfig` on mac/linux, and `ipconfig` on windows. It often starts with either `192.168` or `10.10`)
- Domain: yourdomain.com

### DNS records
Add the following DNS records on your registrar, I recommend [cloudflare](https://cloudflare.com/)
```bash
Type: A
Name: example.com
Content/Value: 210.210.210.210
TTL: Automatic
```

```bash
Type: MX
Name: example.com
Content/Value: example.com
Priority: 10
TTL: Automatic
```
### Port forwarding
On whatever computer you are running you will have to make sure your router is port forwarded for the port 25 and routes its traffic to the private ip of where the code will run. If it will run on 192.168.0.10, port forward 192.168.0.10 port 25. If you don't know how to do it your ISP might be blocking you or your router is just bad, there are tons of guides online, even on my channel.

### Setup config.py


Inside of the config.py file, set the following values:
```bash
domain_name = 'yourdomain.com'
ipv4_address = '192.168.0.10'
```
If on windows set
```bash
parallel = False
processes = 1
```
If on Linux/MacOS set
```
parallel = True
processes = 15
```
Set
```
ref_link = 'https://vy.tc/your-referral-link'
```

## Running
Start the mail server by running:
```bash
python3 abuseserver.py
```
then start the spammer with:
```bash
python3 main.py
```
The mail server might complain if you don't use sudo permissions, run as admin on windows or on mac/linux `sudo python3 abuseserver.py`
## Authors

- [Unknown Star (YouTube)](https://www.youtube.com/@bungsbodulus)
