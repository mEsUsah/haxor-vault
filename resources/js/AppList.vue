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
                        <a :href="getAppUrl(app)" class="button button--danger">Edit</a>
                    </div>
                    <CredentialList
                        v-if="app.credentials.length > 0"
                        :credentials="app.credentials"
                    ></CredentialList>
                </div>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive } from 'vue';
import { staticPath } from './config.ts';
import { App } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts'
import CredentialList from './views/CredentialList.vue';

export default defineComponent({
    components: {
        CredentialList
    },
    setup() {
        const apps = ref<App[]>([]);
        const assets: object = reactive({
            webLogo: <string>staticPath + 'icons/globe--black.svg',
        });

        function getAppUrl(app: App){
            return `/app/${app.id}`;
        }

        async function getData(): Promise<void>{
            apps.value = await getApps();
        }

        onMounted(() => {
            getData();
        });

        return {
            apps,
            assets,
            getAppUrl,
        }
    },
});
</script>