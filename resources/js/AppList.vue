<template>
    <div>
        <div>
            <div v-for="app in apps">
                <div class="app-item__wrapper">
                    <div class="app-item__headline">
                        <div class="app-item__icon">
                            <img class="button__logo" 
                                :src="assets.webLogo" 
                                alt="user">
                        </div>
                        <span class="app-item__title">{{ app.name }}</span>
                        <a href="#" class="button button--danger">Edit</a>
                    </div>
                    <div v-if="app.credentials.length > 0" class="app-item__content">
                        <div 
                            class="app-item__credential-wrapper"
                            v-for="credential in app.credentials" 
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
                            <button class="button button--danger button--icon">
                                <img class="button__logo" 
                                    :src="assets.settingsLogo" 
                                    alt="edit">
                            </button>
                        </div>
                    </div>
                    <div class="app-item__footer">
                        <a href="#" class="button button--danger">&plus; Add credential</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive } from 'vue';
import { staticPath } from './config';
import { App } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts'
import { decryptApps } from './components/appCrypto.ts'
import { getMasterPassword, copyToClipboard } from './components/utils.ts';

export default defineComponent({
    setup() {
        const password = ref<string>("");
        const apps = ref<App[]>([]);
        const assets: object = reactive({
            settingsLogo: <string>staticPath + 'icons/settings--white.png',
            userLogo: <string>staticPath + 'icons/user--white.png',
            passwordLogo: <string>staticPath + 'icons/key--white-v3.png',
            webLogo: <string>staticPath + 'icons/globe--black.svg',
        });

        async function getData(): Promise<void>{
            password.value = getMasterPassword();
            apps.value = await getApps();
        }

        onMounted(() => {
            getData();
        });

        return {
            apps,
            assets,
            copyToClipboard,
        }
    },
});
</script>