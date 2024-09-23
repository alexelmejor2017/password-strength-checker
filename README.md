# Password Strength Evaluation Tool

Hello 👋. The Password Strength Evaluation Tool is a Python tool that allows you to analyze how secure your password is.

## DISCLAIMER

Please note that the Password Strength Evaluation Tool is intended to provide general guidance on password strength and should not be solely relied upon to ensure the security of your online accounts. While this tool can help identify weaknesses in your passwords, it is not a guarantee of safety. No password is completely secure, and even strong passwords can be compromised. It is essential to use a password manager to generate and store unique, complex passwords for each of your online accounts, and regularly changing your passwords and keeping them confidential is crucial to maintaining online security.

## Why did I make this project

Many people use insecure passwords, putting their online accounts at risk. I created this project to help users quickly understand their password security and encourage them to take action to protect their accounts.

## Features

* Provides a score from 1 to 5 based on the complexity of the password.
* Gives recommendations on how to make your password more robust.
* Provides with estimated times that it would take to crack your password using different methods.
* Checks if your password is in the rockyou list, which is a list of 14M+ breached passwords.
* Allows you to use a custom wordlist for the password blacklist check and enable/disable it.

## Requirements

* Python 3.8+
* `zxcvbn` and `colorama` libraries

## Usage

**How to download and run:**

```
git clone https://github.com/alexelmejor2017/Password-Strength-Checker.git
```

```
cd Password-Strength-Checker
```

```
pip install -r requirements.txt --break-system-packages
```

```
python main.py
```

**How to setup:**

You will need to download the [Rockyou List](https://github.com/zacheller/rockyou/raw/master/rockyou.txt.tar.gz), extract the file and paste it in the files directory.

You can customize the password blacklist check in the file `config.ini`

## Thank you

Thanks for using this project! If you found it helpful, please consider starring the repository. If you have any suggestions or improvements, feel free to open an issue or pull request. Your contributions are greatly appreciated!
