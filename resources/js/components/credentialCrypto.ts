import { Credential, CredentialSchema } from './interfaces.ts';
import { encryptAES, decryptAES } from './cryptography.ts';

/**
 * Encrypts an AppSchema.
 * @param { CredentialSchema } credential - Plaintext credential schema
 * @param {string} key - Encryption key
 * @returns { CredentialSchema } Encrypted credential schema
 */
export function encryptCredentialSchema(credential:CredentialSchema, key: string): CredentialSchema{
    credential.username = encryptAES(credential.username, key);
    credential.password = encryptAES(credential.password, key);
    return credential;
}