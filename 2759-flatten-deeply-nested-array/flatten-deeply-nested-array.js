var flat = function(arr, n) {
    if (n === 0) return arr.slice();
    let result = [];
    for (const item of arr) {
        if (Array.isArray(item) && n > 0) {
            result.push(...flat(item, n - 1));
        } else {
            result.push(item);
        }
    }
    return result;
};