<template>
    <div>
        <p>hello apps</p>
        <div>
            <div v-for="app in apps">
                <ul>
                    <li>{{ app.name }}</li>
                    <ul>
                        <li v-if="app.credentials != null" v-for="credential in app.credentials">
                            {{ credential?.username }}:{{ credential?.password }}
                        </li>
                    </ul>
                </ul>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import axios from 'axios';
import { defineComponent, onMounted, ref } from 'vue';
import { App } from './components/interfaces.ts';
import { decryptAES } from './components/cryptography.ts';

const api_host = "http://127.0.0.1:8000";
const api_apps = "/api/v1/apps";


export default defineComponent({
    setup() {
        const password = ref<string>("");
        const apps = ref<App[]>([]);
        

        /**
         * Get user password from local storage in browser.
         * 
         * Redirects to logout page if not found.
         * @returns password
         */
        function getPassword(): string{
            let password = localStorage.getItem("password");
            if (password){
                return password;
            } else {
                window.location.href = "/logout";
                return "";
            }
        }

        async function getApps(): Promise<App[]>{
            return new Promise((resolve, reject) => {
                axios.get(api_host + api_apps)
                    .then(response => {
                        if(response.status == 200){
                            resolve(response.data);
                        }
                    }).catch(error => {
                        reject('Failed to get apps from the API');
                    });
            }); 
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

        async function getData(): Promise<void>{
            password.value = getPassword();
            apps.value = await getApps();
            apps.value = decryptApps(apps.value, password.value);
        }

        onMounted(() => {
            getData();
        });

        return {
            apps
        }
    },
});
</script>