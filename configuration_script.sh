#!/bin/bash
YELLOW='\033[1;31;100m'
RED='\033[1;31m'
NC='\033[0m' # No Color
ALERT='\033[1;32;104m'
HEADER='\033[1;31;42m'
printf "${RED}******************************************************************${NC}\n"
printf "${RED}******************************************************************${NC}\n"
printf "	 \n"
printf "	 \n"
printf "        Welcome to ${RED}foxy_swarm${NC} configuration script!\n"
printf "	 \n"
printf "	 \n"
printf "${RED}******************************************************************${NC}\n"
sudo echo "Please run \"ifconfig\" on another terminal and enter the name of wireless interface (wlan0, wlo1, etc)..."
read interface_name
echo ""
printf "${RED}******************************************************************${NC}\n"
sudo echo "Please select an IP for the current device..."
read ip
echo ""
printf "${RED}******************************************************************${NC}\n"
printf "${RED}******************************************************************${NC}\n"
echo "Configuring /etc/network/interfaces..."
echo "auto $interface_name" | sudo tee --append /etc/network/interfaces
echo "iface $interface_name inet static" | sudo tee --append /etc/network/interfaces
echo "    address $ip" | sudo tee --append /etc/network/interfaces
echo "    netmask 255.255.255.0" | sudo tee --append /etc/network/interfaces
echo "    wireless-channel 1" | sudo tee --append /etc/network/interfaces
echo "    wireless-essid foxyAdHoc" | sudo tee --append /etc/network/interfaces
echo "    wireless-mode ad-hoc" | sudo tee --append /etc/network/interfaces
echo ""
sudo echo "Ad-hoc network is configured with SSID foxyAdHoc."
printf "${RED}******************************************************************${NC}\n"
printf "${RED}******************************************************************${NC}\n"
sudo apt-get install ros-kinetic-multimaster-fkie
printf "${RED}******************************************************************${NC}\n"
printf "${RED}******************************************************************${NC}\n"
printf "foxy_swarm configurations are completed.\n"
printf "			\n"
printf "	${RED}foxySwarm${NC}: Ad-hoc networking project for swarm of drones\n"
printf "		${HEADER}KOVAN Research Laboratory${NC} / ${HEADER}Middle East Technical University${NC} \n"
printf "	 \n"
printf "	${RED}Developer${NC}: \n"
printf "		${HEADER}M. Rasit Ozdemir${NC}(M.Sc. Student)\n"
printf "	\n"
printf "	This project was done under the supervision of ${HEADER}Dr. Erol Şahin${NC} \n	with the infrastructural support of ${HEADER}KOVAN Research Laboratory${NC}.\n"
printf "	Thanks to my friend ${HEADER}Burak Hocaoğlu${NC}(M.Sc. Student) for his support.\n"
printf "	\n"
printf "${RED}******************************************************************${NC}\n"
printf "${RED}******************************************************************${NC}\n"
echo "Press [ENTER] to reboot device or CTRL+C to exit without reboot. Notice"
echo "that network changes will not be applied without reboot."
read cnt
sudo reboot







