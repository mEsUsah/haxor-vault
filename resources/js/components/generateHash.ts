import argon2 from "argon2-browser/dist/argon2-bundled.min.js";

export function generateHash(password): Promise<string> {
    return new Promise((resolve, reject) => {
        argon2.hash({ pass: password, salt: 'somesalt' })
            .then(hash => {
                resolve(hash.encoded);
            })
            .catch(error => {
                console.error(error.message, error.code)
                reject("");
            });
    });
};