import axios from 'axios';
import { hashArgon2 } from './cryptography.ts';
import { RegistrationSchema } from './interfaces.ts';

const url = "/register";

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
export async function registerUser(data: RegistrationSchema): Promise<string> {
    let passwordClearText = data.password;
    let passwordHash: string = await hashArgon2(passwordClearText);
    data.password = passwordHash;
    
    let passwordRepeatedClearText = data.passwordConfirm;
    let passwordRepeatedHash: string = await hashArgon2(passwordRepeatedClearText);
    data.passwordConfirm = passwordRepeatedHash;
    
    return new Promise((resolve, reject) => {
        axios.post(url, data, {
            withCredentials: true,
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })
        .then((response)=>{
            if(response.status == 200){
                console.log("userRegister:", response.data);
                resolve("ok");
            }
        })
        .catch(error => {
            if(error.response.status == 400 && error.response.data.error == "password-mismatch"){
                reject("password-mismatch");
            }
            if(error.response.status == 400 && error.response.data.error == "user-exists"){
                reject("user-exists");
            }
            reject("general-error");
        });

    })
}