// Rotate Matrix
// Description
// Rotate an N * N matrix clockwise 90 degrees.

// Assumptions

// The matrix is not null and N >= 0
// Examples

// { {1,  2,  3}

//   {8,  9,  4},

//   {7,  6,  5} }

// after rotation is

// { {7,  8,  1}

//   {6,  9,  2},

//   {5,  4,  3} }

public class Solution {
	public void rotate(int[][] matrix) {
		// Write your solution here.
		if (matrix.length == 0) {
			return;
		}
		int n = matrix.length;
		int temp = 0;
		for (int i = 0; i < n / 2; i++) {
			for (int k = 0; k < n - 2*i - 1; k++) {
				temp = matrix[i][k + i];
				matrix[i][k + i] = matrix[n - i - 1 - k][i];
				matrix[n - i - 1 - k][i] = matrix[n - i - 1][n - i - 1 - k];
				matrix[n - i - 1][n - i - 1 - k] = matrix[k + i][n - i - 1];
				matrix[k + i][n - i - 1] = temp;
			}
		}
	}
}
