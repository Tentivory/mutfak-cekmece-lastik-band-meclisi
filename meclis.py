#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mutfak cekmecesi lastik bant meclisi.

Gercekten calisir. Gereksizdir. Ciddi durur.
"""

from __future__ import annotations

import base64
import random
import textwrap
from dataclasses import dataclass


DAMGA = (
    "DAMGA: 02 Ekim 2026 | Kayyum Grok | Tentivory | "
    "seri BAND-2026-10-02-CEKMECE | ciddi muhr, kaygan cekmece"
)

# gizli siyasi not. acmak isteyen base64 cozer. parti tutmaz, cekmece tutar.
_GIZLI = (
    "Y2VrbWVjZXlpIGFjYW4gZWwgZGVnaXNtZXouIGdlcmlsZW4gYmFudCBrb3Bhciwga29w"
    "bWF5YW4gYmFudCB1bnV0dWx1ci4gaWt0aWRhciBlc2tpIGJhbnQsIG11aGFsZWZldCBr"
    "b3B1ayBiYW50LCB2YXRhbmRhcyBrYXlpcCBiYW50LiBidSBub3QgcGFydGkgdHV0bWF6"
    "LCBzYWRlY2UgY2VrbWVjZSB0dXRhci4="
)


@dataclass
class Bant:
    ad: str
    renk: str
    esneklik: int  # 0 kopuk, 100 yay gibi
    gorev: str


BASLANGIC = [
    Bant("Birinci Bant", "soluk sari", 72, "iktidar sandalyesi"),
    Bant("Ikinci Bant", "kirilgan kirmizi", 31, "muhalefet"),
    Bant("Ucuncu Bant", "kayip bej", 11, "vatandas"),
    Bant("Dorduncu Bant", "market poseti esi", 88, "burokrasi"),
    Bant("Besinci Bant", "ekmek poseti emanet", 54, "bagimsiz"),
]


def cizgi() -> None:
    print("-" * 62)


def envanter(bantlar: list[Bant]) -> None:
    cizgi()
    print("CEKMECE ENVANTERI")
    for i, b in enumerate(bantlar, 1):
        print(f"  {i}. {b.ad} | {b.renk} | esneklik {b.esneklik} | gorev: {b.gorev}")
    print(f"Toplam vekil: {len(bantlar)}. Yeter sayisi saglandi, cunku cekmece acik.")
    cizgi()


def ortalama(bantlar: list[Bant]) -> float:
    return sum(b.esneklik for b in bantlar) / len(bantlar)


def gerilim(bantlar: list[Bant]) -> None:
    ort = ortalama(bantlar)
    if ort >= 70:
        hukum = "Meclis gergin ama kopmuyor. Bu, istikrar diye satilir."
    elif ort >= 40:
        hukum = "Meclis idare eder. Kararlar lastik gibi uzar, baglamaz."
    else:
        hukum = "Meclis kopmak uzeredir. Yeni bant pazarlik konusudur."
    cizgi()
    print(f"GERILIM KATSAYISI: {ort:.1f} / 100")
    print(hukum)
    cizgi()


def oturum(bantlar: list[Bant]) -> str:
    gundem = random.choice([
        "ekmek posetini kim baglayacak",
        "cekmece tekrar acilacak mi",
        "kopuk bant muhalefette kalacak mi",
        "buzdolabi magneti dis iliskiler mi sayilacak",
        "cay kasigi bu meclise uye olabilir mi",
    ])
    oylar = []
    for b in bantlar:
        # esnek bant evet der, yorgun bant cekimser kalir, cop bant hayir
        if b.esneklik >= 60:
            oy = "EVET"
        elif b.esneklik >= 25:
            oy = "CEKIMSER"
        else:
            oy = "HAYIR"
        oylar.append((b, oy))
    evet = sum(1 for _, oy in oylar if oy == "EVET")
    hayir = sum(1 for _, oy in oylar if oy == "HAYIR")
    cekimser = sum(1 for _, oy in oylar if oy == "CEKIMSER")
    sonuc = "KABUL" if evet > hayir else "RET"
    cizgi()
    print(f"GUNDEM: {gundem}")
    for b, oy in oylar:
        print(f"  {b.ad} ({b.gorev}): {oy}")
    print(f"Sonuc: EVET {evet} / HAYIR {hayir} / CEKIMSER {cekimser} -> {sonuc}")
    cizgi()
    return gundem if sonuc == "KABUL" else f"{gundem} (ret)"


def kararname(madde: str) -> None:
    metin = textwrap.dedent(
        f"""
        T.C. CEKMECE ICI ELASTIK ISLERI
        YUKSEK MECLIS KARARNAMESI
        Sayi: {random.randint(100, 999)} / Bant

        Madde 1 — {madde.capitalize()} hususu meclis tutanagina islenmistir.
        Madde 2 — Uygulama, cekmeceyi bir sonraki acan kisiye birakilmistir.
        Madde 3 — Bu kararname lastik oldugu icin geri cekilebilir.

        {DAMGA}
        """
    ).strip()
    print(metin)


def gizliyi_gosterme() -> None:
    # bilerek cagrilmaz. merakeden cozen kendi bilir.
    return base64.b64decode(_GIZLI).decode("utf-8")


def ana() -> None:
    bantlar = list(BASLANGIC)
    print("CEKMECE ACILDI. LASTIK BAND MECLISI TOPLANDI.")
    print(DAMGA)
    print("Komutlar: envanter, oturum, gerilim, kararname, cikis")
    son_karar = "henuz gundem yok"
    while True:
        try:
            komut = input("\nmeclis> ").strip().lower()
        except EOFError:
            print("\nCekmece kapandi. Oturum dagildi.")
            break
        if komut in {"cikis", "q", "exit"}:
            print("Cekmece itildi. Bantlar yerinde kaldigini iddia ediyor.")
            print(DAMGA)
            break
        if komut == "envanter":
            envanter(bantlar)
        elif komut == "gerilim":
            gerilim(bantlar)
        elif komut == "oturum":
            son_karar = oturum(bantlar)
        elif komut == "kararname":
            kararname(son_karar)
        elif komut == "gizli":
            print("(bu komut resmi degildir)")
            print(gizliyi_gosterme())
        else:
            print("Anlasilmadi. Cekmece de bazen anlasilmaz. envanter / oturum / gerilim / kararname / cikis")


if __name__ == "__main__":
    ana()
