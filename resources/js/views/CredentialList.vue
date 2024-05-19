<template>
    <div v-if="credentials?.length" class="app-item__content">
        <div class="app-item__credential-wrapper" v-for="credential in credentials" :key="credential.id">
            <button class="button button--icon"
                title="Click to copy username to clipboard"
                @click="copyToClipboard(credential.username, 'button-username-' + credential.id)">
                <img class="button__logo" :src="assets.userLogo" alt="user"
                    :id="'button-username-' + credential.id">
            </button>

            <button class="button button--icon"
            title="Click to copy password to clipboard"    
                @click="copyToClipboard(credential.password, 'button-password-' + credential.id)">
                <img class="button__logo" :src="assets.passwordLogo" alt="password" 
                    :id="'button-password-' + credential.id">
            </button>
            
            <span class="app-item__credential-name">{{ credential?.username }}</span>
            
            <a class="button button--danger button--icon" :href="getCredentialUrl(credential)">
                <img class="button__logo" :src="assets.settingsLogo" alt="edit">
            </a>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, PropType, reactive } from 'vue';
import { staticPath } from '../config.ts';
import { copyToClipboard } from '../components/utils.ts';
import { Credential } from '../components/interfaces.ts';

export default defineComponent({
    props: {
        credentials: {
            type: Array as PropType<Credential[]>,
            required: false
        }
    },
    setup() {
        // Asset setup
        const assets: object = reactive({
            settingsLogo: <string>staticPath + 'icons/settings--white.png',
            userLogo: <string>staticPath + 'icons/user--white.png',
            passwordLogo: <string>staticPath + 'icons/key--white-v3.png',
        });

        /**
         * Get credential URL.
         * 
         * Used when navigating to credential details.
         * @param credential 
         */
        function getCredentialUrl(credential: Credential){
            return "/credential/" + credential.id;
        }

        return {
            assets,
            getCredentialUrl,
            copyToClipboard,
        }
    }
});
</script>