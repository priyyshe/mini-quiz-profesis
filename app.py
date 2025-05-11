import streamlit as st

st.set_page_config(page_title="Mini Quiz Profesi", page_icon="💼", layout="centered")

# Judul Aplikasi
st.title("🎯 Mini Quiz Profesi")
st.write("Jawablah beberapa pertanyaan berikut untuk mengetahui profesi yang cocok untukmu!")

# Inisialisasi skor
scores = {"Programmer": 0, "Designer": 0, "Data Scientist": 0}

# Pertanyaan dan pilihan
questions = [
    {
        "pertanyaan": "Apa kegiatan favoritmu di waktu luang?",
        "pilihan": {
            "Ngoding atau bikin bot Telegram": "Programmer",
            "Ngulik desain Canva atau gambar di Procreate": "Designer",
            "Eksperimen Excel dan main-main data": "Data Scientist"
        }
    },
    {
        "pertanyaan": "Apa software yang paling kamu suka?",
        "pilihan": {
            "Visual Studio Code": "Programmer",
            "Figma / Adobe XD": "Designer",
            "Jupyter Notebook / Google Colab": "Data Scientist"
        }
    },
    {
        "pertanyaan": "Kamu paling semangat saat...",
        "pilihan": {
            "Bikin aplikasi atau game": "Programmer",
            "Mendesain poster atau UI": "Designer",
            "Analisis tren atau data dari survei": "Data Scientist"
        }
    }
]

# Formulir kuis
with st.form("quiz_form"):
    for idx, q in enumerate(questions):
        jawaban = st.radio(q["pertanyaan"], list(q["pilihan"].keys()), key=idx)
        scores[q["pilihan"][jawaban]] += 1

    submit = st.form_submit_button("Lihat Hasil")

# Tampilkan hasil
if submit:
    hasil = max(scores, key=scores.get)
    st.subheader("🎉 Profesi yang cocok untukmu adalah:")
    if hasil == "Programmer":
        st.success("💻 **Programmer** — Kamu suka logika dan membangun solusi lewat kode!")
        st.image("https://cdn-icons-png.flaticon.com/512/1055/1055687.png", width=100)
    elif hasil == "Designer":
        st.success("🎨 **Designer** — Kamu punya jiwa seni dan suka membuat hal jadi indah!")
        st.image("https://cdn-icons-png.flaticon.com/512/2920/2920244.png", width=100)
    else:
        st.success("📊 **Data Scientist** — Kamu suka berpikir analitis dan memecahkan teka-teki data!")
        st.image("https://cdn-icons-png.flaticon.com/512/4149/4149649.png", width=100)

    st.write("Skor lengkap: ", scores)
