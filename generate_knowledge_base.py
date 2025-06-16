import os
import shutil
import config

# Ensure knowledge base directory exists
if not os.path.exists("knowledge_base"):
    os.makedirs("knowledge_base")

# Sample content for different mathematics topics
topic_content = {
    "Trigonometry": """
# Trigonometry: Fundamentals and Identities

## Basic Definitions

Trigonometric functions are defined for a right-angled triangle as follows:

- $\sin \theta = \frac{\text{Opposite}}{\text{Hypotenuse}}$
- $\cos \theta = \frac{\text{Adjacent}}{\text{Hypotenuse}}$
- $\tan \theta = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{\sin \theta}{\cos \theta}$
- $\cot \theta = \frac{\text{Adjacent}}{\text{Opposite}} = \frac{\cos \theta}{\sin \theta}$
- $\sec \theta = \frac{\text{Hypotenuse}}{\text{Adjacent}} = \frac{1}{\cos \theta}$
- $\csc \theta = \frac{\text{Hypotenuse}}{\text{Opposite}} = \frac{1}{\sin \theta}$

## Fundamental Identities

1. $\sin^2 \theta + \cos^2 \theta = 1$
2. $1 + \tan^2 \theta = \sec^2 \theta$
3. $1 + \cot^2 \theta = \csc^2 \theta$
4. $\sin(\theta + 2\pi) = \sin \theta$
5. $\cos(\theta + 2\pi) = \cos \theta$

## Addition and Subtraction Formulas

1. $\sin(A + B) = \sin A \cos B + \cos A \sin B$
2. $\sin(A - B) = \sin A \cos B - \cos A \sin B$
3. $\cos(A + B) = \cos A \cos B - \sin A \sin B$
4. $\cos(A - B) = \cos A \cos B + \sin A \sin B$
5. $\tan(A + B) = \frac{\tan A + \tan B}{1 - \tan A \tan B}$
6. $\tan(A - B) = \frac{\tan A - \tan B}{1 + \tan A \tan B}$

## Double Angle Formulas

1. $\sin 2A = 2 \sin A \cos A$
2. $\cos 2A = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A$
3. $\tan 2A = \frac{2 \tan A}{1 - \tan^2 A}$

## Triple Angle Formulas

1. $\sin 3A = 3\sin A - 4\sin^3 A$
2. $\cos 3A = 4\cos^3 A - 3\cos A$

## Half Angle Formulas

1. $\sin^2 \frac{A}{2} = \frac{1 - \cos A}{2}$
2. $\cos^2 \frac{A}{2} = \frac{1 + \cos A}{2}$
3. $\tan \frac{A}{2} = \frac{1 - \cos A}{\sin A} = \frac{\sin A}{1 + \cos A}$

## Product to Sum Formulas

1. $\sin A \sin B = \frac{\cos(A - B) - \cos(A + B)}{2}$
2. $\cos A \cos B = \frac{\cos(A - B) + \cos(A + B)}{2}$
3. $\sin A \cos B = \frac{\sin(A + B) + \sin(A - B)}{2}$

## Sum to Product Formulas

1. $\sin A + \sin B = 2 \sin \frac{A + B}{2} \cos \frac{A - B}{2}$
2. $\sin A - \sin B = 2 \cos \frac{A + B}{2} \sin \frac{A - B}{2}$
3. $\cos A + \cos B = 2 \cos \frac{A + B}{2} \cos \frac{A - B}{2}$
4. $\cos A - \cos B = -2 \sin \frac{A + B}{2} \sin \frac{A - B}{2}$

## Values of Trigonometric Functions at Special Angles

| Angle | $\sin$ | $\cos$ | $\tan$ |
|-------|--------|--------|--------|
| $0°$  | $0$    | $1$    | $0$    |
| $30°$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{3}}$ |
| $45°$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{\sqrt{2}}$ | $1$ |
| $60°$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |
| $90°$ | $1$    | $0$    | Undefined |

## Inverse Trigonometric Functions

1. $\sin^{-1}(\sin x) = x$ for $-\frac{\pi}{2} \leq x \leq \frac{\pi}{2}$
2. $\cos^{-1}(\cos x) = x$ for $0 \leq x \leq \pi$
3. $\tan^{-1}(\tan x) = x$ for $-\frac{\pi}{2} < x < \frac{\pi}{2}$

## Common JEE Problems

### Problem 1: Proving Identities

Prove that $\frac{\sin A + \sin B}{\cos A + \cos B} = \tan \frac{A + B}{2}$

Solution:
- Using sum to product formulas:
  $\sin A + \sin B = 2 \sin \frac{A + B}{2} \cos \frac{A - B}{2}$
  $\cos A + \cos B = 2 \cos \frac{A + B}{2} \cos \frac{A - B}{2}$
- Dividing these equations:
  $\frac{\sin A + \sin B}{\cos A + \cos B} = \frac{2 \sin \frac{A + B}{2} \cos \frac{A - B}{2}}{2 \cos \frac{A + B}{2} \cos \frac{A - B}{2}} = \frac{\sin \frac{A + B}{2}}{\cos \frac{A + B}{2}} = \tan \frac{A + B}{2}$

### Problem 2: Solving Trigonometric Equations

Solve the equation $2\sin^2 x - \sin x - 1 = 0$ for $0 \leq x \leq 2\pi$

Solution:
- Let $t = \sin x$, then the equation becomes $2t^2 - t - 1 = 0$
- Using the quadratic formula: $t = \frac{1 \pm \sqrt{1 + 8}}{4} = \frac{1 \pm 3}{4}$
- So $t = 1$ or $t = -\frac{1}{2}$
- For $t = 1$: $\sin x = 1$ gives $x = \frac{\pi}{2} + 2n\pi$ or $x = \frac{\pi}{2}$ for $0 \leq x \leq 2\pi$
- For $t = -\frac{1}{2}$: $\sin x = -\frac{1}{2}$ gives $x = \frac{7\pi}{6} + 2n\pi$ or $x = \frac{11\pi}{6} + 2n\pi$
- For $0 \leq x \leq 2\pi$, the solutions are $x = \frac{\pi}{2}, \frac{7\pi}{6}, \frac{11\pi}{6}$

### Problem 3: Finding Maximum/Minimum Values

Find the maximum value of $\sin x + \cos x$ for $0 \leq x \leq 2\pi$

Solution:
- Let $f(x) = \sin x + \cos x$
- We can rewrite this as $f(x) = \sqrt{2} \sin(x + \frac{\pi}{4})$
- Since $-1 \leq \sin(x + \frac{\pi}{4}) \leq 1$, we have $-\sqrt{2} \leq f(x) \leq \sqrt{2}$
- Therefore, the maximum value is $\sqrt{2}$, occurring at $x = \frac{\pi}{4} + 2n\pi$
""",
    
    "Vectors": """
# Vectors: Fundamentals and Operations

## Basic Definitions

A vector is a quantity that has both magnitude and direction. In three-dimensional space, a vector can be represented as:

$$\vec{a} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$$

where $\vec{i}$, $\vec{j}$, and $\vec{k}$ are unit vectors along the x, y, and z axes, respectively.

## Vector Operations

### 1. Addition and Subtraction

If $\vec{a} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$ and $\vec{b} = b_1\vec{i} + b_2\vec{j} + b_3\vec{k}$, then:

- $\vec{a} + \vec{b} = (a_1 + b_1)\vec{i} + (a_2 + b_2)\vec{j} + (a_3 + b_3)\vec{k}$
- $\vec{a} - \vec{b} = (a_1 - b_1)\vec{i} + (a_2 - b_2)\vec{j} + (a_3 - b_3)\vec{k}$

### 2. Scalar Multiplication

If $\vec{a} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$ and $\lambda$ is a scalar, then:

$$\lambda\vec{a} = \lambda a_1\vec{i} + \lambda a_2\vec{j} + \lambda a_3\vec{k}$$

### 3. Magnitude (Length) of a Vector

The magnitude of a vector $\vec{a} = a_1\vec{i} + a_2\vec{j} + a_3\vec{k}$ is given by:

$$|\vec{a}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$$

### 4. Unit Vector

A unit vector in the direction of $\vec{a}$ is given by:

$$\hat{a} = \frac{\vec{a}}{|\vec{a}|}$$

### 5. Dot Product (Scalar Product)

The dot product of two vectors $\vec{a}$ and $\vec{b}$ is defined as:

$$\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1b_1 + a_2b_2 + a_3b_3$$

where $\theta$ is the angle between the vectors.

Properties of dot product:
- $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$ (commutative)
- $(\lambda\vec{a}) \cdot \vec{b} = \lambda(\vec{a} \cdot \vec{b})$ (scalar multiplication)
- $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$ (distributive)
- $\vec{a} \cdot \vec{a} = |\vec{a}|^2$
- If $\vec{a} \cdot \vec{b} = 0$, then $\vec{a}$ and $\vec{b}$ are perpendicular (orthogonal)

### 6. Cross Product (Vector Product)

The cross product of two vectors $\vec{a}$ and $\vec{b}$ is defined as:

$$\vec{a} \times \vec{b} = |\vec{a}||\vec{b}|\sin\theta\, \hat{n}$$

where $\theta$ is the angle between the vectors and $\hat{n}$ is a unit vector perpendicular to both $\vec{a}$ and $\vec{b}$ in the right-hand rule direction.

In component form:

$$\vec{a} \times \vec{b} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix} = (a_2b_3 - a_3b_2)\vec{i} + (a_3b_1 - a_1b_3)\vec{j} + (a_1b_2 - a_2b_1)\vec{k}$$

Properties of cross product:
- $\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$ (anti-commutative)
- $(\lambda\vec{a}) \times \vec{b} = \lambda(\vec{a} \times \vec{b})$ (scalar multiplication)
- $\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}$ (distributive)
- $\vec{a} \times \vec{a} = \vec{0}$
- The magnitude of the cross product $|\vec{a} \times \vec{b}|$ equals the area of the parallelogram formed by $\vec{a}$ and $\vec{b}$

### 7. Scalar Triple Product

The scalar triple product of three vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$ is defined as:

$$\vec{a} \cdot (\vec{b} \times \vec{c}) = \begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix}$$

Properties of scalar triple product:
- $\vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{b} \cdot (\vec{c} \times \vec{a}) = \vec{c} \cdot (\vec{a} \times \vec{b})$ (cyclic permutation)
- The absolute value of the scalar triple product $|\vec{a} \cdot (\vec{b} \times \vec{c})|$ equals the volume of the parallelepiped formed by $\vec{a}$, $\vec{b}$, and $\vec{c}$
- If the scalar triple product is zero, then the three vectors are coplanar

### 8. Vector Triple Product

The vector triple product is defined as:

$$\vec{a} \times (\vec{b} \times \vec{c}) = \vec{b}(\vec{a} \cdot \vec{c}) - \vec{c}(\vec{a} \cdot \vec{b})$$

## Vector Equations of Lines and Planes

### 1. Vector Equation of a Line

A line passing through a point with position vector $\vec{a}$ and parallel to a vector $\vec{b}$ can be represented as:

$$\vec{r} = \vec{a} + t\vec{b}$$

where $t$ is a parameter and $\vec{r}$ is the position vector of any point on the line.

### 2. Vector Equation of a Plane

A plane passing through a point with position vector $\vec{a}$ and perpendicular to a vector $\vec{n}$ can be represented as:

$$\vec{n} \cdot (\vec{r} - \vec{a}) = 0$$

where $\vec{r}$ is the position vector of any point on the plane.

## Common JEE Problems

### Problem 1: Finding the Angle Between Two Vectors

Find the angle between the vectors $\vec{a} = 2\vec{i} + 3\vec{j} - \vec{k}$ and $\vec{b} = \vec{i} - 2\vec{j} + 2\vec{k}$.

Solution:
- $\vec{a} \cdot \vec{b} = 2 \cdot 1 + 3 \cdot (-2) + (-1) \cdot 2 = 2 - 6 - 2 = -6$
- $|\vec{a}| = \sqrt{2^2 + 3^2 + (-1)^2} = \sqrt{4 + 9 + 1} = \sqrt{14}$
- $|\vec{b}| = \sqrt{1^2 + (-2)^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$
- $\cos\theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|} = \frac{-6}{\sqrt{14} \cdot 3} = \frac{-6}{3\sqrt{14}} = \frac{-2}{\sqrt{14}}$
- $\theta = \cos^{-1}(\frac{-2}{\sqrt{14}})$

### Problem 2: Finding the Area of a Triangle

Find the area of the triangle formed by the points $A(1, 2, 3)$, $B(2, 3, 1)$, and $C(3, 1, 2)$.

Solution:
- $\vec{AB} = \vec{B} - \vec{A} = (2, 3, 1) - (1, 2, 3) = (1, 1, -2)$
- $\vec{AC} = \vec{C} - \vec{A} = (3, 1, 2) - (1, 2, 3) = (2, -1, -1)$
- Area of the triangle = $\frac{1}{2}|\vec{AB} \times \vec{AC}|$
- $\vec{AB} \times \vec{AC} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 1 & 1 & -2 \\ 2 & -1 & -1 \end{vmatrix}$
- $= (1 \cdot (-1) - 1 \cdot (-1))\vec{i} - (1 \cdot (-1) - (-2) \cdot 2)\vec{j} + (1 \cdot (-1) - 1 \cdot 2)\vec{k}$
- $= 0\vec{i} - (-1 + 4)\vec{j} + (-1 - 2)\vec{k} = 0\vec{i} - 3\vec{j} - 3\vec{k}$
- $|\vec{AB} \times \vec{AC}| = \sqrt{0^2 + (-3)^2 + (-3)^2} = \sqrt{0 + 9 + 9} = \sqrt{18} = 3\sqrt{2}$
- Area of the triangle = $\frac{1}{2} \cdot 3\sqrt{2} = \frac{3\sqrt{2}}{2}$ square units

### Problem 3: Finding the Shortest Distance Between Skew Lines

Find the shortest distance between the lines $L_1: \vec{r} = (1, 2, 3) + t(2, 1, -1)$ and $L_2: \vec{r} = (2, 1, 0) + s(1, -1, 2)$.

Solution:
- Let $\vec{a} = (1, 2, 3)$, $\vec{b} = (2, 1, -1)$, $\vec{c} = (2, 1, 0)$, and $\vec{d} = (1, -1, 2)$
- The shortest distance between the skew lines is given by:
  $d = \frac{|(\vec{c} - \vec{a}) \cdot (\vec{b} \times \vec{d})|}{|\vec{b} \times \vec{d}|}$
- $\vec{c} - \vec{a} = (2, 1, 0) - (1, 2, 3) = (1, -1, -3)$
- $\vec{b} \times \vec{d} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 2 & 1 & -1 \\ 1 & -1 & 2 \end{vmatrix}$
- $= ((1 \cdot 2) - (-1) \cdot (-1))\vec{i} - ((2 \cdot 2) - (-1) \cdot 1)\vec{j} + ((2 \cdot (-1)) - (1 \cdot 1))\vec{k}$
- $= (2 - 1)\vec{i} - (4 - (-1))\vec{j} + ((-2) - 1)\vec{k} = \vec{i} - 5\vec{j} - 3\vec{k}$
- $(\vec{c} - \vec{a}) \cdot (\vec{b} \times \vec{d}) = (1, -1, -3) \cdot (1, -5, -3) = 1 \cdot 1 + (-1) \cdot (-5) + (-3) \cdot (-3) = 1 + 5 + 9 = 15$
- $|\vec{b} \times \vec{d}| = \sqrt{1^2 + (-5)^2 + (-3)^2} = \sqrt{1 + 25 + 9} = \sqrt{35}$
- Shortest distance = $\frac{|15|}{\sqrt{35}} = \frac{15}{\sqrt{35}} = \frac{15}{\sqrt{35}} \cdot \frac{\sqrt{35}}{\sqrt{35}} = \frac{15\sqrt{35}}{35} = \frac{3\sqrt{35}}{7}$ units
""",
    
    "Complex_Numbers": """
# Complex Numbers: Fundamentals and Applications

## Basic Definitions

A complex number is a number of the form $z = a + bi$, where $a$ and $b$ are real numbers, and $i$ is the imaginary unit with the property $i^2 = -1$.

- $a$ is called the real part of $z$, denoted by $\text{Re}(z)$
- $b$ is called the imaginary part of $z$, denoted by $\text{Im}(z)$

## Algebraic Operations

### 1. Addition and Subtraction

If $z_1 = a + bi$ and $z_2 = c + di$, then:

- $z_1 + z_2 = (a + c) + (b + d)i$
- $z_1 - z_2 = (a - c) + (b - d)i$

### 2. Multiplication

If $z_1 = a + bi$ and $z_2 = c + di$, then:

$z_1 \cdot z_2 = (a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i$

### 3. Division

If $z_1 = a + bi$ and $z_2 = c + di$ (where $z_2 \neq 0$), then:

$\frac{z_1}{z_2} = \frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i$

## Complex Conjugate

The complex conjugate of $z = a + bi$ is $\bar{z} = a - bi$.

Properties of complex conjugate:
- $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$
- $\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}$
- $\overline{\frac{z_1}{z_2}} = \frac{\bar{z_1}}{\bar{z_2}}$
- $z \cdot \bar{z} = a^2 + b^2 = |z|^2$

## Modulus and Argument

The modulus (absolute value) of a complex number $z = a + bi$ is defined as:

$$|z| = \sqrt{a^2 + b^2}$$

The argument (or phase) of a complex number $z = a + bi$ is the angle $\theta$ in the complex plane, defined as:

$$\arg(z) = \tan^{-1}\left(\frac{b}{a}\right)$$

with appropriate adjustments for the quadrant in which $z$ lies.

Properties of modulus:
- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$
- $|\frac{z_1}{z_2}| = \frac{|z_1|}{|z_2|}$
- $|z^n| = |z|^n$

Properties of argument:
- $\arg(z_1 \cdot z_2) = \arg(z_1) + \arg(z_2)$
- $\arg\left(\frac{z_1}{z_2}\right) = \arg(z_1) - \arg(z_2)$
- $\arg(z^n) = n \cdot \arg(z)$

## Polar Form

A complex number $z = a + bi$ can be written in polar form as:

$$z = r(\cos\theta + i\sin\theta) = re^{i\theta}$$

where $r = |z| = \sqrt{a^2 + b^2}$ and $\theta = \arg(z)$.

The exponential form $re^{i\theta}$ is based on Euler's formula: $e^{i\theta} = \cos\theta + i\sin\theta$.

## De Moivre's Theorem

If $z = r(\cos\theta + i\sin\theta)$, then for any integer $n$:

$$z^n = r^n(\cos(n\theta) + i\sin(n\theta)) = r^ne^{in\theta}$$

This theorem is particularly useful for finding powers and roots of complex numbers.

## Roots of Complex Numbers

The $n$-th roots of a complex number $z = re^{i\theta}$ are given by:

$$z^{1/n} = r^{1/n}e^{i(\theta + 2k\pi)/n}$$

where $k = 0, 1, 2, ..., n-1$.

These $n$ roots are equally spaced on a circle of radius $r^{1/n}$ in the complex plane.

## Complex Numbers in Geometry

### 1. Rotation

Multiplying a complex number $z$ by $e^{i\theta}$ rotates $z$ counterclockwise by an angle $\theta$ about the origin.

### 2. Reflection

The complex conjugate $\bar{z}$ represents the reflection of $z$ across the real axis.

### 3. Translation

Adding a complex number $a + bi$ to $z$ translates $z$ by $a$ units horizontally and $b$ units vertically.

## Common JEE Problems

### Problem 1: Finding Powers of Complex Numbers

Find the value of $(1 + i)^6$.

Solution:
- $1 + i = \sqrt{2}e^{i\pi/4}$ (in polar form)
- Using De Moivre's theorem: $(1 + i)^6 = (\sqrt{2})^6 e^{6i\pi/4} = 8e^{6i\pi/4} = 8e^{3i\pi/2} = 8(\cos(3\pi/2) + i\sin(3\pi/2)) = 8(0 - i) = -8i$

### Problem 2: Solving Complex Equations

Solve the equation $z^4 + 16 = 0$.

Solution:
- Rearranging: $z^4 = -16 = 16e^{i\pi}$
- Taking the fourth root: $z = 16^{1/4}e^{i(\pi + 2k\pi)/4} = 2e^{i(\pi/4 + k\pi/2)}$ where $k = 0, 1, 2, 3$
- For $k = 0$: $z_1 = 2e^{i\pi/4} = 2(\cos(\pi/4) + i\sin(\pi/4)) = 2 \cdot \frac{1}{\sqrt{2}}(1 + i) = \sqrt{2}(1 + i)$
- For $k = 1$: $z_2 = 2e^{i3\pi/4} = 2(\cos(3\pi/4) + i\sin(3\pi/4)) = 2 \cdot \frac{1}{\sqrt{2}}(-1 + i) = \sqrt{2}(-1 + i)$
- For $k = 2$: $z_3 = 2e^{i5\pi/4} = 2(\cos(5\pi/4) + i\sin(5\pi/4)) = 2 \cdot \frac{1}{\sqrt{2}}(-1 - i) = \sqrt{2}(-1 - i)$
- For $k = 3$: $z_4 = 2e^{i7\pi/4} = 2(\cos(7\pi/4) + i\sin(7\pi/4)) = 2 \cdot \frac{1}{\sqrt{2}}(1 - i) = \sqrt{2}(1 - i)$

### Problem 3: Locus Problems

Find the locus of the point $z$ such that $|z - 1| = |z - i|$.

Solution:
- Let $z = x + yi$
- $|z - 1| = |z - i|$ means $|(x + yi) - 1| = |(x + yi) - i|$
- $|(x - 1) + yi| = |x + (y - 1)i|$
- $\sqrt{(x - 1)^2 + y^2} = \sqrt{x^2 + (y - 1)^2}$
- Squaring both sides: $(x - 1)^2 + y^2 = x^2 + (y - 1)^2$
- Expanding: $x^2 - 2x + 1 + y^2 = x^2 + y^2 - 2y + 1$
- Simplifying: $-2x = -2y$
- Therefore, $x = y$
- The locus is the line $y = x$, which is the set of all points equidistant from the points 1 and $i$ in the complex plane.

### Problem 4: Finding the Roots of Unity

Find all the fifth roots of unity and show that their sum is zero.

Solution:
- The fifth roots of unity are the solutions to $z^5 = 1$
- In polar form: $1 = 1e^{i0}$
- The fifth roots are: $z_k = 1^{1/5}e^{i(0 + 2k\pi)/5} = e^{2k\pi i/5}$ where $k = 0, 1, 2, 3, 4$
- $z_0 = e^{0} = 1$
- $z_1 = e^{2\pi i/5} = \cos(2\pi/5) + i\sin(2\pi/5)$
- $z_2 = e^{4\pi i/5} = \cos(4\pi/5) + i\sin(4\pi/5)$
- $z_3 = e^{6\pi i/5} = \cos(6\pi/5) + i\sin(6\pi/5)$
- $z_4 = e^{8\pi i/5} = \cos(8\pi/5) + i\sin(8\pi/5)$
- The sum of these roots is $1 + z_1 + z_2 + z_3 + z_4$
- This sum equals $\frac{1 - z_1^5}{1 - z_1} = \frac{1 - 1}{1 - z_1} = 0$ (using the formula for the sum of a geometric series)
"""
}

# Generate knowledge base files
for topic, content in topic_content.items():
    file_path = os.path.join("knowledge_base", f"{topic}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created knowledge base file: {file_path}")

print("\nKnowledge base generation complete!")
print("You can now run the RAG agent with: streamlit run app.py")