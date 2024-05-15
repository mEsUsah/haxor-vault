<template>
    <div class="login-section__wrapper">
        <StatusMessageBox 
            v-if="statusMessage"
            :statusMessage>
        </StatusMessageBox>
        <form @submit="register" class="login-form__wrapper">
            <img class="login-section__logo" 
                :src="assets.haxorLogo" 
                alt="logo">
            <h1>Vault</h1>
            <div class="login-form__input">
                <input type="text" 
                    v-model="email"
                    placeholder="Email">
            </div>
            <div class="login-form__input">
                <input type="password"
                    v-model="password"
                    placeholder="Password">
            </div>
            <div class="login-form__input">
                <input type="password"
                    v-model="passwordConfirm"
                    placeholder="Confirm password">
            </div>
            <button type="submit" :disabled="!enableRegistertration">Register</button> 
            <div>Already have an account? <a href="/login">Login</a></div>
        </form>
    </div>
</template>
<script lang="ts">

import { defineComponent, reactive, ref } from 'vue';
import StatusMessageBox from './views/MessageBox.vue';
import { staticPath } from './config';
import { animateElementShake } from './components/animations';
import {RegistrationSchema, StatusMessage} from './components/interfaces.ts';
import { validateRegistrationSchema } from './components/validateRegistrationSchema.ts';
import { registerUser } from './components/userRegister.ts';
const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

export default defineComponent({
    components: {
        StatusMessageBox
    },
    setup(){
        const assets: object = reactive({
            haxorLogo: <string>staticPath + 'icons/haxor-logo-only-black.svg',
        });
        const email = ref(<string>"");
        const password = ref(<string>"");
        const passwordConfirm = ref(<string>"");
        const statusMessage = ref(<StatusMessage|null>null);
        const enableRegistertration = ref(<boolean>true);

        function register(event:Event): void {
            event.preventDefault();
            
            const registrationSchema: RegistrationSchema = {
                email: email.value,
                password: password.value,
                passwordConfirm: passwordConfirm.value,
                csrfmiddlewaretoken: csrfToken?csrfToken:"",
            };
            const validationResult = validateRegistrationSchema(registrationSchema);
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
                        text: "Registered! Check your Email to verify your account",
                    };
                    enableRegistertration.value = false;
                })
                .catch(error => {
                    if(error == "user-exists"){
                        statusMessage.value = {
                            type: "error",
                            messageClass: "message--error",
                            text: "User already exists!",
                        };
                        animateElementShake("loginAlert");
                    }
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