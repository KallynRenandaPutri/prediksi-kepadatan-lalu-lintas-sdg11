# ============================================================
# TAHAP 1 — IMPORT LIBRARY
# ============================================================

import streamlit as st
import pandas as pd
from datetime import date, time
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# ============================================================
# TAHAP 2 — KONFIGURASI DAN JUDUL APLIKASI
# ============================================================

# Mengatur judul tab browser, ikon, dan tata letak aplikasi.

st.set_page_config(
    page_title="Prediksi Kepadatan Lalu Lintas",
    page_icon="🚦",
    layout="wide",
)

st.title("🚦 Klasifikasi Tingkat Kepadatan Lalu Lintas")
st.write(
    "Aplikasi pembelajaran Machine Learning menggunakan Decision Tree Classifier "
    "untuk mendukung SDGs 11."
)

NAMA_FILE = "Metro_Interstate_Traffic_Volume.csv"
LABELS = ["Rendah", "Sedang", "Tinggi"]

# Fitur harus sama dengan notebook Colab.
FITUR = [
    "holiday", "temp_c", "rain_1h", "snow_1h", "clouds_all",
    "hour", "day", "month", "day_of_week", "year",
    "weather_Clear", "weather_Clouds", "weather_Drizzle",
    "weather_Fog", "weather_Haze", "weather_Mist", "weather_Rain",
    "weather_Smoke", "weather_Snow", "weather_Squall",
    "weather_Thunderstorm",
]

# ============================================================
# TAHAP 3 — MEMBACA DAN MEMPERSIAPKAN DATASET
# ============================================================

# Cache menyimpan hasil pemrosesan agar tidak perlu mengulang
# seluruh proses setiap kali Streamlit memperbarui tampilan.

@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv(NAMA_FILE)

    # Ikuti notebook: hapus duplikat sebelum membangun fitur dan target.
    df = df.drop_duplicates().copy()

    df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce")

    # Jika file CSV bersih sudah berisi holiday 0/1, pertahankan nilainya.
    # Jika masih berupa nama hari libur dan nilai kosong, ubah dengan aturan notebook.
    if df["holiday"].dtype == object:
        df["holiday"] = df["holiday"].fillna(0)
        df["holiday"] = (
            df["holiday"].astype(str).str.strip() != "0"
        ).astype(int)
    else:
        df["holiday"] = df["holiday"].fillna(0).astype(int)

    df["hour"] = df["date_time"].dt.hour
    df["day"] = df["date_time"].dt.day
    df["month"] = df["date_time"].dt.month
    df["day_of_week"] = df["date_time"].dt.dayofweek
    df["year"] = df["date_time"].dt.year
    df["temp_c"] = df["temp"] - 273.15

    # Samakan persis dengan notebook: 0.33 dan 0.66, bukan 1/3 dan 2/3.
    q1 = df["traffic_volume"].quantile(0.33)
    q2 = df["traffic_volume"].quantile(0.66)

    def kategori_traffic(volume):
        if volume <= q1:
            return "Rendah"
        elif volume <= q2:
            return "Sedang"
        return "Tinggi"

    df["Traffic_Level"] = df["traffic_volume"].apply(kategori_traffic)
    df = df.dropna(subset=["date_time", "Traffic_Level", "weather_main"]).copy()

    # One-hot encoding cuaca seperti notebook.
    df = pd.get_dummies(
        df,
        columns=["weather_main"],
        prefix="weather",
        dtype=int,
    )

    # Pastikan seluruh kolom fitur yang digunakan Colab tersedia.
    for feature in FITUR:
        if feature not in df.columns:
            df[feature] = 0

    X = df[FITUR].copy()
    y = df["Traffic_Level"].copy()
    return df, X, y, q1, q2

# ============================================================
# TAHAP 4 — MENJALANKAN PEMROSESAN DATA
# ============================================================

# Menjalankan fungsi persiapan data.
# Menampilkan pesan jika file tidak ditemukan atau data gagal diproses.

try:
    df, X, y, q1, q2 = load_and_prepare_data()
except FileNotFoundError:
    st.error(
        f"File '{NAMA_FILE}' tidak ditemukan. Letakkan file CSV tersebut "
        "di folder yang sama dengan app.py."
    )
    st.stop()
except Exception as exc:
    st.error(f"Dataset gagal diproses: {exc}")
    st.stop()

# ============================================================
# TAHAP 5 — MEMBAGI DATA LATIH DAN DATA UJI
# ============================================================

# Samakan split dan parameter model dengan notebook Colab.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# ============================================================
# TAHAP 6 — MELATIH MODEL DECISION TREE
# ============================================================

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ============================================================
# TAHAP 7 — EVALUASI MODEL
# ============================================================

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(
    y_test,
    y_pred,
    labels=LABELS,
    output_dict=True,
    zero_division=0,
)
cm = confusion_matrix(y_test, y_pred, labels=LABELS)

