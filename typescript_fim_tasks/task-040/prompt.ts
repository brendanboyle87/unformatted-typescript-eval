/* Docstring:
 * Implement `invertObject` to swap keys and values of an object.
 * The input object's values must be convertible to strings to become keys in the result.
 * When duplicate values occur, later keys should overwrite earlier ones.
 */
<｜fim▁begin｜>
export function invertObject(source: Record<string, string | number | boolean>): Record<string, string> {
<｜fim▁hole｜>
  const result: Record<string, string> = {};
  Object.entries(source).forEach(([key, value]) => {
    result[String(value)] = key;
  });
  return result;
<｜fim▁end｜>
}
