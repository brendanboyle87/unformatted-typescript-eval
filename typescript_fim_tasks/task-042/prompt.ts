/* Docstring:
 * Implement `withTimeout` to wrap a promise with a timeout.
 * If the wrapped promise does not settle within the specified milliseconds, reject with a timeout error message.
 * Allow a custom error message, defaulting to `"Operation timed out"`.
 */
<｜fim▁begin｜>
export function withTimeout<T>(promise: Promise<T>, timeoutMs: number, message = 'Operation timed out'): Promise<T> {
<｜fim▁hole｜>
  return new Promise<T>((resolve, reject) => {
    const timer = setTimeout(() => {
      reject(new Error(message));
    }, timeoutMs);

    promise
      .then((value) => {
        clearTimeout(timer);
        resolve(value);
      })
      .catch((error) => {
        clearTimeout(timer);
        reject(error);
      });
  });
<｜fim▁end｜>
}
