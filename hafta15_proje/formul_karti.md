# Formül kartı (sınavda verilir)

**Sınıflandırma:** Doğruluk $=\dfrac{TP+TN}{N}$, Kesinlik $=\dfrac{TP}{TP+FP}$, Duyarlılık $=\dfrac{TP}{TP+FN}$,
$F_1=\dfrac{2PR}{P+R}$, FPR $=\dfrac{FP}{FP+TN}$.

**Regresyon:** MAE $=\frac1n\sum|y_i-\hat y_i|$, RMSE $=\sqrt{\frac1n\sum(y_i-\hat y_i)^2}$, $R^2=1-\dfrac{\sum(y_i-\hat y_i)^2}{\sum(y_i-\bar y)^2}$.

**Lojistik:** $p=\sigma(z)=\dfrac{1}{1+e^{-z}}$, $z=\mathbf w^\top\mathbf x+b$; BCE $=-\frac1n\sum[y\ln p+(1-y)\ln(1-p)]$.

**Kümeleme:** inertia $=\sum_k\sum_{i\in C_k}\|x_i-\mu_k\|^2$; silüet $s_i=\dfrac{b_i-a_i}{\max(a_i,b_i)}$.

**PCA:** açıklanan varyans oranı $=\lambda_j/\sum_k\lambda_k$.

**Kayma:** PSI $=\sum_b (p_b^{\text{yeni}}-p_b^{\text{ref}})\ln\dfrac{p_b^{\text{yeni}}}{p_b^{\text{ref}}}$; $<0{,}1$ kararlı, $0{,}1$–$0{,}25$ izle, $>0{,}25$ uyarı.

**Bellek:** $n\times n$ float32 matris $=4n^2$ bayt; LLM ağırlığı $\approx$ parametre $\times$ bayt/parametre (fp16: 2, Q4: 0,5).

**Maliyet:** VM aylık $=$ saatlik $\times 730$; sunucusuz $=$ çağrı$\times$birim $+$ GB-s$\times$birim.

**Gecikme:** throughput $=$ istek / süre; p95 $=$ sıralı gecikmelerin %95'inci yüzdeliği.
