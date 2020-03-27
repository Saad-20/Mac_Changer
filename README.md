# Mac_Changer
To change the MAC address of your network adapter in order to remain anonymous. This would enable the user to put an extra layer of security

## Prerequisites
You need to install scapy module in order for it to work   
```pip install scapy-python3```

## Runnining the Mac_Changer
cd mac_changer (Goto directory)
```python mac_changer.py --help``` (For Further help)

## Changing MAC address
```python mac_changer.py -i {interface name} -m {Enter mac}```

e.g: ```python mac_changer.py -i wlan0 -m 00:11:22:33:44:55```


