# 線性代數筆記本

通常我們會拿筆記本來做一些計算、看看例子、或是拿來寫筆記。  
線性代數筆記本的概念也是一樣的；  
當你學到一個新的概念﹐你應該要**動手算一算**、**觀察一些例子**（正面的或反正的！）、最後把寫下**屬於你自己的筆記**。  
這比較像是一個做實驗的過程﹐實驗執行者是是自己的大腦﹐而實驗對象是各個數學概念；  
好好地把這份實驗紀錄下來﹐讓你未來的大腦可以快速回顧自己曾經做過的事吧！  

**[下載整份筆記本](https://github.com/jephianlin/LA-notebook/releases/download/v0.1/LA-notebook.zip)**

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
101 --> 102 --> {103,104} --> 105

Affine subspace & solutions
(102 -->)
106 --> 107 --> 108 --> {109,110} --> 111

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
201 --> 202 --> {203,204} --> 205 --> 206 --> 207

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


### 5. 矩陣對角化


### 6. 對稱矩陣論


### 附錄

A. 索引暨翻譯對照表