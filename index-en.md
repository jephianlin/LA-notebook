# Linear Algebra Notebook

[中文](index.html)

We use a notebook for doing computation, finding examples, or taking notes.  The idea of this *Linear Algebra Notebook* (LA-notebook) follows the same philosophy:  Whenever you encounter a new mathematical object, you should **play with it by doing some computation** , **run some examples to see its behaviors** (both examples or counterexamples!), and then **write down the notes just for yourself** .  This process is like conducting experiments in your mind, where your brain is analyzing the mathematical objects.

Take a awesome note for yourself, so that you can easily review what your brain has done in the future!


**To download the LA-notebook**：Visit [LA-notebook Releases](https://github.com/jephianlin/LA-notebook/releases) and download the latest version; newer versions are at the top, and you may click on "Source code (zip)" to download it.


## Usage

You need Jupyter with the SageMath kernel to open the files.  

You may choose one of the following two methods.

### 1. Install SageMath on your local machine (faster)

1. Follow the [Installation Guide](https://docs.google.com/document/d/1PnMK_GtNfKQYyBNZiub0PmHus8-VPBw-JeN52oVElHQ/edit?usp=sharing) to install SageMath
2. Download the LA-notebook through the link at the top of this page
3. Use the Jupyter Notebook, which was installed by SageMath, to open the `ipynb` files in the LA-notebook.

If you are not able to install SageMath on your machine, or you wish to use the browser version of it.  You may run the files through CoCalc as follows.


### 2. Run the files through [CoCalc](https://cocalc.com/app) (slower)

1. Register a [CoCalc](https://cocalc.com/app) account
2. Download the LA-notebook through the link at the top of this page
3. Login and then click on "Create New Project…" (you may enter any project name you like)
4. Click on "Upload" and select `LA-notebook.zip` you downloaded in Step 2.
5. Click on the `zip` to extract it.


## Table of contents
(The links below are read-only.  Follow the instructions above if you wish to run the code inside a file.)


### 1. Linear geometry

1. [Vector, length, and angle](html/101-Vector-length-angle.html)
2. [Subspaces in Rn](html/102-Subspaces-in-Rn.html)
3. [Column space of a matrix](html/103-Column-space-of-a-matrix.html)
4. [Row space of a matrix](html/104-Row-space-of-a-matrix.html)
5. [Projection and reflection](html/105-Projection-and-reflection.html)
6. [Affine subspaces in Rn](html/106-Affine-subspaces-in-Rn.html)
7. [Solution set of Ax = b](html/107-Solution-set-of-Ax-=-b.html)
8. [Row operations](html/108-Row-operations.html)
9. [Finding a particular solution](html/109-Finding-a-particular-solution.html)
10. [Finding the homogeneous solutions](html/110-Finding-the-homogeneous-solutions.html)
11. [Number of solutions](html/111-Number-of-solutions.html)
12. [Matrix inverse](html/112-Matrix-inverse.html)
13. [Elementary matrices](html/113-Elementary-matrices.html)
14. [Four fundamental subspaces](html/114-Four-fundamental-subspaces.html)

a. [Sage: Matrices and linear equations](html/1aa-Sage-Matrices-and-linear-equations.html)

```
Basic geometry & subspaces
101 --> 102 --> {103, 104} --> 105

Affine subspace & solutions
(102 -->)
106 --> 107 --> 108 --> {109, 110} --> 111

Topics
112, 113, 114, 10a
```


### 2. Linear spaces

1. [Linear independence](html/201-Linear-independence.html)
2. [Basis](html/202-Basis.html)
3. [Column space, left kernel, and their bases](html/203-Column-space-left-kernel-and-their-bases.html)
4. [Row space, kernel, and their bases](html/204-Row-space-kernel-and-their-bases.html)
5. [Basis exchange lemma](html/205-Basis-exchange-lemma.html)
6. [Dimension, expanding and shrinking lemmas](html/206-Dimension-expanding-and-shrinking-lemmas.html)
7. [Rank and nullity](html/207-Rank-and-nullity.html)
8. [Vector space](html/208-Vector-space.html)
9. [Subspaces in a vector space](html/209-Subspaces-in-a-vector-space.html)
10. [Common vector spaces](html/210-Common-vector-spaces.html)
11. [Constructing new subspaces](html/211-Constructing-new-subspaces.html)
12. [Constructing new vector spaces](html/212-Constructing-new-vector-spaces.html)
13. [Orthogonal geometry](html/213-Orthogonal-geometry.html)
14. [Gram–Schmidt orthogonalization](html/214-Gram--Schmidt-orthogonalization.html)
15. [Direct sum of orthogonal subspaces](html/215-Direct-sum-of-orthogonal-subspaces.html)

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


### 3. Linear functions

1. [Function basics](html/301-Function-basics.html)
2. [Linear function](html/302-Linear-function.html)
3. [Matrix as a linear function](html/303-Matrix-as-a-linear-function.html)
4. [Linear function as a matrix](html/304-Linear-function-as-a-matrix.html)
5. [Vector representation in Rn](html/305-Vector-representation-in-Rn.html)
6. [Vector representation in a vector space](html/306-Vector-representation-in-a-vector-space.html)
7. [Change of basis](html/307-Change-of-basis.html)
8. [Isomorphism](html/308-Isomorphism.html)
9. [Matrix representation in Rn](html/309-Matrix-representation-in-Rn.html)
10. [Matrix representation in a vector space](html/310-Matrix-representation-in-a-vector-space.html)
11. [Lagrange polynomials and Vandermonde matrix](html/311-Lagrange-polynomials-and-Vandermonde-matrix.html)
12. [Sylvester matrix and resultant](html/312-Sylvester-matrix-and-resultant.html)
13. [Understanding the spectral decomposition](html/313-Understanding-the-spectral-decomposition.html)
14. [Understanding the singular value decomposition](html/314-Understanding-the-singular-value-decomposition.html)
15. [Understanding the Jordan canonical form](html/315-Understanding-the-Jordan-canonical-form.html)

```
Linear function
301 --> 302 --> 303 -->304

Vector and matrix representations
305 --> 306 --> 307 --> 308 --> 309 --> 310

Topics
311, 312, 313, 314, 315
```


### 4. Determinant

1. [Determinant for small matrices](html/401-Determinant-for-small-matrices.html)
2. [Invertible matrix as the product of elementary matrices](html/402-Invertible-matrix-as-the-product-of-elementary-matrices.html)
3. [Elementary matrix acts on columns](html/403-Elementary-matrix-acts-on-columns.html)
4. [Elementary matrix acts on rows](html/404-Elementary-matrix-acts-on-rows.html)
5. [Definition of the determinant](html/405-Definition-of-the-determinant.html)
6. [Invertibility](html/406-Invertibility.html)
7. [Matrix multiplication and transpose](html/407-Matrix-multiplication-and-transpose.html)
8. [Block matrix](html/408-Block-matrix.html)
9. [Distributive law and Laplace expansion](html/409-Distributive-law-and-Laplace-expansion.html)
10. [Adjugate](html/410-Adjugate.html)
11. [Cramer's rule](html/411-Cramer's-rule.html)
12. [Permutation matrix](html/412-Permutation-matrix.html)
13. [Permutation expansion](html/413-Permutation-expansion.html)
14. [Interpretation through graph theory](html/414-Interpretation-through-graph-theory.html)
15. [Determinant is well-defined](html/415-Determinant-is-well-defined.html)

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


### 5. Diagonalization

1. [Find a good basis](html/501-Find-a-good-basis.html)
2. [Quadratic curve](html/502-Quadratic-curve.html)
3. [Recurrence relation](html/503-Recurrence-relation.html)
4. [Linear differential equation](html/504-Linear-differential-equation.html)
5. [Matrix exponential](html/505-Matrix-exponential.html)
6. [Characteristic polynomial](html/506-Characteristic-polynomial.html)
7. [Coefficients of the characteristic polynomial](html/507-Coefficients-of-the-characteristic-polynomial.html)
8. [Diagonalization](html/508-Diagonalization.html)
9. [Algebraic multiplicity and geometric multiplicity](html/509-Algebraic-multiplicity-and-geometric-multiplicity.html)
10. [Eigenspace](html/510-Eigenspace.html)
11. [Graph and characteristic polynomial](html/511-Graph-and-characteristic-polynomial.html)
12. [Cayley–Hamilton theorem](html/512-Cayley--Hamilton-theorem.html)
13. [Minimal polynomial](html/513-Minimal-polynomial.html)
14. [Jordan canonical form](html/514-Jordan-canonical-form.html)

a. [Python: NumPy and numerical linear algebra](html/5aa-Python-NumPy-and-numerical-linear-algebra.html)

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

1. [Reduction](html/601-Reduction.html)
2. [Schur triangulation](html/602-Schur-triangulation.html)
3. [Symmetric matrices and normal matrices](html/603-Symmetric-matrices-and-normal-matrices.html)
4. [Spectral decomposition](html/604-Spectral-decomposition.html)
5. [Singular value decomposition](html/605-Singular-value-decomposition.html)
6. [Understanding the principal component analysis](html/606-Understanding-the-principal-component-analysis.html)
7. [Inertia](html/607-Inertia.html)
8. [Positivity](html/608-Positivity.html)
9. [Rayleigh quotient](html/609-Rayleigh-quotient.html)
10. [Cauchy interlacing theorem](html/610-Cauchy-interlacing-theorem.html)
11. [Equitable partition](html/611-Equitable-partition.html)
12. [Covariance matrix](html/612-Covariance-matrix.html)
13. [Principal component analysis](html/613-Principal-component-analysis.html)
14. [Laplacian matrix](html/614-Laplacian-matrix.html)
15. [Spectral embedding and clustering](html/615-Spectral-embedding-and-clustering.html)

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


### Appendix

A. Index with translations