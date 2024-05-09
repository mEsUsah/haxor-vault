<template>
    <div class="login-section__wrapper">
        <div v-if="statusMessage" class="alert" :class="statusMessage.messageClass" id="loginAlert">
            <img class="alert-icon" 
                :src="assets.warningIcon" 
                alt="warning symbol">
            <p class="alert__message">{{statusMessage.text}}</p>
        </div>
        <div >
            <form @submit="login" class="login-form__wrapper">
                <img class="login-section__logo" 
                    :src="assets.haxorLogo" 
                    alt="logo">
                <h1>Vault</h1>
                <div class="login-form__input">
                    <input type="text" 
                        v-model="username"
                        placeholder="Username">
                </div>
                <div class="login-form__input">
                    <input type="password"
                        v-model="password"
                        placeholder="Password">
                </div>
                <button type="submit">Login</button> 
            </form>
        </div>
    </div>
</template>
<script lang="ts">
import axios from 'axios';
import { PropType, Ref, defineComponent, reactive, ref } from 'vue';
import { staticPath } from './config';
import { generateHash } from './components/generateHash';
import { animateElementShake } from './components/animations'

interface StatusMessage {
    type: string,
    messageClass: string,
    text: string,
}

export default defineComponent({
    setup(){
        const assets: object = reactive({
            haxorLogo: <string>staticPath + 'icons/haxor-logo-only-black.svg',
            warningIcon: <string>staticPath + 'icons/warning.png'
        });
        const username = ref(<string>"");
        const password = ref(<string>"");
        const statusMessage = ref(<StatusMessage|null>null);

        async function authenticate(data: object): Promise<string> {
            return new Promise((resolve, reject) => {
                axios.post("/login", data, {
                    withCredentials: true,
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then((response)=>{
                    if(response.status == 200){
                        if(response.data.authenticated){
                            localStorage.setItem("password", password.value);
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

        async function login(event:Event): Promise<void> {
            event.preventDefault();
            let passwordHash: string = await generateHash(password.value);
            
 
            await authenticate({
                username: username.value,
                password: passwordHash,
                csrfmiddlewaretoken: csrfToken
            }).then(() => {
                statusMessage.value = {
                    type: "success",
                    messageClass: "alert--success",
                    text: "Logged in!",
                };
            }).catch(error => {
                if(error == "password-error"){
                    statusMessage.value = {
                        type: "error",
                        messageClass: "alert--error",
                        text: "Username or Password was wrong",
                    }
                    animateElementShake("loginAlert");
                }
                if(error == "system-error"){
                    statusMessage.value = {
                        type: "error",
                        messageClass: "alert--error",
                        text: "Sorry, we have a problem...",
                    };
                    location.reload(); // Refresh page to get new csrf token
                }
            });
        }

        return {
            assets,
            username,
            password,
            statusMessage,
            login
        }
    }
});
</script>