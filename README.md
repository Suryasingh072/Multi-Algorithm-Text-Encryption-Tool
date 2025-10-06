# Multi-Algorithm Text Encryption Tool

A Streamlit web app to encrypt and decrypt text using three algorithms — AES, DES, and RSA.  
Designed for secure data protection and learning cryptography concepts.

## Features

- AES (Advanced Encryption Standard) – Fast and secure symmetric encryption  
- DES (Data Encryption Standard) – Legacy symmetric encryption for demo purposes  
- RSA (Rivest–Shamir–Adleman) – Asymmetric encryption with public/private keys  
- Streamlit Interface – Interactive and user-friendly  
- Copy or download encrypted/decrypted text easily  
- Great for learning encryption and cybersecurity basics  

## How It Works

1. Choose an encryption algorithm (AES, DES, or RSA).  
2. Enter your text input and key (if required).  
3. Click Encrypt to convert plain text into ciphertext.  
4. Click Decrypt to restore the original message.  
5. For RSA, the app automatically generates a key pair.  

## How to Run

1. Install Python 3.8 or higher  
2. Install required packages:
ip install -r requirements.txt

3. Run the app:


streamlit run app.py

4. Open your browser at http://localhost:8501

## Security Notes

- AES key must be 16 characters (128-bit)  
- DES key must be 8 characters (64-bit)  
- RSA generates public/private keys automatically  
- Keep private keys secure  
- For educational and demo purposes only  

## Developed By

Surya Pratap Singh  
Cybersecurity Enthusiast & Developer
