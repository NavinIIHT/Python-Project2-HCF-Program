import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from number_to_words import number_to_words
from HCF import get_hcf
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_result_type_for_words(self):
        s=number_to_words(58)
        if type(s)==type(" "):
            with open("output_revised.txt","a") as f:
                f.write("TestResultTypeForWords=True\n")
                print("{}TestResultTypeForWords = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestResultTypeForWords=False\n")
                print("{}TestResultTypeForWords = {}Failed".format(Fore.YELLOW,Fore.RED))
    def test_result_type_for_hcf(self):
        n=get_hcf(10,8)
        if type(n)==type(1):
            with open("output_revised.txt","a") as f:
                f.write("TestResultTypeForHcf=True\n")
                print("{}TestResultTypeForHcf = {}Passed".format(Fore.YELLOW,Fore.GREEN))
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestResultTypeForHcf=False\n")
                print("{}TestResultTypeForHcf = {}Failed".format(Fore.YELLOW,Fore.RED))
