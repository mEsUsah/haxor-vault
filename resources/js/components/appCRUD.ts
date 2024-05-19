import axios from 'axios';
import { api_host, api_apps } from '../config.ts';
import { App, AppSchema } from './interfaces.ts';
import { decryptApp, encrypteAppSchema } from './appCrypto.ts'
import { getMasterPassword } from './utils.ts';
import { toRaw } from 'vue';

/**
 * Get all apps from the API.
 * 
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

                    // Sort apps by name
                    apps.sort((a, b) => (a.name > b.name) ? 1 : -1);

                    // Sort credentials by username
                    apps.forEach(app => {
                        app.credentials.sort((a, b) => (a.username > b.username) ? 1 : -1);
                    });

                    resolve(apps);
                }
            }).catch(error => {
                reject('Failed to get apps from the API');
            });
    }); 
}

/**
 * Get app details from API.
 * 
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

                    // Sort credentials by username
                    app.credentials.sort((a, b) => (a.username > b.username) ? 1 : -1);
   
                    resolve(app);
                }
            }).catch(error => {
                reject('Failed to get app from the API');
            });
    }); 
}

/**
 * Create a app
 * 
 * @param {AppSchema} data - App data
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

/**
 * Update a app.
 * 
 * @param {string} id - App ID.
 * @param {AppSchema} data - App data.
 * @returns {Promise<App>} Updated app object.
 */
export async function updateApp(id: string, data: AppSchema): Promise<App>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_apps + "/" + id;

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encrypteAppSchema(formData, getMasterPassword())

        axios.post(url, formData, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if(response.status == 200){
                let app: App = response.data;
                app = decryptApp(app, getMasterPassword())
                resolve(app);
            }
        }).catch(error => {
            reject('Failed create app');
        });
    }); 
}

/**
 * Delete a app.
 * 
 * @param {string} id App ID.
 * @param {AppSchema} data App data.
 * @returns {Promise<string>} Status string.
 */
export async function deleteApp(id: string, data: AppSchema): Promise<String>{
    return new Promise((resolve, reject) => {
        const url = api_host + api_apps + "/" + id + "/delete";

        // Escape reactivity to prevent form from showing encrypted data.
        let formData = toRaw(data);
        formData = encrypteAppSchema(formData, getMasterPassword())

        axios.post(url, formData, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(response => {
            if(response.status == 200){
                resolve("App deleted");
            }
        }).catch(error => {
            reject('Failed create app');
        });
    }); 
}