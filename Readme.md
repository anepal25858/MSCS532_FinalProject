Explanation of the Implementation:

1. Naive Matrix Multiplication (matmul_naive):
•	This method multiplies two matrices A and B without any optimizations.
•	It iterates over every element in the result matrix C, computing the sum of element-wise products from row i of Aand column j of B.
•	Time complexity: O(n³), where n is the matrix size.

2. Tiled Matrix Multiplication (matmul_tiled):
•	This implementation divides the matrix multiplication into smaller sub-blocks (tiles).
•	The idea is to improve cache performance by operating on smaller sections of the matrices that can fit into the CPU cache, reducing memory latency.
•	The three nested loops process each tile block-by-block, avoiding frequent cache misses.

Parameters:
•	tile_size: Defines the size of the sub-blocks.
•	A, B: Input matrices.
•	C: Output matrix where results are stored.
