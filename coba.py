import streamlit as st
import numpy as np
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Aplikasi Multi-Fitur",
    page_icon="🤖",
    layout="centered"
)

# CSS untuk styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        background-color: #f8f9fa;
        border-left: 4px solid #1f77b4;
    }
    .stButton button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header aplikasi
st.markdown('<h1 class="main-header">Aplikasi Multi-Fitur</h1>', unsafe_allow_html=True)
st.write("Pilih salah satu fitur dari menu di bawah:")

# Membuat menu pilihan dengan tabs
tab1, tab2, tab3 = st.tabs(["🧮 Kalkulator", "🌡️ Konversi Suhu", "🔢 Baris Fibonacci"])

# Fitur 1: Kalkulator
with tab1:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("Kalkulator Sederhana")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num1 = st.number_input("Masukkan angka pertama", value=0, key="num1")
    
    with col2:
        operator = st.selectbox(
            "Pilih operator",
            ("+", "-", "×", "÷", "^"),
            key="operator"
        )
    
    with col3:
        num2 = st.number_input("Masukkan angka kedua", value=0, key="num2")
    
    if st.button("Hitung", key="hitung"):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "×":
            result = num1 * num2
        elif operator == "÷":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Pembagian dengan nol"
        elif operator == "^":
            result = num1 ** num2
        
        st.success(f"Hasil: **{result}**")
    st.markdown('</div>', unsafe_allow_html=True)

# Fitur 2: Konversi Suhu
with tab2:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("Konversi Suhu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        suhu_input = st.number_input("Masukkan nilai suhu", value=0, key="suhu")
        satuan_asal = st.selectbox(
            "Dari satuan:",
            ("Celcius", "Reamur", "Fahrenheit", "Kelvin"),
            key="satuan_asal"
        )
    
    with col2:
        satuan_tujuan = st.selectbox(
            "Ke satuan:",
            ("Celcius", "Reamur", "Fahrenheit", "Kelvin"),
            key="satuan_tujuan"
        )
    
    if st.button("Konversi", key="konversi"):
        if satuan_asal == satuan_tujuan:
            hasil = suhu_input
        else:
            # Konversi ke Celcius dulu
            if satuan_asal == "Celcius":
                celcius = suhu_input
            elif satuan_asal == "Reamur":
                celcius = suhu_input * 5/4
            elif satuan_asal == "Fahrenheit":
                celcius = (suhu_input - 32) * 5/9
            elif satuan_asal == "Kelvin":
                celcius = suhu_input - 273.15
            
            # Konversi dari Celcius ke satuan tujuan
            if satuan_tujuan == "Celcius":
                hasil = celcius
            elif satuan_tujuan == "Reamur":
                hasil = celcius * 4/5
            elif satuan_tujuan == "Fahrenheit":
                hasil = (celcius * 9/5) + 32
            elif satuan_tujuan == "Kelvin":
                hasil = celcius + 273.15
        
        st.success(f"Hasil konversi: **{hasil:.4f}° {satuan_tujuan}**")
    st.markdown('</div>', unsafe_allow_html=True)

# Fitur 3: Baris Fibonacci
with tab3:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("Baris Fibonacci")
    
    st.write(
        "Pilih jumlah nilai Fibonacci yang ingin ditampilkan", 
        "(minimal 1, maksimal 100)"
    )
    
    n = st.number_input (
        "Jumlah nilai Fibonacci", 
        min_value=1, 
        max_value=100, 
        value=10,
        step=1,
        key="n_fibonacci"
    )
    
    if st.button("Tampilkan Baris Fibonacci", key="tampilkan_fibonacci"):
        fibonacci = [0, 1]
        
        if n == 1:
            fibonacci = [0]
        elif n > 2:
            for i in range(2, n):
                next_value = fibonacci[i-1] + fibonacci[i-2]
                fibonacci.append(next_value)
        
        # Menampilkan deret Fibonacci
        st.write("**Baris Fibonacci:**")
        fib_text = ", ".join(str(x) for x in fibonacci)
        st.write(fib_text)
        
        # Visualisasi sederhana
        st.write("**Visualisasi:**")
        st.line_chart(fibonacci)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6c757d;'>"
    "Aplikasi Multi-Fitur © 2023 | Kalkulator, Konversi Suhu, dan Baris Fibonacci"
    "</div>",
    unsafe_allow_html=True
)