
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gold Market Dashboard", layout="wide")
st.title("📊 Gold Market Dashboard (ย้อนหลัง 1 ปี)")

uploaded_file = st.file_uploader("📥 อัปโหลดไฟล์ราคาทองและ SPDR (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        df_price = pd.read_excel(uploaded_file, sheet_name=0)
        df_spdr = pd.read_excel(uploaded_file, sheet_name=1)

        df_price["วันที่"] = pd.to_datetime(df_price["วันที่"])
        df_spdr["วันที่"] = pd.to_datetime(df_spdr["วันที่"])

        with st.sidebar:
            st.header("🕒 เลือกช่วงเวลา")
            option = st.selectbox("เลือกช่วงเวลา", ["7 วันล่าสุด", "30 วันล่าสุด", "90 วันล่าสุด", "ย้อนหลัง 1 ปี"])

        def filter_by_days(df, days):
            latest_date = df["วันที่"].max()
            return df[df["วันที่"] >= latest_date - pd.Timedelta(days=days)]

        if option == "7 วันล่าสุด":
            df_price = filter_by_days(df_price, 7)
            df_spdr = filter_by_days(df_spdr, 7)
        elif option == "30 วันล่าสุด":
            df_price = filter_by_days(df_price, 30)
            df_spdr = filter_by_days(df_spdr, 30)
        elif option == "90 วันล่าสุด":
            df_price = filter_by_days(df_price, 90)
            df_spdr = filter_by_days(df_spdr, 90)

        st.subheader("📈 ราคาทองย้อนหลัง")
        st.line_chart(df_price.set_index("วันที่")["ราคาทอง (USD/Oz)"])

        st.subheader("🏦 ปริมาณทองคำที่ SPDR ถือ")
        st.line_chart(df_spdr.set_index("วันที่")["SPDR ถือทอง (ตัน)"])

        st.subheader("🔔 แจ้งเตือน SPDR ซื้อ/ขายผิดปกติ")
        alerts = df_spdr[df_spdr["SPDR ถือทอง (ตัน)"].diff().abs() > 10]
        if not alerts.empty:
            st.warning("พบการเปลี่ยนแปลงมากกว่า 10 ตัน")
            st.dataframe(alerts[["วันที่", "SPDR ถือทอง (ตัน)"]])
        else:
            st.success("ไม่มีความเคลื่อนไหวผิดปกติในช่วงนี้")

    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {e}")
else:
    st.info("กรุณาอัปโหลดไฟล์ .xlsx เพื่อเริ่มวิเคราะห์")
