# 線性代數筆記本

通常我們會拿筆記本來做一些計算、看看例子、或是拿來寫筆記。  
線性代數筆記本的概念也是一樣的；  
當你學到一個新的概念﹐你應該要**動手算一算**、**觀察一些例子**（正面的或反正的！）、最後把寫下**屬於你自己的筆記**。  
這比較像是一個做實驗的過程﹐實驗執行者是是自己的大腦﹐而實驗對象是各個數學概念；  
好好地把這份實驗紀錄下來﹐讓你未來的大腦可以快速回顧自己曾經做過的事吧！  


**下載整份筆記本**：請至 [LA-notebook Releases](https://github.com/jephianlin/LA-notebook/releases) 下載最新版本的原始碼；愈新的版本在愈上面，一般使用者請點 Source code (zip) 下載。

## 使用方式

這份講義必須用 Jupyter 開啟，配合 SageMath 核心才能執行其中的程式碼。  

以下提供兩種方式安裝 SageMath。

### 1. 在自己的機器上安裝 SageMath（速度較快）

1. 參考 [安裝指南](https://docs.google.com/document/d/1CXc1Aw8qA_jpN2mar-i7Ik3jB3fswXYkGp9ww4Rb_QU/edit?usp=sharing) 下載並安裝 SageMath
2. 用上方連結下載整份筆記本
3. 利用 SageMath 安裝好的 Jupyter Notebook 開啟課程檔案中的 `ipynb` 檔

若自己的電腦無法安裝，或是希望使用網頁版
可以依照以下的步驟在 CoCalc 上開啟

### 2. 在 [CoCalc](https://cocalc.com/app) 上開啟講義（速度會比較慢）

1. 申請 [CoCalc](https://cocalc.com/app) 帳號
2. 用上方連結下載整份筆記本
3. 登入後點擊 Create New Project…（輸入自己想要的名稱）
4. 點 Upload 上傳第二步下載的 `LA-notebook.zip`
5. 點擊上傳的 `zip` 檔解壓縮


## 目錄
（各小節的連結僅為網頁版，若要執行其中程式碼請參考上方的使用方式。）

### 1. 線性幾何

1. [向量、長度、角度](html/101-Vector-length-angle.html)
2. [Rn 中的子空間](html/102-Subspaces-in-Rn.html)
3. [矩陣的行空間](html/103-Column-space-of-a-matrix.html)
4. [矩陣的列空間](html/104-Row-space-of-a-matrix.html)
5. [投影與鏡射](html/105-Projection-and-reflection.html)
6. [Rn 中的仿射子空間](html/106-Affine-subspaces-in-Rn.html)
7. [Ax = b 的解集合](html/107-Solution-set-of-Ax-=-b.html)
8. [列運算](html/108-Row-operations.html)
9. [特解](html/109-Finding-a-particular-solution.html)
10. [零解](html/110-Finding-the-homogeneous-solutions.html)
11. [解的個數](html/111-Number-of-solutions.html)
12. [反矩陣](html/112-Matrix-inverse.html)
13. [基本矩陣](html/113-Elementary-matrices.html)
14. [四大基礎子空間](html/114-Four-fundamental-subspaces.html)

a. [Sage: 矩陣、線性方程組](html/1aa-Sage-Matrices-and-linear-equations.html)

```
Basic geometry & subspaces
101 --> 102 --> {103, 104} --> 105

Affine subspace & solutions
(102 -->)
106 --> 107 --> 108 --> {109, 110} --> 111

Topics
112, 113, 114, 10a
```


### 2. 線性空間

1. [線性獨立](html/201-Linear-independence.html)
2. [基底](html/202-Basis.html)
3. [行空間、左零解空間、及其基底](html/203-Column-space-left-kernel-and-their-bases.html)
4. [列空間、零解空間、及其基底](html/204-Row-space-kernel-and-their-bases.html)
5. [基底交換法則](html/205-Basis-exchange-lemma.html)
6. [維度、擴充與縮限法則](html/206-Dimension-expanding-and-shrinking-lemmas.html)
7. [秩與核數](html/207-Rank-and-nullity.html)
8. [向量空間](html/208-Vector-space.html)
9. [向量子空間](html/209-Subspaces-in-a-vector-space.html)
10. [常見的向量空間](html/210-Common-vector-spaces.html)
11. [建構新的子空間](html/211-Constructing-new-subspaces.html)
12. [建構新的向量空間](html/212-Constructing-new-vector-spaces.html)
13. [垂直幾何](html/213-Orthogonal-geometry.html)
14. [基底正交化](html/214-Gram--Schmidt-orthogonalization.html)
15. [垂直子空間](html/215-Direct-sum-of-orthogonal-subspaces.html)

```
Spaces in Rn
201 --> 202 --> {203, 204} --> 205 --> 206 --> 207

Abstract spaces
208 --> 209 --> 210

Operations of spaces
211 -->  212

Inner product space
213 --> 214 --> 215
```


### 3. 線性函數

1. [函數基本概念](html/301-Function-basics.html)
2. [線性函數](html/302-Linear-function.html)
3. [將矩陣視為線性函數](html/303-Matrix-as-a-linear-function.html)
4. [將線性函數化為矩陣](html/304-Linear-function-as-a-matrix.html)
5. [Rn 中的向量表示法](html/305-Vector-representation-in-Rn.html)
6. [向量空間中的向量表示法](html/306-Vector-representation-in-a-vector-space.html)
7. [基底轉換](html/307-Change-of-basis.html)
8. [同構](html/308-Isomorphism.html)
9. [Rn 中的矩陣表示法](html/309-Matrix-representation-in-Rn.html)
10. [向量空間中的矩陣表示法](html/310-Matrix-representation-in-a-vector-space.html)
11. [拉格朗日多項式、凡德孟矩陣](html/311-Lagrange-polynomials-and-Vandermonde-matrix.html)
12. [西爾維斯特矩陣、結式](html/312-Sylvester-matrix-and-resultant.html)
13. [體驗譜分解](html/313-Understanding-the-spectral-decomposition.html)
14. [體驗奇異值分解](html/314-Understanding-the-singular-value-decomposition.html)
15. [體驗喬丹標準型](html/315-Understanding-the-Jordan-canonical-form.html)

```
Linear function
301 --> 302 --> 303 -->304

Vector and matrix representations
305 --> 306 --> 307 --> 308 --> 309 --> 310

Topics
311, 312, 313, 314, 315
```


### 4. 行列式值

1. [小型矩陣的行列式值](html/401-Determinant-for-small-matrices.html)
2. [將可逆矩陣展開為基本矩陣的乘積](html/402-Invertible-matrix-as-the-product-of-elementary-matrices.html)
3. [基本矩陣與行超平行體](html/403-Elementary-matrix-acts-on-columns.html)
4. [基本矩陣與列超平行體](html/404-Elementary-matrix-acts-on-rows.html)
5. [行列式值的定義](html/405-Definition-of-the-determinant.html)
6. [判斷矩陣是否可逆](html/406-Invertibility.html)
7. [矩陣乘積與轉置](html/407-Matrix-multiplication-and-transpose.html)
8. [區塊矩陣](html/408-Block-matrix.html)
9. [分配律、拉普拉斯展開](html/409-Distributive-law-and-Laplace-expansion.html)
10. [伴隨矩陣](html/410-Adjugate.html)
11. [克拉瑪公式](html/411-Cramer's-rule.html)
12. [排列矩陣](html/412-Permutation-matrix.html)
13. [排列展開式](html/413-Permutation-expansion.html)
14. [代數圖論觀點](html/414-Interpretation-through-graph-theory.html)
15. [行列式值是定義完善的](html/415-Determinant-is-well-defined.html)

```
Determinant for small matrices
401

Geometric interpretations
402 --> {403, 404}

Definition and properties
405 --> {406, 407, 408} --> 409

Adjugate
410 --> 411

Permutation expansion
412 --> 413 --> {414, 415}
```


### 5. 矩陣對角化

_內容尚未完成_

1. [找一組好基底]()
2. [二次曲線]()
3. [遞迴關係式]()
4. [線性微分方程]()
5. [矩陣指數]()
6. [特徵多項式]()
7. [特徵多項式係數]()
8. [矩陣對角化]()
9. [代數重數與幾何重數]()
10. [特徵空間]()
11. [圖與特徵方程式]()
12. [凱力–漢米頓定理]()
13. [最小多項式]()
14. [喬丹標準型]()

a. [Python: NumPy]()

```
Good basis
501 --> {502, 503, 504, 505}

Characteristic polynomial
506 --> 507

Diagonalization
508 --> 509 --> 510

Topics
511, 512, 513, 514, 50a

```


### 6. 對稱矩陣論

_內容尚未完成_

1. [化簡]()
2. [薛爾上三角化]()
3. [對稱矩陣與正規矩陣]()
4. [譜分解]()
5. [奇異值分解]()
6. [體驗主成份分析]()
7. [慣性]()
8. [正定與半正定矩陣]()
9. [瑞利商]()
10. [柯西交錯定理]()
11. [等量分割]()
12. [變異數]()
13. [主成份分析]()
14. [拉普拉斯矩陣]()
15. [譜聚類與群數]()

```
Schur triangulation
601 --> 602 --> 603 --> 604 --> 605 --> 606

Symmetric matrix
607 --> 608 --> 609 --> 610 --> 611

Statistics
612 --> 613

Laplacian matrix
614 --> 615
```


### 附錄

A. 索引暨翻譯對照表