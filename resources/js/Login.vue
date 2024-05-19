<template>
    <div class="login-section__wrapper">
        <StatusMessageBox 
            v-if="statusMessage"
            :statusMessage>
        </StatusMessageBox>

        <form @submit="login" class="login-form__wrapper">
            <img class="login-section__logo" :src="assets.haxorLogo" alt="logo">
            <h1>Vault</h1>
            
            <div class="login-form__input">
                <input type="text" v-model="username" placeholder="Username">
            </div>
            <div class="login-form__input">
                <input type="password" v-model="password" placeholder="Password">
            </div>
            <button type="submit">Login</button>

            <div>Don't have an account? <a href="/register">Register</a></div>
        </form>

    </div>
</template>
<script lang="ts">

import { defineComponent, reactive, ref } from 'vue';
import { useReCaptcha } from 'vue-recaptcha-v3'
import { StatusMessage, AuthenticationSchema } from './components/interfaces.ts';
import { authenticate } from './components/userAuthenticate.ts';
import { staticPath } from './config';
import { animateElementShake } from './components/animations';
import StatusMessageBox from './views/MessageBox.vue';

const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

export default defineComponent({
    components: {
        StatusMessageBox
    },
    setup(){
        // View setup
        const username = ref(<string>"");
        const password = ref(<string>"");
        const statusMessage = ref(<StatusMessage|null>null);

        // Asset setup.
        const assets: object = reactive({
            haxorLogo: <string>staticPath + 'icons/haxor-logo-only-black.svg',
        });

        // ReCaptcha setup.
        const reCaptchaInstance = useReCaptcha();
        async function reCaptcha() {
            await reCaptchaInstance?.recaptchaLoaded();
            return await reCaptchaInstance?.executeRecaptcha("login");
        }

        /**
         * Authenticate user.
         * 
         * Displays status message if authentication succeeds or fails.
         * Redirects to dashboard if authentication is successful.
         * 
         * @param {Event} event 
         * @returns {Promise<void>}
         */
        async function login(event:Event): Promise<void> {
            event.preventDefault();
            const captchaToken = await reCaptcha();
            
            await authenticate(<AuthenticationSchema>{
                username: username.value,
                password: password.value,
                csrfmiddlewaretoken: csrfToken?csrfToken:"",
                captchaToken: captchaToken?captchaToken:"",
            }).then(() => {
                statusMessage.value = {
                    type: "success",
                    messageClass: "message--success",
                    text: "Logged in!",
                };

                // Wait 1 second to allow the user to read the success message.
                setTimeout(() => {
                    location.href = "/dashboard";
                }, 1000);
            }).catch(error => {
                if(error == "password-error"){
                    statusMessage.value = {
                        type: "error",
                        messageClass: "message--error",
                        text: "Username or Password was wrong",
                    }
                    animateElementShake("loginAlert");
                }
                if(error == "not-verified"){
                    statusMessage.value = {
                        type: "error",
                        messageClass: "message--error",
                        text: "User account not verified",
                    }
                }
                if(error == "system-error"){
                    statusMessage.value = {
                        type: "error",
                        messageClass: "message--error",
                        text: "Sorry, we have a problem...",
                    };
                    
                    // Error is problaby caused by invalid CSRF token.
                    // Refresh page to get a new CSRF token.
                    location.reload(); 
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