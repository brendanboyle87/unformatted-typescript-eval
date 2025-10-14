export function invertObject(source: Record<string, string | number | boolean>): Record<string, string> {
  const result: Record<string, string> = {};
  Object.entries(source).forEach(([key, value]) => {
    result[String(value)] = key;
  });
  return result;
}
