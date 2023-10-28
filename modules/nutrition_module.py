"""power control module your PC"""
import os


class Power:
    @staticmethod
    def off():
        os.system("shutdown /s /t 0")

    @staticmethod
    def reboot():
        os.system("shutdown /r /t 0")

    @staticmethod
    def sleep_mode():
        os.system("shutdown -l")


