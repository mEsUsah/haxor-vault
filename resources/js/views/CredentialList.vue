<template>
    <div v-if="credentials?.length" class="app-item__content">
        <div class="app-item__credential-wrapper"
            v-for="credential in credentials" 
            :key="credential.id">
            <button class="button button--icon"
                @click="copyToClipboard(credential.username)">
                <img class="button__logo" 
                    :src="assets.userLogo" 
                    alt="user">
            </button>
            <button class="button button--icon"
            @click="copyToClipboard(credential.password)">
                <img class="button__logo" 
                    :src="assets.passwordLogo" 
                    alt="password">
            </button>
            <span class="app-item__credential-name">{{ credential?.username }}</span>
            <a class="button button--danger button--icon"
                :href="getCredentialUrl(credential)">
                <img class="button__logo" 
                    :src="assets.settingsLogo" 
                    alt="edit">
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
        const assets: object = reactive({
            settingsLogo: <string>staticPath + 'icons/settings--white.png',
            userLogo: <string>staticPath + 'icons/user--white.png',
            passwordLogo: <string>staticPath + 'icons/key--white-v3.png',
        });

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