import { App } from './interfaces.ts';
import { decryptAES } from './cryptography.ts';

/**
 * Decrypts Array of Apps, and credentials found in each app.
 * @param { App[] } encryptedApps - Array of Apps with encrypted name and credentials
 * @param {string} key - Decryption key
 * @returns { App[] } Decrypted Apps
 */
export function decryptApps(encryptedApps:App[], key: string): App[] {
    let decryptedApps:App[] = [];
    encryptedApps.forEach(app => {
        app.name = decryptAES(app.name, key);
        app.credentials.forEach(credential => {
            credential.username = decryptAES(credential.username, key);
            credential.password = decryptAES(credential.password, key);
        })
        decryptedApps.push(app);
    });
    return decryptedApps;
}