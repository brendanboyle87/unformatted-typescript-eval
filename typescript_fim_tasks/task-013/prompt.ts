/* Docstring:
 * Implement `chunkArray` that splits an array into equally sized chunks except possibly the last chunk.
 * Accept the input array and a positive chunk size; throw an error if the size is less than one.
 * Return a new array of chunk arrays without mutating the original input.
 */
<｜fim▁begin｜>
export function chunkArray<T>(items: T[], size: number): T[][] {
<｜fim▁hole｜>
  if (size <= 0) {
    throw new Error('size must be greater than zero');
  }

  const result: T[][] = [];
  for (let index = 0; index < items.length; index += size) {
    result.push(items.slice(index, index + size));
  }

  return result;
<｜fim▁end｜>
}
