import streamlit as st

st.title("Aplikasi Multi-Fungsi dengan Streamlit")

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Fitur",
    ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"]
)

# =======================
# Fitur 1: Kalkulator
# =======================
if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")

    # Input sebagai teks
    a = st.text_input("Masukkan angka pertama", "0")
    b = st.text_input("Masukkan angka kedua", "0")
    operator = st.selectbox("Pilih operator", ["+", "-", "*", "/"])

    if st.button("Hitung"):
        try:
            a = float(a)
            b = float(b)

            if operator == "+":
                hasil = a + b
            elif operator == "-":
                hasil = a - b
            elif operator == "*":
                hasil = a * b
            elif operator == "/":
                hasil = a / b if b != 0 else "Error (pembagian nol)"

            st.success(f"Hasil: {hasil}")
        except ValueError:
            st.error("Input harus berupa angka!")



# =======================
# Fitur 2: Konversi Suhu
# =======================
elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")
    nilai = st.text_input("Masukkan nilai suhu", "0")
    asal = st.selectbox("Satuan asal", ["Celcius", "Reamur", "Fahrenheit"])
    tujuan = st.selectbox("Konversi ke", ["Celcius", "Reamur", "Fahrenheit"])

    def convert_suhu(val, asal, tujuan):
        if asal == "Celcius":
            c = val
        elif asal == "Reamur":
            c = val * 5/4
        elif asal == "Fahrenheit":
            c = (val - 32) * 5/9

        if tujuan == "Celcius":
            return c
        elif tujuan == "Reamur":
            return c * 4/5
        elif tujuan == "Fahrenheit":
            return (c * 9/5) + 32

    if st.button("Konversi"):
        try:
            nilai = float(nilai)
            hasil = convert_suhu(nilai, asal, tujuan)
            st.success(f"Hasil: {hasil:.2f} {tujuan}")
        except ValueError:
            st.error("Input harus berupa angka!")


# =======================
# Fitur 3: Deret Fibonacci
# =======================
elif menu == "Deret Fibonacci":
    st.header("Deret Fibonacci")
    n = st.text_input("Masukkan jumlah bilangan Fibonacci", "5")

    def fibonacci(n):
        deret = [0, 1]
        while len(deret) < n:
            deret.append(deret[-1] + deret[-2])
        return deret[:n]

    if st.button("Generate"):
        try:
            n = int(n)
            hasil = fibonacci(n)
            st.write("Deret Fibonacci:")
            st.success(hasil)
        except ValueError:
            st.error("Input harus berupa angka bulat!")

