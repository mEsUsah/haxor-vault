import axios from 'axios';
import { api_host, api_apps } from '../config.ts';
import { App, AppSchema } from './interfaces.ts';
import { decryptApp, encrypteAppSchema } from './appCrypto.ts'
import { getMasterPassword } from './utils.ts';
import { toRaw } from 'vue';

/**
 * Get all user apps from API
 * @returns {Promise<App[]>} - Promise with decrypted apps
 */
export async function getApps(): Promise<App[]>{
    return new Promise((resolve, reject) => {
        axios.get(api_host + api_apps)
            .then(response => {
                if(response.status == 200){
                    let apps: App[] = response.data;
                    apps.forEach(app => {
                        app = decryptApp(app, getMasterPassword())
                    });
                    resolve(apps);
                }
            }).catch(error => {
                reject('Failed to get apps from the API');
            });
    }); 
}

/**
 * Get user app from API
 * @param {string} id - App id
 * @returns {Promise<App>} - Promise with decrypted apps
 */
export async function getApp(id: string): Promise<App>{
    return new Promise((resolve, reject) => {
        axios.get(api_host + api_apps + "/" + id)
            .then(response => {
                if(response.status == 200){
                    let app: App = response.data;
                    app = decryptApp(app, getMasterPassword())
                    resolve(app);
                }
            }).catch(error => {
                reject('Failed to get app from the API');
            });
    }); 
}

/**
 * Create an user app
 * @param {AppSchema} data
 * @returns {Promise<App>} Created app object
 */
export async function createApp(data: AppSchema): Promise<App>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_apps;

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encrypteAppSchema(formData, getMasterPassword())

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