
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import unittest
import sys
sys.path.append("..")
from number_to_words import number_to_words
from HCF import get_hcf
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_exception_revised.txt","w") as f:
            pass
    def test_error_type_for_words(self):
        try:
            number_to_words("58")
            with open("output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForWords=False\n")
                print("{}TestErrorTypeForWords = {}Failed".format(Fore.YELLOW,Fore.RED))
        except ValueError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForWords=True\n")
                print("{}TestErrorTypeForWords = {}Passed".format(Fore.YELLOW,Fore.GREEN))
    def test_error_type_for_hcf(self):
        try:
            get_hcf("58",40)
            with open("output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForHcf=False\n")
                print("{}TestErrorTypeForHcf = {}Failed".format(Fore.YELLOW,Fore.RED))
        except ValueError:
            with open("output_exception_revised.txt","a") as f:
                f.write("TestErrorTypeForHcf=True\n")
                print("{}TestErrorTypeForHcf= {}Passed".format(Fore.YELLOW,Fore.GREEN))
