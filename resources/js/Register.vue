<template>
    <div class="login-section__wrapper">
        <StatusMessageBox 
            v-if="statusMessage"
            :statusMessage>
        </StatusMessageBox>

        <form @submit="register" class="login-form__wrapper">
            <img class="login-section__logo" :src="assets.haxorLogo" alt="logo">
            <h1>Vault</h1>
            
            <div class="login-form__input">
                <input type="text" v-model="email" placeholder="Email">
            </div>
            <div class="login-form__input">
                <input type="password" v-model="password" placeholder="Password">
            </div>
            <div class="login-form__input">
                <input type="password" v-model="passwordConfirm" placeholder="Confirm password">
            </div>
            <button type="submit" :disabled="!enableRegistertration">Register</button> 

            <div>Already have an account? <a href="/login">Login</a></div>
        </form>

    </div>
</template>
<script lang="ts">

import { defineComponent, reactive, ref } from 'vue';
import { useReCaptcha } from 'vue-recaptcha-v3'
import { RegistrationSchema, StatusMessage, ValidationResult } from './components/interfaces.ts';
import { validateRegistrationSchema } from './components/validateRegistrationSchema.ts';
import { animateElementShake } from './components/animations';
import { registerUser } from './components/userRegister.ts';
import { staticPath } from './config';
import StatusMessageBox from './views/MessageBox.vue';

const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

export default defineComponent({
    components: {
        StatusMessageBox
    },
    setup(){
        // View setup
        const email = ref(<string>"");
        const password = ref(<string>"");
        const passwordConfirm = ref(<string>"");
        const statusMessage = ref(<StatusMessage|null>null);
        const enableRegistertration = ref(<boolean>true);
        
        // Asset setup
        const assets: object = reactive({
            haxorLogo: <string>staticPath + 'icons/haxor-logo-only-black.svg',
        });

        // ReCaptcha setup
        const reCaptchaInstance = useReCaptcha();
        async function reCaptcha() {
            await reCaptchaInstance?.recaptchaLoaded();
            return await reCaptchaInstance?.executeRecaptcha("register");
        }

        /**
         * Register user account.
         * 
         * Validates the registration form, checks CAPTCHA, and sends the registration request.
         * Displays status message if registration succeeds or fails.
         * 
         * @param {Event} event 
         * @returns {Promise<void>}
         */
        async function register(event:Event): Promise<void>{
            event.preventDefault();
            const captchaToken = await reCaptcha();

            const registrationSchema: RegistrationSchema = {
                email: email.value,
                password: password.value,
                passwordConfirm: passwordConfirm.value,
                csrfmiddlewaretoken: csrfToken?csrfToken:"",
                captchaToken: captchaToken?captchaToken:"",
            };
            const validationResult: ValidationResult = validateRegistrationSchema(registrationSchema);
            if (!validationResult.success){
                statusMessage.value = validationResult.message;
                animateElementShake("loginAlert");
                return;
            }

            registerUser(registrationSchema)
                .then(data => {
                    statusMessage.value = {
                        type: "success",
                        messageClass: "message--success",
                        text: "Registered! Check your Email to verify your account.",
                    };
                    enableRegistertration.value = false;
                })
                .catch(error => {
                    if(error == "user-exists"){
                        statusMessage.value = {
                            type: "error",
                            messageClass: "message--error",
                            text: "User already exists. Please login.",
                        };
                    }
                    if(error == "invalid-email"){
                        statusMessage.value = {
                            type: "error",
                            messageClass: "message--error",
                            text: "Please enter a valid email address.",
                        };
                    }
                    if(error == "password-mismatch"){
                        statusMessage.value = {
                            type: "error",
                            messageClass: "message--error",
                            text: "Passwords do not match!",
                        };
                    }
                    animateElementShake("loginAlert");
                });
        }

        return {
            assets,
            email,
            password,
            passwordConfirm,
            enableRegistertration,
            statusMessage,
            register,
        }
    }
});
</script>