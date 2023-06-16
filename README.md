# Python-Security
The goal of this project is to develop a program that helps identify typosquatted packages on PyPI (Python Package Index). Typosquatting refers to the act of registering packages with similar names to popular packages, often with malicious intent.
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/efcc1e9a-c678-45a0-9972-31454f733928)

_


**The program offers several options:**

In-depth analysis (-a): It performs an analysis of the supplier package, checking its metadata, download statistics, and user feedback.
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/ab0bec27-0ce6-40e5-9c4a-c4233726aeb3)

_
Typosquat check (-b): It checks if the specified package has been typosquatted by comparing its name with similar packages on PyPI. It also displays statistics on typosquatted packages.
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/a490ada4-8630-4bf1-917b-6e72821e6d28)

_
Version report (-r): It generates a detailed report on the versions of the searched package. It retrieves version and release date information from the PyPI RSS feed.
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/9bb84e6f-02d8-4d8c-814e-0a26ec9eefe0)

_
Typosquatted packages list (-l): It lists the typosquatted packages of the searched package. It compares the package name with other similar packages and identifies potential typosquats.
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/a96690cc-cb31-4705-af59-4ca402b8fb57)

______
To use the program, you need to provide the name of the package you want to search for and specify the desired options using command-line arguments. For example, to check if the package "requests" has been typosquatted and display statistics, you would run the command: 
<br>
```python3 typosquat.py requests -b.```
<br>

Similarly, you can use --h if you need help :
<br>
![image](https://github.com/RaphaelBouffault/Python-Security/assets/103072020/a46f26d4-0886-4536-96ab-951dc9c536cd)
