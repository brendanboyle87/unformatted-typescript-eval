/* Docstring:
 * Implement `searchMatrix` to determine whether a target number exists in a 2D matrix.
 * Each row of the matrix is sorted in ascending order and the first element of each row is greater than the last element of the previous row.
 * Use binary search across the flattened matrix and return a boolean indicating whether the target is present.
 */
<｜fim▁begin｜>
export function searchMatrix(matrix: number[][], target: number): boolean {
<｜fim▁hole｜>
  if (matrix.length === 0 || matrix[0].length === 0) {
    return false;
  }

  const rows = matrix.length;
  const cols = matrix[0].length;
  let low = 0;
  let high = rows * cols - 1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const row = Math.floor(mid / cols);
    const col = mid % cols;
    const value = matrix[row][col];

    if (value === target) {
      return true;
    }

    if (value < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return false;
<｜fim▁end｜>
}
