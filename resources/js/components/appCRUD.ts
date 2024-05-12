import axios from 'axios';
import { api_host, api_apps } from '../config.ts';
import { App, AppSchema } from './interfaces.ts';
import { encrypteAppSchema } from './appCrypto.ts'
import { getMasterPassword } from './utils.ts';
import { toRaw } from 'vue';

export async function getApps(): Promise<App[]>{
    return new Promise((resolve, reject) => {
        axios.get(api_host + api_apps)
            .then(response => {
                if(response.status == 200){
                    resolve(response.data);
                }
            }).catch(error => {
                reject('Failed to get apps from the API');
            });
    }); 
}

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