var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length);
        let completed = 0;
        if (functions.length === 0) resolve(results);
        functions.forEach((fn, i) => {
            fn().then(value => {
                results[i] = value;
                completed++;
                if (completed === functions.length) resolve(results);
            }).catch(reject);
        });
    });
};