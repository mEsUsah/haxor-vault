import axios from 'axios';
import { api_host, api_apptypes } from '../config.ts';
import { AppType } from './interfaces.ts';

export async function getAppTypes(): Promise<AppType[]>{
    return new Promise((resolve, reject) => {
        axios.get(api_host + api_apptypes)
            .then(response => {
                if(response.status == 200){
                    resolve(response.data);
                }
            }).catch(error => {
                reject('Failed to get app typs from the API');
            });
    }); 
}