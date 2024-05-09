import argon2 from "argon2-browser/dist/argon2-bundled.min.js";

const salt = 'hackingIsSimplyCuriosity';

/**
 * Generate Argon2 hash of supplied password.
 * 
 * @param {string} password - plaintext password that is to be hashed.
 * @returns {Promise<string>} Promise with hash string.
 */
export function generateHash(password: string): Promise<string> {
    return new Promise((resolve, reject) => {
        argon2.hash({ pass: password, salt: salt })
            .then(hash => {
                resolve(hash.encoded);
            })
            .catch(error => {
                console.error(error.message, error.code)
                reject("");
            });
    });
};