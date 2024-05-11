import argon2 from "argon2-browser/dist/argon2-bundled.min.js";
import CryptoJS  from 'crypto-js';

const salt = 'hackingIsSimplyCuriosity';

/**
 * Generate Argon2 hash of supplied password.
 * 
 * @param {string} password - plaintext password that is to be hashed.
 * @returns {Promise<string>} Promise with hash string.
 */
export function hashArgon2(password: string): Promise<string> {
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

export function encryptAES(plaintext: string, key: string): string{
    return CryptoJS.AES.encrypt(plaintext, key).toString();
}

export function decryptAES(ciphertext: string, key: string): string{
    var bytes  = CryptoJS.AES.decrypt(ciphertext, key);
    return bytes.toString(CryptoJS.enc.Utf8);
}