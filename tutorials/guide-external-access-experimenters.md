<!-- TITLE: Guide: External Access to VxFs for Experimenters -->
<!-- SUBTITLE: A quick summary of operations -->

# Guide: External Access to VxFs for Experimenters
Prior step to this guide is to request the VPN credentials via the ticketing tool, as stated in [5GinFIRE Experimentation Tutorial](http://wiki.5ginfire.eu/5-gin-fire-experimentation-tutorial)

## Windows OS
Download and install [OpenVPN client](https://openvpn.net/index.php/download/community-downloads.html) for Windows

![OpenVPN client download](/uploads/external-access-for-experimenters/openvpndownload.jpg "OpenVPN client download")

As a response to the Bugzilla ticket, you will receive an OpenVPN Config File (filename.ovpn) and the appropriate VPN credentials. Copy the file into the "ProgramFiles/OpenVPN/config" directory

Run “OpenVPN GUI” application (via Windows desktop icon, or “ProgramFiles/OpenVPN/bin/openvpn-gui”), click on the up arrow (for hidden icons) in the Windows notification area (step 1 in figure), and then right-click on the OpenVPN GUI hidden icon (step 2). Finally, click “connect”
 
Insert your VPN credentials and click OK
 
Once connected, you can establish an SSH connection to the gateway (or jump machine): 10.4.255.10, using its credentials
 
Finally, from the jump machine you will be able to SSH your own VxFs, with your own credentials. Command will be “ssh <dest-IP>”, where <dest-IP> will be one of those assigned to your VxFs in the 5GinFIRE management network




