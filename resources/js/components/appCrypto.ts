import { App, AppSchema } from './interfaces.ts';
import { encryptAES, decryptAES } from './cryptography.ts';

/**
 * Decrypts Array of Apps, and credentials found in each app.
 * @param { App[] } encryptedApps - Array of Apps with encrypted name and credentials
 * @param {string} key - Decryption key
 * @returns { App[] } Decrypted Apps
 */
export function decryptApp(app:App, key: string): App {
    app.name = decryptAES(app.name, key);
    app.credentials.forEach(credential => {
        credential.username = decryptAES(credential.username, key);
        credential.password = decryptAES(credential.password, key);
    });
    return app;
}


/**
 * Encrypts an AppSchema.
 * @param { AppSchema } app - Plaintext App schema
 * @param {string} key - Encryption key
 * @returns { AppSchema } Encrypted App
 */
export function encrypteAppSchema(app:AppSchema, key: string): AppSchema{
    app.name = encryptAES(app.name, key);
    return app;
}