st.subheader("Evaluasi Model")
c1, c2, c3 = st.columns(3)
c1.metric("Jumlah Data", f"{len(df):,}")
c2.metric("Akurasi Data Uji", f"{accuracy:.4%}")
c3.metric("Jumlah Fitur", len(FITUR))
st.caption(f"Batas kelas Colab: q1 = {q1:g}, q2 = {q2:g}.")

st.write("**Classification Report**")
st.dataframe(pd.DataFrame(report).T.round(6))

st.write("**Confusion Matrix**")
st.caption("Baris = kelas sebenarnya; kolom = hasil prediksi.")
st.dataframe(
    pd.DataFrame(
        cm,
        index=[f"Aktual {label}" for label in LABELS],
        columns=[f"Prediksi {label}" for label in LABELS],
    ),
    use_container_width=True,
)

# ============================================================
# TAHAP 8 — MENAMPILKAN FITUR PALING BERPENGARUH
# ============================================================

st.divider()
st.subheader("Fitur Paling Berpengaruh")
importance = pd.DataFrame({
    "Fitur": FITUR,
    "Importance": model.feature_importances_,
}).sort_values("Importance", ascending=True)
st.bar_chart(importance.set_index("Fitur"), horizontal=True)
st.caption(
    "Feature importance menunjukkan kontribusi relatif fitur pada model, "
    "bukan bukti sebab-akibat."
)

# ============================================================
# TAHAP 9 — FORM INPUT PREDIKSI
# ============================================================

st.divider()
st.subheader("Prediksi Tingkat Kepadatan")
st.write("Masukkan waktu dan kondisi cuaca untuk memperoleh prediksi model.")

weather_options = sorted(df["weather_main"].dropna().unique().tolist()) if "weather_main" in df.columns else [
    "Clear", "Clouds", "Drizzle", "Fog", "Haze", "Mist", "Rain", "Smoke", "Snow", "Squall", "Thunderstorm"
]

with st.form("form_prediksi"):
    left, right = st.columns(2)
    with left:
        tanggal = st.date_input(
            "Tanggal", value=date(2018, 9, 30),
            min_value=date(2012, 10, 2), max_value=date(2018, 9, 30)
        )
        jam = st.time_input("Jam", value=time(8, 0))
        holiday_choice = st.selectbox("Hari libur?", ["Tidak", "Ya"])
        temp_c = st.number_input("Suhu (°C)", min_value=-50.0, max_value=60.0, value=20.0, step=0.5)
    with right:
        weather = st.selectbox("Kondisi cuaca", weather_options)
        rain = st.number_input("Curah hujan (mm/jam)", min_value=0.0, value=0.0, step=0.1)
        snow = st.number_input("Curah salju (mm/jam)", min_value=0.0, value=0.0, step=0.1)
        clouds = st.slider("Tutupan awan (%)", min_value=0, max_value=100, value=40)
    submit = st.form_submit_button("Prediksi Kepadatan", type="primary")

# ============================================================
# TAHAP 10 — MEMPROSES INPUT DAN MENAMPILKAN PREDIKSI
# ============================================================

if submit:
    dt = pd.Timestamp.combine(tanggal, jam)
    row = {
        "holiday": 1 if holiday_choice == "Ya" else 0,
        "temp_c": temp_c,
        "rain_1h": rain,
        "snow_1h": snow,
        "clouds_all": clouds,
        "hour": dt.hour,
        "day": dt.day,
        "month": dt.month,
        "day_of_week": dt.dayofweek,
        "year": dt.year,
    }
    for feature in FITUR:
        if feature.startswith("weather_"):
            row[feature] = 1 if feature == f"weather_{weather}" else 0
    input_df = pd.DataFrame([row], columns=FITUR).fillna(0)
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    st.subheader("Hasil Prediksi")
    if prediction == "Rendah":
        st.success("🟢 Tingkat kepadatan: RENDAH")
    elif prediction == "Sedang":
        st.warning("🟡 Tingkat kepadatan: SEDANG")
    else:
        st.error("🔴 Tingkat kepadatan: TINGGI")

    st.write("Probabilitas setiap kelas:")
    for class_name, probability in zip(model.classes_, probabilities):
        st.write(f"**{class_name}:** {probability:.2%}")
        st.progress(float(probability))

    st.info(
        "Ini merupakan prediksi dari pola historis dataset Minnesota, AS, "
        "bukan informasi lalu lintas real-time atau model yang divalidasi "
        "untuk kondisi jalan di Indonesia."
    )

with st.expander("Tentang aplikasi"):
    st.write(
        "Pembentukan target, 21 fitur, pembagian data 80:20, random_state=42, "
        "stratify=y, dan DecisionTreeClassifier(random_state=42) diselaraskan "
        "dengan notebook Colab yang diberikan. Hasil evaluasi akan identik hanya "
        "jika dataset dan preprocessing juga identik."
    )
