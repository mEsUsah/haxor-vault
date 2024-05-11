import axios from 'axios';
import { api_host, api_apps } from '../config.ts';
import { App, AppSchema } from './interfaces.ts';

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

        axios.post(url, data, {
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