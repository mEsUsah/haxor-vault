import { Credential, CredentialSchema } from './interfaces.ts';
import { encryptAES, decryptAES } from './cryptography.ts';

/**
 * Decrypts credential, and app it belongs to.
 * 
 * @param { Credential } credential Array of Apps with encrypted name and credentials.
 * @param {string} key Decryption key.
 * @returns { Credential } Decrypted Apps.
 */
export function decryptCredential(credential:Credential, key: string): Credential {
    credential.username = decryptAES(credential.username, key);
    credential.password = decryptAES(credential.password, key);
    credential.app.name = decryptAES(credential.app.name, key);
    return credential;
}


/**
 * Encrypts an CredentialSchema.
 * 
 * @param { CredentialSchema } credential Plaintext credential schema.
 * @param {string} key Encryption key.
 * @returns { CredentialSchema } Encrypted credential schema, used for updating or creating credentials.
 */
export function encryptCredentialSchema(credential:CredentialSchema, key: string): CredentialSchema{
    credential.username = encryptAES(credential.username, key);
    credential.password = encryptAES(credential.password, key);
    return credential;
}