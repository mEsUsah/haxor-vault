import axios from 'axios';
import { generateHash } from './generateHash';

interface AuthenticationInterface {
    username: string,
    password: string,
    csrfmiddlewaretoken: string
}

const url = "/login";

/**
 * Authenticates using front-end password hashing, and passes the hash
 * to the backend endpoint.
 * 
 * If successfully authenticated, the session cookie will be set, and 
 * cleartext password will be stored in localstorage. Password is stored in 
 * localstorage for ease of encrypting and decrypting secrets once authenticated.
 * 
 * @param {AuthenticationInterface} data - Data that will be passed to the API.
 * @returns {Promise<string>} Promise with status string.
 */
export async function authenticate(data: AuthenticationInterface): Promise<string> {
    let passwordClearText = data.password;
    let passwordHash: string = await generateHash(passwordClearText);
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
                    localStorage.setItem("password", passwordClearText);
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