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
import { decryptAES } from './components/cryptography.ts';
import { getApps } from './components/appCRUD.ts'

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
        

        /**
         * Get master password from local storage in browser.
         * 
         * Redirects to logout page if not found.
         * @returns password
         */
        function getMasterPassword(): string{
            let password = localStorage.getItem("password");
            if (password){
                return password;
            } else {
                window.location.href = "/logout";
                return "";
            }
        }

        /**
         * Decrypts Array of Apps, and credentials found in each app.
         * @param { App[] } encryptedApps - Array of Apps with encrypted name and credentials
         * @param {string} key - Decryption key
         * @returns { App[] } Decrypted Apps
         */
        function decryptApps(encryptedApps:App[], key: string): App[] {
            let decryptedApps:App[] = [];
            encryptedApps.forEach(app => {
                app.name = decryptAES(app.name, key);
                app.credentials.forEach(credential => {
                    credential.username = decryptAES(credential.username, key);
                    credential.password = decryptAES(credential.password, key);
                })
                decryptedApps.push(app);
            });
            return decryptedApps;
        }

        function copyToClipboard(text){
            navigator.clipboard.writeText(text)
                .then(()=>{
                    console.log("copied to clipboard:", text);
                }).catch(error=>{
                    console.log(error);
                })
        }

        async function getData(): Promise<void>{
            password.value = getMasterPassword();
            apps.value = await getApps();
            apps.value = decryptApps(apps.value, password.value);
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