#!/usr/bin/env python3
# Version 1.1.0
import os
import sys
import webbrowser
from platform import system
from time import sleep

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

logo = """\033[1m\033[37m
     ___       __       __          __  .__   __.      ______   .__   __.  _______         
    /   \     |  |     |  |        |  | |  \ |  |     /  __  \  |  \ |  | |   ____|        
   /  ^  \    |  |     |  |        |  | |   \|  |    |  |  |  | |   \|  | |  |__           
  /  /_\  \   |  |     |  |        |  | |  . `  |    |  |  |  | |  . `  | |   __|          
 /  _____  \  |  `----.|  `----.   |  | |  |\   |    |  `--'  | |  |\   | |  |____         
/__/     \__\ |_______||_______|   |__| |__| \__|     \______/  |__| \__| |_______|        
                                                                                           
 _______   ______   .______       _______ .__   __.      _______. __    ______     _______.
|   ____| /  __  \  |   _  \     |   ____||  \ |  |     /       ||  |  /      |   /       |
|  |__   |  |  |  | |  |_)  |    |  |__   |   \|  |    |   (----`|  | |  ,----'  |   (----`
|   __|  |  |  |  | |      /     |   __|  |  . `  |     \   \    |  | |  |        \   \    
|  |     |  `--'  | |  |\  \----.|  |____ |  |\   | .----)   |   |  | |  `----.----)   |   
|__|      \______/  | _| `._____||_______||__| \__| |_______/    |__|  \______|_______/  
\033[0m"""


all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo)


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = "/home/hackingtoolpath.txt"
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Hacking Tool =>> ").strip()

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Set Path to: {}".format(inpath))
                elif choice == "2":
                    autopath = "/home/hackingtool/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print("Your Default Path Is: {}".format(autopath))
                    sleep(3)
                else:
                    print("Try Again..!!")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline()
                if not os.path.exists(archive):
                    os.mkdir(archive)
                os.chdir(archive)
                AllTools().show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print(
                r"\033[91m Please Run This Tool On A Debian System For Best Results\e[00m"
            )
            sleep(2)
            webbrowser.open_new_tab("https://youtu.be/zuFHa6A_m9g")

        else:
            print("Please Check Your System or Open New Issue ...")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)
