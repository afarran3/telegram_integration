from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in telegram_integration/__init__.py
from telegram_integration import __version__ as version

setup(
	name="telegram_integration",
	version=version,
	description="Telegram Integration App For FRAPPE",
	author="Ahmed Al-farran",
	author_email="afarran1992@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
