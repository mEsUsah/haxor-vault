<template>
    <div class="login-section__wrapper">
        <div v-if="statusMessage" class="alert" :class="statusMessage.messageClass">
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
import { PropType, defineComponent } from 'vue';
import { staticPath } from './config.ts';

interface StatusMessage {
    type: string,
    messageClass: string,
    text: string,
}

export default defineComponent({
    data() {
        return {
            assets: <object>{
                haxorLogo: <string>staticPath + 'icons/haxor-logo-only-black.svg',
                warningIcon: <string>staticPath + 'icons/warning.png'
            },
            csrfToken: <string>csrfToken,
            username: <string>"",
            password: <string>"",
            statusMessage: <StatusMessage>null
        }
    },
    methods: {
        login(event): void {
            event.preventDefault();
            axios.post("/login", {
                username: this.username,
                password: this.password,
                csrfmiddlewaretoken: this.csrfToken
            }, {
                withCredentials: true,
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((response)=>{
                if(response.status == 200){
                    localStorage.setItem("password", this.password);
                }
            })
            .catch(error => {
                localStorage.removeItem("password");
                this.statusMessage = {
                    type: "error",
                    messageClass: "alert--error",
                    text: "Username or Password was wrong",
                };
                console.log(this.statusMessage);
            });
            
        }
    },
    mounted() {
        console.log(this.csrfToken);
    },
});
</script>