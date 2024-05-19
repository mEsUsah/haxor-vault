/**
 * A set of simple and easy-to-use cryptography functions.
 * 
 * @author Stanley Skarshaug
 * @requires argon2-browser":^1.18.0
 * @requires crypto-js":^4.2.0
 */
import argon2 from "argon2-browser/dist/argon2-bundled.min.js";
import CryptoJS  from 'crypto-js';

const salt = 'hackingIsSimplyCuriosity';

/**
 * Generate Argon2 hash of supplied password.
 * 
 * @param {string} password Plaintext password that is to be hashed.
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

/**
 * Encrypt plaintext using AES.
 * 
 * @param {string} plaintext Plaintex to be encrypted.
 * @param {string} key Encryption key.
 * @returns {string} Ciphertext.
 */
export function encryptAES(plaintext: string, key: string): string{
    return CryptoJS.AES.encrypt(plaintext, key).toString();
}

/**
 * Decryptes ciphertext using AES.
 * 
 * @param {string} ciphertext Ciphertext to be decrypted.
 * @param {string} key Decrtyption key.
 * @returns {string} Plaintext.
 */
export function decryptAES(ciphertext: string, key: string): string{
    var bytes  = CryptoJS.AES.decrypt(ciphertext, key);
    return bytes.toString(CryptoJS.enc.Utf8);
}