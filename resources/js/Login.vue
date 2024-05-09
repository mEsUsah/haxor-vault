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

        function animateMessage():void {
            const loginAlert = document.getElementById("loginAlert");
            if(loginAlert){
                loginAlert.classList.remove("shake");
                loginAlert.classList.add("shake");
                setTimeout(() => {
                    loginAlert.classList.remove("shake");
                }, 1000);
            }
        }

        async function login(event:Event): Promise<void> {
            event.preventDefault();
            let passwordHash: string = await generateHash(password.value);

            axios.post("/login", {
                username: username.value,
                password: passwordHash,
                csrfmiddlewaretoken: csrfToken
            }, {
                withCredentials: true,
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((response)=>{
                if(response.status == 200){
                    if(response.data.authenticated){
                        localStorage.setItem("password", password.value);
                        statusMessage.value = {
                            type: "success",
                            messageClass: "alert--success",
                            text: "Logged in!",
                        };
                    } else {
                        statusMessage.value = {
                            type: "error",
                            messageClass: "alert--error",
                            text: "Username or Password was wrong",
                        };
                        animateMessage();
                        localStorage.removeItem("password");
                    }
                }
            })
            .catch(error => {
                statusMessage.value = {
                    type: "error",
                    messageClass: "alert--error",
                    text: "Sorry, we have a problem...",
                };
                animateMessage();
                location.reload(); // Refresh page to get new csrf token
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