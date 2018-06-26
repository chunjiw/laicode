// Set Matrix Zeroes
// Description
// Given a m x n matrix, if an element is 0, set its entire row and column to 0.

// E.g.    Input: Matrix =  [

//                                      [1, 1, 1, 1, 0],

//                                      [0, 1, 1, 0, 1],

//                                      [1, 1, 1, 0, 1],

//                                      [1, 1, 1, 1, 1]

//                                  ]

// Output: Matrix = [

//                              [0, 0, 0, 0, 0],

//                              [0, 0, 0, 0, 0],

//                              [0, 0, 0, 0, 0],

//                              [0, 1, 1, 0, 0],

//                           ]

public class Solution {
    public void setZero(int[][] matrix) {
        //Input your code here
        if (matrix == null || matrix.length == 0) {
            return;
        }
        int m = matrix.length;
        int n = matrix[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    this.setColRow(matrix, i, j);
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 99) {
                    matrix[i][j] = 0;
                }
            }
        }
        return;
    }

    private void setColRow(int[][] matrix, int i, int j) {
        for (int k = 0; k < matrix.length; k++) {
            if (matrix[k][j] != 0) {
                matrix[k][j] = 99;    
            }
        }
        for (int k = 0; k < matrix[0].length; k++) {
            if (matrix[i][k] != 0) {
                matrix[i][k] = 99;    
            }
        } 
        return;
    }
}
