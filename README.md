# Mac Changer
The tool allows the user to change the MAC address of their network adapter in order to remain anonymous. This would enable the user to put an extra layer of security by hiding their mac addressing and changing it into something else

## Prerequisites
You need to install scapy module in order for it to work   
```pip install scapy-python3```

## Installation
```git clone https://github.com/Saad-20/Mac_Changer.git```    
```cd Mac_Changer```    
```python mac_changer.py --help``` (For Further help)

## Running the MAC Changer
```python mac_changer.py -i {interface name} -m {Enter mac}```    
e.g: ```python mac_changer.py -i wlan0 -m 00:11:22:33:44:55```


