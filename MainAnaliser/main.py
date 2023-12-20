import pandas as pd
import matplotlib.pyplot as plt


# Analise da porcentagem de utilização de CPU de todos os dados 
def PlotarTables(path1,path2,path3, title):
    tb_320 = pd.read_csv(path1)
    tb_480 = pd.read_csv(path2)
    tb_640 = pd.read_csv(path3)

    Tabela_inter = pd.concat([
        pd.Series(tb_320["cpu_porcentagem_pc"], name="320x240"),
        pd.Series(tb_480["cpu_porcentagem_pc"], name="480x360"),
        pd.Series(tb_640["cpu_porcentagem_pc"], name="640x480")],
        axis=1)

    Tabela_inter.plot()
    plt.title(title)
    plt.xlabel("Tempo (s)")
    plt.ylim(0,100)
    plt.ylabel("% Utilização de CPU")
    plt.legend()
    plt.show()

PlotarTables(
    'Alta Dinamicidade\AD_2min_AVI\AltaDinamicidade2min_avi_320x240.csv',
    'Alta Dinamicidade\AD_2min_AVI\AltaDinamicidade2min_avi_480x360.csv',
    'Alta Dinamicidade\AD_2min_AVI\AltaDinamicidade2min_avi_640x480.csv',
    "Alta Dinamicidade 2min AVI"
    )

PlotarTables(
    "Alta Dinamicidade\AD_2min_MOV\AltaDinamicidade2min_mov_320x240.csv",
    "Alta Dinamicidade\AD_2min_MOV\AltaDinamicidade2min_mov_480x360.csv",
    "Alta Dinamicidade\AD_2min_MOV\AltaDinamicidade2min_mov_640x480.csv",
    "Alta Dinamicidade 2min MOV"
)

PlotarTables(
    "Alta Dinamicidade\AD_10min_AVI\AltaDinamicidade10min_avi_320x240.csv",
    "Alta Dinamicidade\AD_10min_AVI\AltaDinamicidade10min_avi_480x360.csv",
    "Alta Dinamicidade\AD_10min_AVI\AltaDinamicidade10min_avi_640x480.csv",
    "Alta Dinamicidade 10min AVI"
)

PlotarTables(
    "Alta Dinamicidade\AD_10min_MOV\AltaDinamicidade10min_mov_320x240.csv",
    "Alta Dinamicidade\AD_10min_MOV\AltaDinamicidade10min_mov_480x360.csv",
    "Alta Dinamicidade\AD_10min_MOV\AltaDinamicidade10min_mov_640x480.csv",
    "Alta Dinamicidade 10min MOV"
)

PlotarTables(
    "Alta Dinamicidade\AD_10min_MP4\AltaDinamicidade10min_mp4_320x240.csv",
    "Alta Dinamicidade\AD_10min_MP4\AltaDinamicidade10min_mp4_480x360.csv",
    "Alta Dinamicidade\AD_10min_MP4\AltaDinamicidade10min_mp4_640x480.csv",
    "Alta Dinamicidade 10min MP4"
)

PlotarTables(
    "Alta Dinamicidade\AD_30s_AVI\AltaDinamicidade30s_avi_320x240.csv",
    "Alta Dinamicidade\AD_30s_AVI\AltaDinamicidade30s_avi_480x360.csv",
    "Alta Dinamicidade\AD_30s_AVI\AltaDinamicidade30s_avi_640x480.csv",
    "Alta Dinamicidade 30s AVI"
)

PlotarTables(
    "Alta Dinamicidade\AD_30s_MOV\AltaDinamicidade30s_mov_320x240.csv",
    "Alta Dinamicidade\AD_30s_MOV\AltaDinamicidade30s_mov_480x360.csv",
    "Alta Dinamicidade\AD_30s_MOV\AltaDinamicidade30s_mov_640x480.csv",
    "Alta Dinamicidade 30s MOV"
)

PlotarTables(
    'Baixa Dinamicidade\BD_2min_AVI\BaixaDinamicidade2min_avi_320x240.csv',
    'Baixa Dinamicidade\BD_2min_AVI\BaixaDinamicidade2min_avi_480x360.csv',
    'Baixa Dinamicidade\BD_2min_AVI\BaixaDinamicidade2min_avi_640x480.csv',
    "Baixa Dinamicidade 2min AVI"
    )

PlotarTables(
    "Baixa Dinamicidade\BD_2min_MOV\BaixaDinamicidade2min_mov_320x240.csv",
    "Baixa Dinamicidade\BD_2min_MOV\BaixaDinamicidade2min_mov_480x360.csv",
    "Baixa Dinamicidade\BD_2min_MOV\BaixaDinamicidade2min_mov_640x480.csv",
    "Baixa Dinamicidade 2min MOV"
)

PlotarTables(
    "Baixa Dinamicidade\BD_10min_AVI\BaixaDinamicidade10min_avi_320x240.csv",
    "Baixa Dinamicidade\BD_10min_AVI\BaixaDinamicidade10min_avi_480x360.csv",
    "Baixa Dinamicidade\BD_10min_AVI\BaixaDinamicidade10min_avi_640x480.csv",
    "Baixa Dinamicidade 10min AVI"
)

PlotarTables(
    "Baixa Dinamicidade\BD_10min_MOV\BaixaDinamicidade10min_mov_320x240.csv",
    "Baixa Dinamicidade\BD_10min_MOV\BaixaDinamicidade10min_mov_480x360.csv",
    "Baixa Dinamicidade\BD_10min_MOV\BaixaDinamicidade10min_mov_640x480.csv",
    "Baixa Dinamicidade 10min MOV"
)

PlotarTables(
    "Baixa Dinamicidade\BD_30s_AVI\BaixaDinamicidade30s_avi_320x240.csv",
    "Baixa Dinamicidade\BD_30s_AVI\BaixaDinamicidade30s_avi_480x360.csv",
    "Baixa Dinamicidade\BD_30s_AVI\BaixaDinamicidade30s_avi_640x480.csv",
    "Baixa Dinamicidade 30s AVI"
)

PlotarTables(
    "Baixa Dinamicidade\BD_30s_MOV\BaixaDinamicidade30s_mov_320x240.csv",
    "Baixa Dinamicidade\BD_30s_MOV\BaixaDinamicidade30s_mov_480x360.csv",
    "Baixa Dinamicidade\BD_30s_MOV\BaixaDinamicidade30s_mov_640x480.csv",
    "Baixa Dinamicidade 30s MOV"
)

