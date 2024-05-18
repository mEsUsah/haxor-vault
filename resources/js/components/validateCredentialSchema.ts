import { CredentialSchema } from './interfaces.ts';

export function validateCredentialSchema(credential: CredentialSchema): Boolean {
    if (credential.username.trim() === "" || credential.username.length > 100) {
        return false;
    }
    if (credential.password.trim() === "" || credential.password.length > 100) {
        return false;
    }
    if (credential.app.trim() === "") {
        return false;
    }
    return true;

}