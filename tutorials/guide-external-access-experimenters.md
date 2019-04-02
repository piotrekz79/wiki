<!-- TITLE: Guide: External Access to VxFs for Experimenters -->
<!-- SUBTITLE: A quick summary of operations -->

# Guide: External Access to VxFs for Experimenters
Prior step to this guide is to request the VPN credentials via the ticketing tool, as stated in [5GinFIRE Experimentation Tutorial](http://wiki.5ginfire.eu/5-gin-fire-experimentation-tutorial)

Also, you need to have created your VNFs with specific interfaces destined to connect to the 5GinFIRE management plane. In 5GinFIRE, this management plane is decoupled from the data plane, and therefore demands additional interfaces.

## Windows OS
Download and install [OpenVPN client](https://openvpn.net/index.php/download/community-downloads.html) for Windows

![OpenVPN client download](/uploads/external-access-for-experimenters/openvpndownload.png "OpenVPN client download")

As a response to the Bugzilla ticket, you will receive an OpenVPN Config File (filename.ovpn) and the appropriate VPN credentials. Copy the file into the "ProgramFiles/OpenVPN/config" directory

![OpenVPN Config File location](/uploads/external-access-for-experimenters/openvpnconfigfile.png "OpenVPN Config File location")

Run “OpenVPN GUI” application (via Windows desktop icon, or “ProgramFiles/OpenVPN/bin/openvpn-gui”), click on the up arrow (for hidden icons) in the Windows notification area (step 1 in figure), and then right-click on the OpenVPN GUI hidden icon (step 2). Finally, click “connect”

![Run OpenVPN](/uploads/external-access-for-experimenters/openvpnrun.png "Run OpenVPN")

![OpenVPN Connect](/uploads/external-access-for-experimenters/openvpnconnect.png "OpenVPN Connect")

Insert your VPN credentials and click OK

![OpenVPN Credentials](/uploads/external-access-for-experimenters/openvpncredentials.png "OpenVPN Credentials")

Once connected, you can establish an SSH connection to the gateway (or jump machine): 10.4.255.10, using its credentials (for security reasons you should ask your Mentor for the credentials)

![SSH to Jump Machine](/uploads/external-access-for-experimenters/jumpmachinessh.png "SSH to Jump Machine")

![Jump Machine Credentials](/uploads/external-access-for-experimenters/jumpmachinecredentials.png "Jump Machine Credentials")
 
Finally, from the jump machine you will be able to SSH your own VxFs, with your own credentials. Command will be “ssh [dest-IP]”, where [dest-IP] will be one of those assigned to your VxFs in the 5GinFIRE management network

![SSH to VxF](/uploads/external-access-for-experimenters/vxfssh.png "SSH to VxF")


