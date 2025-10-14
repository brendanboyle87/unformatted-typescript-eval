const cloneStructure = (input: unknown): unknown => {
  if (Array.isArray(input)) {
    return input.map((item) => cloneStructure(item));
  }
  if (input !== null && typeof input === 'object') {
    const result: Record<string, unknown> = {};
    for (const [key, value] of Object.entries(input as Record<string, unknown>)) {
      result[key] = cloneStructure(value);
    }
    return result;
  }
  return input;
};

const isNumericSegment = (segment: string): boolean => /^\d+$/.test(segment);

export function setValueByPath<T extends Record<string, unknown>>(source: T, path: string, value: unknown): T & Record<string, unknown> {
  if (!path) {
    return cloneStructure(value) as T & Record<string, unknown>;
  }

  const clone = cloneStructure(source) as Record<string, unknown> | unknown[];
  const segments = path.split('.');
  let current: any = clone;

  for (let index = 0; index < segments.length; index += 1) {
    const segment = segments[index];
    const isLast = index === segments.length - 1;
    const key = isNumericSegment(segment) ? Number(segment) : segment;

    if (isLast) {
      if (Array.isArray(current) && typeof key === 'number') {
        current[key] = cloneStructure(value);
      } else {
        current[key] = cloneStructure(value);
      }
      break;
    }

    const nextSegment = segments[index + 1];
    const shouldCreateArray = isNumericSegment(nextSegment);

    if (current[key] === undefined || current[key] === null || typeof current[key] !== 'object') {
      current[key] = shouldCreateArray ? [] : {};
    } else {
      current[key] = cloneStructure(current[key]);
    }

    current = current[key];
  }

  return clone as T & Record<string, unknown>;
}
