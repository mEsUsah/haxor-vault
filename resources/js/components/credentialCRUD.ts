import axios from 'axios';
import { toRaw } from 'vue';
import { Credential, CredentialSchema } from './interfaces.ts';
import { api_host, api_credentials } from '../config.ts';
import { getMasterPassword } from './utils.ts';
import { encryptCredentialSchema, decryptCredential } from './credentialCrypto.ts'

/**
 * Get credential from API.
 * 
 * @param {string} id Credential id.
 * @returns {Promise<Credential>} Promise with decrypted credential.
 */
export async function getCredential(id: string): Promise<Credential>{
    return new Promise((resolve, reject) => {
        axios.get(api_host + api_credentials + "/" + id)
            .then(response => {
                if(response.status == 200){
                    let credential: Credential = response.data;
                    credential = decryptCredential(credential, getMasterPassword())
                    resolve(credential);
                }
            }).catch(error => {
                reject('Failed to get credential from the API');
            });
    }); 
}

/**
 * Create a credential.
 * 
 * @param {CredentialSchema} data Credential data.
 * @returns {Promise<Credential>} Created credential object.
 */
export async function createCredential(data: CredentialSchema): Promise<Credential>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_credentials;

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encryptCredentialSchema(formData, getMasterPassword())

        axios.post(url, formData, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if(response.status == 201){
                resolve(response.data);
            }
        }).catch(error => {
            reject('Failed create app');
        });
    }); 
}

/**
 * Update a credential.
 * 
 * @param {string} id Credential id.
 * @param {CredentialSchema} data Credential data.
 * @returns {Promise<Credential>} Created credential object.
 */
export async function updateCredential(id: string, data: CredentialSchema): Promise<Credential>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_credentials + "/" + id;

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encryptCredentialSchema(formData, getMasterPassword())

        axios.post(url, formData, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if(response.status == 200){
                let credential = response.data;
                credential = decryptCredential(credential, getMasterPassword());
                resolve(credential);
            }
        }).catch(error => {
            reject('Failed create app');
        });
    }); 
}

/**
 * Delete a credential
 * 
 * @param {string} id - Credential ID
 * @param {CredentialSchema} data Credential data
 * @returns {Promise<string>} Status string
 */
export async function deleteCredential(id: string, data: CredentialSchema): Promise<String>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_credentials + "/" + id + "/delete";

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encryptCredentialSchema(formData, getMasterPassword())

        axios.post(url, formData, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if(response.status == 200){
                resolve("Credential deleted");
            }
        }).catch(error => {
            reject('Failed create app');
        });
    }); 
}