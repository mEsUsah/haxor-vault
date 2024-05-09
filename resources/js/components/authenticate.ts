import axios from 'axios';
import { generateHash } from './generateHash';

interface AuthenticationInterface {
    username: string,
    password: string,
    csrfmiddlewaretoken: string
}

const url = "/login";

/**
 * @param {AuthenticationInterface} data - Data that will be passed to the API
 * @returns {Promise<string>} Promise with string
 */
export async function authenticate(data: AuthenticationInterface): Promise<string> {
    let passwordHash: string = await generateHash(data.password);
    data.password = passwordHash;
    
    return new Promise((resolve, reject) => {
        axios.post(url, data, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then((response)=>{
            if(response.status == 200){
                if(response.data.authenticated){
                    localStorage.setItem("password", passwordHash);
                    resolve("success");
                } else {
                    localStorage.removeItem("password");
                    reject("password-error");
                }
            }
        })
        .catch(error => {
            console.log(error)
            reject("system-error");
        });

    })
}