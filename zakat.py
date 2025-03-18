import streamlit as st
import requests
from datetime import datetime
import pytz

# پیج سیٹ اپ
st.set_page_config(page_title="🌙 اسلامی کیلکولیٹر - زکوٰۃ و فطرہ", page_icon="🌙", layout="centered")

# کسٹم CSS
st.markdown("""
<style>
    .main {background:#f5f5f5; padding:20px;}
    .header {background:#2c5f2d; color:white; padding:2rem; text-align:center; border-radius:10px; border: 2px solid lightgreen;}
    .section {background:white; padding:20px; border-radius:10px; margin-bottom:20px; box-shadow:0 2px 5px rgba(0,0,0,0.1); border: 2px solid lightgreen;}
    .calculator {background:#e8f5e9; padding:15px !important; border: 2px solid lightgreen;}
    footer {text-align:center; padding:1rem; margin-top:20px; border: 2px solid lightgreen;}
    .answer-box {border-left:4px solid #2c5f2d; padding:10px; margin:10px 0; background-color: #ffffcc; border: 2px solid lightgreen;}
    .sidebar {background:#f5f5f5; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1); border: 2px solid lightgreen;}
    .green-text {color: green; margin-bottom: 10px;}
    .red-text {color: red; margin-bottom: 10px;}
    .stButton>button {background-color: green; color: white;}
    .time-date {font-size: 1.5rem; margin-top: 10px;}
</style>
""", unsafe_allow_html=True)

# ہیڈر
st.markdown('<div class="header"><h1>🌙 اسلامی کیلکولیٹر - زکوٰۃ و فطرہ</h1><p>زکوٰۃ، فطرہ اور کرنسی کنورٹر</p></div>', unsafe_allow_html=True)

# پاکستان کا وقت اور تاریخ
pakistan_tz = pytz.timezone('Asia/Karachi')
pakistan_time = datetime.now(pakistan_tz).strftime('%Y-%m-%d %H:%M:%S')
st.markdown(f'<div class="header time-date"><p>🕒 پاکستان کا وقت اور تاریخ: {pakistan_time}</p></div>', unsafe_allow_html=True)

