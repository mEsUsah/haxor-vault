<template>
    <div class="login-section__wrapper">
        <StatusMessageBox 
            v-if="statusMessage"
            :statusMessage>
        </StatusMessageBox>
        <form class="login-form__wrapper">
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
            <button type="submit">Register</button> 
            <div>Already have an account? <a href="/login">Login</a></div>
        </form>
    </div>
</template>
<script lang="ts">

import { defineComponent, reactive, ref } from 'vue';
import StatusMessageBox from './views/MessageBox.vue';
import { staticPath } from './config';
import { animateElementShake } from './components/animations';
import {StatusMessage} from './components/interfaces.ts';

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

        return {
            assets,
            email,
            password,
            passwordConfirm,
            statusMessage,
        }
    }
});
</script>