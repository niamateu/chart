import streamlit as st
import pandas as pd
import altair as alt

st.title('出荷変動チャート')

# 左側にアップロード用のサイドバーを設置
uploaded_file = st.sidebar.file_uploader("CSVファイルをアップロード", type=["csv"])

# csvファイルからデータフレームに変換
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="Shift-JIS")
    st.dataframe(df)

    # melt関数で各フルーツの数量、品名をそれぞれ一つの列にまとめる
    df_melted = df.melt(id_vars=["月"], var_name="フルーツ缶", value_name="数量(カートン)")

    # グラフの作成
    chart = alt.Chart(df_melted).mark_line(point=alt.OverlayMarkDef(filled=False, fill="white")).encode(
        x=alt.X("月:O", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("数量(カートン):Q", axis=alt.Axis(title="数量(カートン)")),
        color=alt.Color("フルーツ缶:N", scale=alt.Scale(domain=['みかん', 'もも', 'ぶどう'], range=['orange', 'pink', 'purple']))
        ).properties(
        title='月ごとの出荷変動グラフ')

    st.altair_chart(chart, use_container_width=True)