# نماز کے اوقات
st.markdown("""
<div class="header time-date">
    <h3>نماز کے اوقات</h3>
    <ul>
        <li>فجر: 5:00 AM</li>
        <li>ظہر: 1:30 PM</li>
        <li>عصر: 5:00 PM</li>
        <li>مغرب: 6:45 PM</li>
        <li>عشاء: 8:00 PM</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ------------------------- زکوٰۃ کی تفصیل -------------------------
with st.expander("**زکوٰۃ کیا ہے؟**", expanded=True):
    st.markdown("""
    <div class="answer-box">
        <h3>❞ زکوٰۃ کی تعریف اور اہمیت ❝</h3>
        <p><strong>تعریف:</strong> زکوٰۃ اسلام کے پانچ ارکان میں سے ایک ہے جو مال کی صفائی اور غریبوں کی مدد کے لیے ادا کی جاتی ہے۔</p>
        <ul>
            <li>📜 <strong class="red-text">قرآنی حکم:</strong> "اور نماز قائم کرو اور زکوٰۃ دو" (سورہ البقرہ:43)</li>
            <li>💵 <strong class="red-text">نصاب:</strong> سونے پر 7.5 تولہ یا چاندی پر 52.5 تولہ (یا اس کی مالیت)</li>
            <li>📅 <strong class="red-text">وقت:</strong> مال پر ایک قمری سال (354 دن) گزرنے پر</li>
            <li>📊 <strong class="red-text">شرح:</strong> کل مال کا 2.5%</li>
        </ul>
        <p>📜 <strong class="red-text">حدیث:</strong> "جو شخص اپنے مال کی زکوٰۃ ادا کرتا ہے، اللہ تعالیٰ اس کے مال میں برکت عطا فرماتا ہے" (بخاری)</p>
        <p>📜 <strong class="red-text">حدیث:</strong> "زکوٰۃ اسلام کے ستونوں میں سے ایک ستون ہے" (مسلم)</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------------- فطرہ کی تفصیل -------------------------
with st.expander("**فطرہ کیا ہے؟**", expanded=True):
    st.markdown("""
    <div class="answer-box">
        <h3>❞ فطرہ کی تعریف اور اہمیت ❝</h3>
        <p><strong>تعریف:</strong> فطرہ رمضان کے اختتام پر ہر مسلمان پر واجب ہونے والی عبادت ہے جو غریبوں کو دی جاتی ہے۔</p>
        <ul>
            <li>📜 <strong class="red-text">حدیث:</strong> "رسول اللہ ﷺ نے فطرہ فرض کیا تاکہ روزے لغو باتوں سے پاک ہوں" (بخاری)</li>
            <li>🌾 <strong class="red-text">اقسام:</strong> گندم (2.7 کلو)، جو (3.8 کلو)، کھجور (3.6 کلو)، یا ان کی مالیت</li>
            <li>⏰ <strong class="red-text">وقت:</strong> رمضان کے آخری دن سے عید کی نماز تک</li>
        </ul>
        <p>📜 <strong class="red-text">حدیث:</strong> "فطرہ ہر مسلمان پر واجب ہے، چاہے وہ مرد ہو یا عورت، بچہ ہو یا بالغ" (ترمذی)</p>
        <p>📜 <strong class="red-text">حدیث:</strong> "فطرہ غریبوں کی مدد کے لیے ہے تاکہ وہ بھی عید کی خوشیوں میں شامل ہو سکیں" (ابو داؤد)</p>
    </div>
    """, unsafe_allow_html=True)

    
# ------------------------- زکوٰۃ اور فطرہ کب ادا کریں -------------------------
with st.expander("**زکوٰۃ اور فطرہ کب ادا کریں؟**", expanded=True):
    st.markdown("""
    <div class="answer-box">
        <h3>❞ زکوٰۃ اور فطرہ کی ادائیگی کا وقت ❝</h3>
        <p><strong class="red-text">زکوٰۃ:</strong> زکوٰۃ اس وقت واجب ہوتی ہے جب آپ کے پاس نصاب کی مقدار میں مال ہو اور اس پر ایک قمری سال (354 دن) گزر جائے۔ زکوٰۃ کی ادائیگی کسی بھی وقت کی جا سکتی ہے جب یہ واجب ہو جائے، لیکن رمضان کے مہینے میں اس کی ادائیگی کا زیادہ ثواب ہے۔</p>
        <p><strong class="red-text">فطرہ:</strong> فطرہ رمضان کے آخری دن سے عید کی نماز تک ادا کیا جاتا ہے۔ یہ ہر مسلمان پر واجب ہے جو اپنی بنیادی ضروریات سے زائد مال رکھتا ہو۔</p>
    </div>
    """, unsafe_allow_html=True)

    

# ------------------------- زکوٰۃ کیلکولیٹر -------------------------
with st.expander("**زکوٰۃ کیلکولیٹر**", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        zakat_amount = st.number_input("کل مال (روپے میں):", min_value=0, step=1000)
    with col2:
        if st.button("زکوٰۃ معلوم کریں"):
            zakat = (zakat_amount * 2.5) / 100
            st.success(f"زکوٰۃ: **{zakat:,.0f} روپے**")

# ------------------------- فطرہ کیلکولیٹر -------------------------
with st.expander("**فطرہ کیلکولیٹر**", expanded=True):
    fitra_type = st.selectbox("فطرہ کی قسم:", ["گندم (2.7 کلو)", "جو (3.8 کلو)", "کشمش (5.5 کلو)", "نقد رقم"])
    persons = st.number_input("افراد کی تعداد:", min_value=1, value=1)
    
    if st.button("فطرہ معلوم کریں"):
        if "نقد" in fitra_type:
            fitra_per_person = 300  # اپ ڈیٹ کر سکتے ہیں
            total = fitra_per_person * persons
        else:
            rates = {"گندم": 200, "جو": 300, "کشمش": 500}  # مثال کے لیے
            total = rates[fitra_type.split(" ")[0]] * persons
        st.success(f"کل فطرہ: **{total:,.0f} روپے**")

# ------------------------- کرنسی کنورٹر -------------------------
with st.expander("**کرنسی کنورٹر**", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        amount = st.number_input("رقم درج کریں:", min_value=0.0)
    with col2:
        from_currency = st.selectbox("From:", ["PKR", "USD", "EUR", "SAR"])
    with col3:
        to_currency = st.selectbox("To:", ["PKR", "USD", "EUR", "SAR"])
    
    if st.button("کنورٹ کریں"):
        try:
            response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
            data = response.json()
            converted = data['rates'][to_currency] * amount
            st.success(f"**{amount} {from_currency}** = **{converted:.2f} {to_currency}**")
        except Exception as e:
            st.error(f"کنورژن ناکام! انٹرنیٹ کنکشن چیک کریں۔ Error: {e}")

# ------------------------- اللہ کے 99 نام -------------------------
with st.sidebar:
    st.markdown("""<div class="sidebar">
    <div class="sidebar">
        <h3>❞ اللہ کے 99 نام ❝</h3>
        <ul>
            <li class="green-text">الرَّحْمَنُ - <span class="red-text">نہایت مہربان</span></li>
            <li class="green-text">الرَّحِيمُ - <span class="red-text">بہت رحم کرنے والا</span></li>
            <li class="green-text">الْمَلِكُ - <span class="red-text">بادشاہ</span></li>
            <li class="green-text">الْقُدُّوسُ - <span class="red-text">پاک</span></li>
            <li class="green-text">السَّلاَمُ - <span class="red-text">سلامتی دینے والا</span></li>
            <li class="green-text">الْمُؤْمِنُ - <span class="red-text">امن دینے والا</span></li>
            <li class="green-text">الْمُهَيْمِنُ - <span class="red-text">حفاظت کرنے والا</span></li>
            <li class="green-text">الْعَزِيزُ - <span class="red-text">غالب</span></li>
            <li class="green-text">الْجَبَّارُ - <span class="red-text">زبردست</span></li>
            <li class="green-text">الْمُتَكَبِّرُ - <span class="red-text">بڑائی والا</span></li>
            <li class="green-text">الْخَالِقُ - <span class="red-text">پیدا کرنے والا</span></li>
            <li class="green-text">الْبَارِئُ - <span class="red-text">درست بنانے والا</span></li>
            <li class="green-text">الْمُصَوِّرُ - <span class="red-text">صورت بنانے والا</span></li>
            <li class="green-text">الْغَفَّارُ - <span class="red-text">بخشنے والا</span></li>
            <li class="green-text">الْقَهَّارُ - <span class="red-text">سب پر غالب</span></li>
            <li class="green-text">الْوَهَّابُ - <span class="red-text">بہت عطا کرنے والا</span></li>
            <li class="green-text">الرَّزَّاقُ - <span class="red-text">رزق دینے والا</span></li>
            <li class="green-text">الْفَتَّاحُ - <span class="red-text">کھولنے والا</span></li>
            <li class="green-text">اَلْعَلِيْمُ - <span class="red-text">سب کچھ جاننے والا</span></li>
            <li class="green-text">الْقَابِضُ - <span class="red-text">قبضہ کرنے والا</span></li>
            <li class="green-text">الْبَاسِطُ - <span class="red-text">کشادگی دینے والا</span></li>
            <li class="green-text">الْخَافِضُ - <span class="red-text">پست کرنے والا</span></li>
            <li class="green-text">الرَّافِعُ - <span class="red-text">بلند کرنے والا</span></li>
            <li class="green-text">المُعِزُّ - <span class="red-text">عزت دینے والا</span></li>
            <li class="green-text">المُذِلُّ - <span class="red-text">ذلت دینے والا</span></li>
            <li class="green-text">السَّمِيعُ - <span class="red-text">سب کچھ سننے والا</span></li>
            <li class="green-text">الْبَصِيرُ - <span class="red-text">سب کچھ دیکھنے والا</span></li>
            <li class="green-text">الحَكَمُ - <span class="red-text">فیصلہ کرنے والا</span></li>
            <li class="green-text">العَدْلُ - <span class="red-text">انصاف کرنے والا</span></li>
            <li class="green-text">اللَّطِيفُ - <span class="red-text">مہربان</span></li>
            <li class="green-text">الخَبِيرُ - <span class="red-text">خبر رکھنے والا</span></li>
            <li class="green-text">الحَلِيمُ - <span class="red-text">بردبار</span></li>
            <li class="green-text">العَظِيمُ - <span class="red-text">عظمت والا</span></li>
            <li class="green-text">الغَفُورُ - <span class="red-text">بہت بخشنے والا</span></li>
            <li class="green-text">الشَّكُورُ - <span class="red-text">شکر قبول کرنے والا</span></li>
            <li class="green-text">العَلِيُّ - <span class="red-text">بلند</span></li>
            <li class="green-text">الكَبِيرُ - <span class="red-text">بڑا</span></li>
            <li class="green-text">الحَفِيظُ - <span class="red-text">حفاظت کرنے والا</span></li>
            <li class="green-text">المُقيِتُ - <span class="red-text">قوت دینے والا</span></li>
            <li class="green-text">الحسِيبُ - <span class="red-text">حساب لینے والا</span></li>
            <li class="green-text">الجَلِيلُ - <span class="red-text">جلال والا</span></li>
            <li class="green-text">الكَرِيمُ - <span class="red-text">کرم کرنے والا</span></li>
            <li class="green-text">الرَّقِيبُ - <span class="red-text">نگہبان</span></li>
            <li class="green-text">المُجِيبُ - <span class="red-text">قبول کرنے والا</span></li>
            <li class="green-text">الوَاسِعُ - <span class="red-text">کشادگی دینے والا</span></li>
            <li class="green-text">الحَكِيمُ - <span class="red-text">حکمت والا</span></li>
            <li class="green-text">الوَدُودُ - <span class="red-text">محبت کرنے والا</span></li>
            <li class="green-text">المَجِيدُ - <span class="red-text">بزرگی والا</span></li>
            <li class="green-text">البَاعِثُ - <span class="red-text">اٹھانے والا</span></li>
            <li class="green-text">الشَّهِيدُ - <span class="red-text">گواہ</span></li>
            <li class="green-text">الحَقُ - <span class="red-text">سچا</span></li>
            <li class="green-text">الوَكِيلُ - <span class="red-text">کارساز</span></li>
            <li class="green-text">القَوِيُ - <span class="red-text">طاقتور</span></li>
            <li class="green-text">المَتِينُ - <span class="red-text">مضبوط</span></li>
            <li class="green-text">الوَلِيُّ - <span class="red-text">دوست</span></li>
            <li class="green-text">الحَمِيدُ - <span class="red-text">تعریف کے لائق</span></li>
            <li class="green-text">المُحصِي - <span class="red-text">شمار کرنے والا</span></li>
            <li class="green-text">المُبدِئُ - <span class="red-text">پہلی بار پیدا کرنے والا</span></li>
            <li class="green-text">المُعِيدُ - <span class="red-text">دوبارہ پیدا کرنے والا</span></li>
            <li class="green-text">المُحيِي - <span class="red-text">زندگی دینے والا</span></li>
            <li class="green-text">المُمِيتُ - <span class="red-text">موت دینے والا</span></li>
            <li class="green-text">الحَيُ - <span class="red-text">زندہ</span></li>
            <li class="green-text">القَيُّومُ - <span class="red-text">قائم رہنے والا</span></li>
            <li class="green-text">الوَاجِدُ - <span class="red-text">پانے والا</span></li>
            <li class="green-text">المَاجِدُ - <span class="red-text">بزرگی والا</span></li>
            <li class="green-text">الوَاحِدُ - <span class="red-text">ایک</span></li>
            <li class="green-text">الصَّمَدُ - <span class="red-text">بے نیاز</span></li>
            <li class="green-text">القَادِرُ - <span class="red-text">قدرت والا</span></li>
            <li class="green-text">المُقتَدِرُ - <span class="red-text">قدرت والا</span></li>
            <li class="green-text">المُقَدِّمُ - <span class="red-text">آگے کرنے والا</span></li>
            <li class="green-text">المُؤَخِّرُ - <span class="red-text">پیچھے کرنے والا</span></li>
            <li class="green-text">الأوَّلُ - <span class="red-text">سب سے پہلا</span></li>
            <li class="green-text">الآخِرُ - <span class="red-text">سب کے بعد</span></li>
            <li class="green-text">الظَّاهِرُ - <span class="red-text">ظاہر</span></li>
            <li class="green-text">البَاطِنُ - <span class="red-text">پوشیدہ</span></li>
            <li class="green-text">الوَالِي - <span class="red-text">کارساز</span></li>
            <li class="green-text">المُتَعالِي - <span class="red-text">بلند</span></li>
            <li class="green-text">البَرُ - <span class="red-text">نیکی کرنے والا</span></li>
            <li class="green-text">التَّوَابُ - <span class="red-text">توبہ قبول کرنے والا</span></li>
            <li class="green-text">المُنتَقِمُ - <span class="red-text">بدلہ لینے والا</span></li>
            <li class="green-text">العَفُوُ - <span class="red-text">معاف کرنے والا</span></li>
            <li class="green-text">الرَّؤُوفُ - <span class="red-text">بہت مہربان</span></li>
            <li class="green-text">مَالِكُ ٱلْمُلْكُ - <span class="red-text">بادشاہوں کا بادشاہ</span></li>
            <li class="green-text">ذُوالْجَلاَلِ وَالإكْرَامِ - <span class="red-text">بزرگی اور عزت والا</span></li>
            <li class="green-text">المُقسِطُ - <span class="red-text">انصاف کرنے والا</span></li>
            <li class="green-text">الجَامِعُ - <span class="red-text">جمع کرنے والا</span></li>
            <li class="green-text">الغَنيُّ - <span class="red-text">بے نیاز</span></li>
            <li class="green-text">المُغنِي - <span class="red-text">غنی کرنے والا</span></li>
            <li class="green-text">اَلْمَانِعُ - <span class="red-text">روکنے والا</span></li>
            <li class="green-text">الضَّارَ - <span class="red-text">نقصان دینے والا</span></li>
            <li class="green-text">النَّافِعُ - <span class="red-text">نفع دینے والا</span></li>
            <li class="green-text">النُّورُ - <span class="red-text">روشنی</span></li>
            <li class="green-text">الهَادِي - <span class="red-text">ہدایت دینے والا</span></li>
            <li class="green-text">البَدِيعُ - <span class="red-text">نیا پیدا کرنے والا</span></li>
            <li class="green-text">البَاقِي - <span class="red-text">باقی رہنے والا</span></li>
            <li class="green-text">الوَارِثُ - <span class="red-text">سب کا وارث</span></li>
            <li class="green-text">الرَّشِيدُ - <span class="red-text">راستہ دکھانے والا</span></li>
            <li class="green-text">الصَّبُورُ - <span class="red-text">صبر کرنے والا</span></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ------------------------- اللہ کے 99 نام کا انتخاب -------------------------
with st.sidebar:
    st.markdown("### اللہ کے 99 نام کا انتخاب")
    names = [
        "الرَّحْمَنُ - نہایت مہربان", "الرَّحِيمُ - بہت رحم کرنے والا", "الْمَلِكُ - بادشاہ", "الْقُدُّوسُ - پاک",
        "السَّلاَمُ - سلامتی دینے والا", "الْمُؤْمِنُ - امن دینے والا", "الْمُهَيْمِنُ - حفاظت کرنے والا", "الْعَزِيزُ - غالب",
        "الْجَبَّارُ - زبردست", "الْمُتَكَبِّرُ - بڑائی والا", "الْخَالِقُ - پیدا کرنے والا", "الْبَارِئُ - درست بنانے والا",
        "الْمُصَوِّرُ - صورت بنانے والا", "الْغَفَّارُ - بخشنے والا", "الْقَهَّارُ - سب پر غالب", "الْوَهَّابُ - بہت عطا کرنے والا",
        "الرَّزَّاقُ - رزق دینے والا", "الْفَتَّاحُ - کھولنے والا", "اَلْعَلِيْمُ - سب کچھ جاننے والا", "الْقَابِضُ - قبضہ کرنے والا",
        "الْبَاسِطُ - کشادگی دینے والا", "الْخَافِضُ - پست کرنے والا", "الرَّافِعُ - بلند کرنے والا", "المُعِزُّ - عزت دینے والا",
        "المُذِلُّ - ذلت دینے والا", "السَّمِيعُ - سب کچھ سننے والا", "الْبَصِيرُ - سب کچھ دیکھنے والا", "الحَكَمُ - فیصلہ کرنے والا",
        "العَدْلُ - انصاف کرنے والا", "اللَّطِيفُ - مہربان", "الخَبِيرُ - خبر رکھنے والا", "الحَلِيمُ - بردبار",
        "العَظِيمُ - عظمت والا", "الغَفُورُ - بہت بخشنے والا", "الشَّكُورُ - شکر قبول کرنے والا", "العَلِيُّ - بلند",
        "الكَبِيرُ - بڑا", "الحَفِيظُ - حفاظت کرنے والا", "المُقيِتُ - قوت دینے والا", "الحسِيبُ - حساب لینے والا",
        "الجَلِيلُ - جلال والا", "الكَرِيمُ - کرم کرنے والا", "الرَّقِيبُ - نگہبان", "المُجِيبُ - قبول کرنے والا",
        "الوَاسِعُ - کشادگی دینے والا", "الحَكِيمُ - حکمت والا", "الوَدُودُ - محبت کرنے والا", "المَجِيدُ - بزرگی والا",
        "البَاعِثُ - اٹھانے والا", "الشَّهِيدُ - گواہ", "الحَقُ - سچا", "الوَكِيلُ - کارساز", "القَوِيُ - طاقتور",
        "المَتِينُ - مضبوط", "الوَلِيُّ - دوست", "الحَمِيدُ - تعریف کے لائق", "المُحصِي - شمار کرنے والا",
        "المُبدِئُ - پہلی بار پیدا کرنے والا", "المُعِيدُ - دوبارہ پیدا کرنے والا", "المُحيِي - زندگی دینے والا",
        "المُمِيتُ - موت دینے والا", "الحَيُ - زندہ", "القَيُّومُ - قائم رہنے والا", "الوَاجِدُ - پانے والا",
        "المَاجِدُ - بزرگی والا", "الوَاحِدُ - ایک", "الصَّمَدُ - بے نیاز", "القَادِرُ - قدرت والا", "المُقتَدِرُ - قدرت والا",
        "المُقَدِّمُ - آگے کرنے والا", "المُؤَخِّرُ - پیچھے کرنے والا", "الأوَّلُ - سب سے پہلا", "الآخِرُ - سب کے بعد",
        "الظَّاهِرُ - ظاہر", "البَاطِنُ - پوشیدہ", "الوَالِي - کارساز", "المُتَعالِي - بلند", "البَرُ - نیکی کرنے والا",
        "التَّوَابُ - توبہ قبول کرنے والا", "المُنتَقِمُ - بدلہ لینے والا", "العَفُوُ - معاف کرنے والا", "الرَّؤُوفُ - بہت مہربان",
        "مَالِكُ ٱلْمُلْكُ - بادشاہوں کا بادشاہ", "ذُوالْجَلاَلِ وَالإكْرَامِ - بزرگی اور عزت والا", "المُقسِطُ - انصاف کرنے والا",
        "الجَامِعُ - جمع کرنے والا", "الغَنيُّ - بے نیاز", "المُغنِي - غنی کرنے والا", "اَلْمَانِعُ - روکنے والا",
        "الضَّارَ - نقصان دینے والا", "النَّافِعُ - نفع دینے والا", "النُّورُ - روشنی", "الهَادِي - ہدایت دینے والا",
        "البَدِيعُ - نیا پیدا کرنے والا", "البَاقِي - باقی رہنے والا", "الوَارِثُ - سب کا وارث", "الرَّشِيدُ - راستہ دکھانے والا",
        "الصَّبُورُ - صبر کرنے والا"
    ]
    selected_name = st.selectbox("اللہ کے نام منتخب کریں:", names)
    st.write(f"آپ نے منتخب کیا: {selected_name}")

# ------------------------- فوٹر -------------------------
st.markdown("""<footer><p>© 2023 اسلامی کیلکولیٹر - زکوٰۃ و فطرہ | تمام حقوق محفوظ ہیں | تخلیق کردہ دلشر کھوسکیلی</p></footer>""", unsafe_allow_html=True)

# ------------------------- اللہ کے 99 نام کا بٹن -------------------------
if st.button("اللہ کے 99 نام"):
    st.markdown("""
    <div class="header">
        <h1>اللہ کے 99 نام</h1>
    </div>
    """, unsafe_allow_html=True)
