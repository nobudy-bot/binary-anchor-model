# バイナリー・アンカー・モデル (BAM) V2.0

[ [English](README.md) | **日本語** ]

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21759689.svg)](https://doi.org/10.5281/zenodo.21759689)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

本リポジトリは、澤田法光による論文  
**『The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure（バイナリー・アンカー：認知、記号ループ、およびシステム不全）』**  
の公式 Python シミュレーションコードを収録しています。

- **Zenodo プレプリント (V2.0.0 英語版):** [DOI: 10.5281/zenodo.21759689](https://doi.org/10.5281/zenodo.21759689)
- **コンセプト DOI (全バージョン共通):** [DOI: 10.5281/zenodo.21566423](https://doi.org/10.5281/zenodo.21566423)
- **ライセンス:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 🚀 実行方法

リポジトリをクローンし、最小限の依存パッケージをインストールします：

```bash
# 1. リポジトリのクローン
git clone https://github.com/nobudy-bot/binary-anchor-model.git
cd binary-anchor-model

# 2. 依存パッケージのインストール（numpy と matplotlib のみ）
pip install -r requirements.txt
```

### シミュレーション実行オプション:

- **オプション A: 微視的認知エンジン（V2.0 Core / 推奨）**  
  マスター方程式 $A_t = \mathrm{WTA}(V_t)$ の高解像度シミュレーションを実行します。**個人の脳内力学（扁桃体 vs 前頭前野）** に焦点を当てています（ゼロ依存・完全ヘッドレス対応）：
  ```bash
  python bam_engine.py
  ```

- **オプション B: 論文原本ベースラインスクリプト（V2.0）**  
  V2.0 プレプリント論文内の図表（Figure 4, 5）を生成したベースラインスクリプトです：
  ```bash
  python bam_simulator.py
  ```

- **オプション C: 巨視的社会動態シミュレーション（V1.0 Legacy）**  
  観測者間の相互作用・対話ループをシミュレートします。個人の微視的意思決定が、いかにして制度の化石化やシステム全体の臨界バーストを引き起こすかを可視化します（V1 論文 Figure 2 の再現）：
  ```bash
  python legacy_simulations/bam_v1_macro_dynamics.py
  ```

### 生成される出力図表:
- **V2.0 出力:** `bam_simulation_vulnerable.png`, `bam_comparison_eta.png`（個人の認知崩壊および回復プロセスの動態 / 第8章に対応）
- **V1.0 出力:** `bam_v1_simulation.png`（V1論文 Figure 2 の再現：適応的収束、再帰的振動、臨界バーストの3分岐シナリオ）

---

## 🧠 多層アーキテクチャ（Multiscale Architecture）

**バイナリー・アンカー・モデル（BAM）** は、異なるスケール（個人の脳からマクロ社会まで）に現れる同一の構造的トラップを記述するフラクタルな理論フレームワークです：

| スケール | モデル版 | 焦点 | 中核メカニズム |
| :--- | :--- | :--- | :--- |
| **微視的 (Brain)** | **V2.0 (Core)** | 個人の意思決定・認知崩壊 | WTAマスター方程式 / 扁桃体-前頭前野の拮抗 |
| **巨視的 (Society)** | **V1.0 (Legacy)** | 制度の飽和・硬直化 | 相互更新ループ / 化石化した知識（技術負債）の蓄積 |

- **システムA（生物学的アンカー / Biological Anchor）:** 身体的生存、クオリア、ホメオスタシス維持（扁桃体・内受容感覚系）。
- **システムB（社会的アンカー / Social Anchor）:** 記号体系、言語、制度規範、AIによる効率化（前頭前野・大脳皮質系）。

---

## 🛠 マスター方程式 (V2.0)

バージョン2.0では、意思決定と行動生成の頂点原理としてマスター方程式を定式化しています：

$$A_t = \mathrm{WTA}(V_t) \in \{0, 1\}$$
$$V_t = r_t \cdot m_t + (1 - r_t) \cdot m_{\mathrm{sys}, t}$$
$$\mathrm{WTA}(V_t) = \theta(V_t - T_{\mathrm{E}})$$

### 主要な数理定式化:
- **確率論的拡張 (Soft-WTA):** $A_t \sim \mathrm{Bernoulli}(\sigma(V_t - T_{\mathrm{E}}))$
- **躊躇エネルギー ($H_t$) ＆ 蓄積負荷 ($I_t$):** 計算破綻（Burst）を引き起こす二重トリガー機構。
- **扁桃体感受性・可塑性 ($\eta_{A0}$) の神経生物学的同定:** $\eta_{\mathrm{A}}(t) = \eta_{A0} \cdot (1 - \phi_t)$
- **回復時間 ($T_{\mathrm{recovery}}$) ＆ 暴力履歴 ($h_t$) による閾値修正:** Type 1 Burst からの回復経路と過去の強化履歴による発火閾値の変動。

---

## 📖 引用（Citation）

本モデル、概念、またはシミュレーションコードを研究で利用される場合は、以下のように引用してください：

```bibtex
@article{sawada2026binary,
  author      = {Sawada, Norimitsu},
  title       = {The Binary Anchor: Cognition, Symbolic Loops, and Systems Failure},
  journal     = {Zenodo Preprint},
  year        = {2026},
  month       = {aug},
  version     = {2.0.0},
  doi         = {10.5281/zenodo.21759689},
  url         = {https://doi.org/10.5281/zenodo.21759689}
}
```

---

## ライセンス

本プロジェクトは [クリエイティブ・コモンズ 表示 4.0 国際 ライセンス (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.ja) の下で公開されています。
