/* Docstring:
 * Write a generic function `flattenOneLevel` that flattens an array by one depth.
 * The input array may contain elements of type `T` or arrays of `T`, and the output should be a new array of `T`.
 * The original array must not be mutated.
 */
<｜fim▁begin｜>
export function flattenOneLevel<T>(input: (T | T[])[]): T[] {
<｜fim▁hole｜>
  const result: T[] = [];
  for (const element of input) {
    if (Array.isArray(element)) {
      result.push(...element);
    } else {
      result.push(element);
    }
  }
  return result;
<｜fim▁end｜>
}
