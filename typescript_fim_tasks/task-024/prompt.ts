/* Docstring:
 * Implement `insertionSortByKey` to sort an array of objects using the insertion sort algorithm.
 * The function accepts an array of records and a key whose numeric values determine the ordering.
 * Return a new array sorted ascending by the key without mutating the original.
 */
<｜fim▁begin｜>
export function insertionSortByKey<T extends Record<string, unknown>>(items: T[], key: keyof T): T[] {
<｜fim▁hole｜>
  const result = items.map((item) => ({ ...item }));

  for (let i = 1; i < result.length; i += 1) {
    const current = result[i];
    let j = i - 1;

    while (j >= 0 && Number(result[j][key]) > Number(current[key])) {
      result[j + 1] = result[j];
      j -= 1;
    }

    result[j + 1] = current;
  }

  return result;
<｜fim▁end｜>
}
