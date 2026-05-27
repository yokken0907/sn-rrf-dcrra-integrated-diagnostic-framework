# SPARC銀河回転曲線残差に対する claim-bounded 診断監査

**短縮名:** `SN-RRF / A10-TVC-RRF 診断監査`  
**Version:** `v2.0.1-claim-bounded-reader-guidance`  
**GitHub URL:** https://github.com/yokken0907/a10-tvc-rrf-galaxy-residual-diagnostic  
**過去版のリポジトリ・アーカイブ DOI:** https://doi.org/10.5281/zenodo.20224479

本リポジトリは、SPARC銀河回転曲線残差に対する claim-bounded diagnostic audit の統合論文および補助資料を収録するものです。

本プロジェクトは、A10/TVC由来の固定カーネル型残差応答診断から出発し、最終的に **SN-RRF: Scale-Normalized Residual-Response Family（スケール正規化残差応答ファミリー）** へ一般化されました。

## 読者向け注意

本パッケージは、診断・再現性確認・検証導線のためのリポジトリであり、完成した天体物理理論または宇宙論理論ではありません。

GitHub/Zenodo release により発行される Zenodo DOI は、論文そのものの査読済み article DOI ではなく、リポジトリの archived release DOI として扱ってください。

## 主結論

安全な統合結論は、「固定指数の唯一性」でも「暗黒物質代替理論」でもありません。

支持される診断的解釈は次の通りです。

> テストされたSPARC残差監査プロトコルの範囲内では、銀河回転曲線残差に、スケール正規化された単調飽和型の残差応答ファミリーと整合する証拠が見られる。無次元応答空間では、非病理クラスが中心流形の周辺に集まり、core-pathologyケースは pathology moat によって分離される。

## 主要チェックポイント

- 有効SPARC銀河数: 143。
- A10/TVC-RRF population relation: `rrf_log10_A` vs `v_max_kms`, Spearman rho = 0.873, permutation p = 0.001996。
- RAR相対診断: median Delta AIC(TVC-RRF - RAR-like) = -33.482; beats-RAR fraction = 0.867。
- Stage 23 manifold stability: 7/7 guards passed。
- Stage 26 curve-level destructive null controls: 5/5 guards passed; RRF beats best destructive null fraction = 0.916。
- Stage 30 kernel-continuum profile: 6/6 guards passed; best-n median = 2.25; best-n IQR = [1.5, 3.2545]。

## 主張境界

本リポジトリは以下を主張しません。

- 暗黒物質否定;
- Lambda-CDM置換;
- MOND/RARの反証・撃破;
- 弾丸銀河団の説明;
- 物理的TVC機構の証明;
- `n = 3.258993` が宇宙的・物理的に唯一の指数であること;
- ハッブルテンションの解決;
- 付属監査パッケージ外での独立観測的検証。

## 可視化ページ

以下をブラウザで開いてください。

```text
docs/project_visual_orientation/index.html
```

Python、外部API、インターネット接続は不要です。
