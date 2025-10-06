import streamlit as st
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

# ---------- Helper Functions ----------
def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def aes_decrypt(enc_text, key):
    raw = base64.b64decode(enc_text)
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def des_encrypt(text, key):
    cipher = DES.new(key, DES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def des_decrypt(enc_text, key):
    raw = base64.b64decode(enc_text)
    nonce, tag, ciphertext = raw[:8], raw[8:24], raw[24:]
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()

def rsa_generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(text.encode())
    return base64.b64encode(ciphertext).decode()

def rsa_decrypt(enc_text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(base64.b64decode(enc_text))
    return plaintext.decode()

# ---------- Streamlit App ----------
st.set_page_config(page_title="🔐 Text Encryption Tool", page_icon="🔑", layout="wide")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Multi-Algorithm Text Encryption Tool</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Encrypt & Decrypt Text using AES, DES, or RSA</p>", unsafe_allow_html=True)

# Create Tabs
tab1, tab2, tab3 = st.tabs(["AES 🔑", "DES 🔑", "RSA 🔑"])

# ---------- AES Tab ----------
with tab1:
    st.subheader("AES Encryption (Symmetric)")
    text_input = st.text_area("Enter text to encrypt:", key="aes_text")
    aes_key_input = st.text_input("Enter 16-char key 🔑", type="password", key="aes_key")
    
    if st.button("Encrypt & Decrypt AES", key="aes_button"):
        if len(aes_key_input) != 16:
            st.error("❌ AES key must be exactly 16 characters!")
        else:
            key = aes_key_input.encode()
            try:
                encrypted = aes_encrypt(text_input, key)
                decrypted = aes_decrypt(encrypted, key)
                st.success(f"Encrypted Text: {encrypted}")
                st.info(f"Decrypted Text: {decrypted}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# ---------- DES Tab ----------
with tab2:
    st.subheader("DES Encryption (Symmetric)")
    text_input = st.text_area("Enter text to encrypt:", key="des_text")
    des_key_input = st.text_input("Enter 8-char key 🔑", type="password", key="des_key")
    
    if st.button("Encrypt & Decrypt DES", key="des_button"):
        if len(des_key_input) != 8:
            st.error("❌ DES key must be exactly 8 characters!")
        else:
            key = des_key_input.encode()
            try:
                encrypted = des_encrypt(text_input, key)
                decrypted = des_decrypt(encrypted, key)
                st.success(f"Encrypted Text: {encrypted}")
                st.info(f"Decrypted Text: {decrypted}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# ---------- RSA Tab ----------
with tab3:
    st.subheader("RSA Encryption (Asymmetric)")
    text_input = st.text_area("Enter text to encrypt:", key="rsa_text")
    
    if st.button("Encrypt & Decrypt RSA", key="rsa_button"):
        try:
            private_key, public_key = rsa_generate_keys()
            encrypted = rsa_encrypt(text_input, public_key)
            decrypted = rsa_decrypt(encrypted, private_key)
            st.success(f"Encrypted Text: {encrypted}")
            st.info(f"Decrypted Text: {decrypted}")
            st.markdown("**Public Key:**")
            st.code(public_key.decode())
            st.markdown("**Private Key:**")
            st.code(private_key.decode())
        except Exception as e:
            st.error(f"Error: {str(e)}")

# ---------- Footer ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Developed with ❤️ by Surya Pratap Singh | Cybersecurity Project</p>", unsafe_allow_html=True)
