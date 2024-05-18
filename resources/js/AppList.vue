<template>
    <div>
        <div class="search__wrapper">
            <div class="form__field">
                <input v-model="search" type="text" name="name" placeholder="Search">
            </div>
        </div>
        <div v-for="app in filteredApps">
            <div class="app-item__wrapper">
                <div class="app-item__headline">
                    <div class="app-item__headline-text">
                        <div class="app-item__icon">
                            <img v-if="app.apptype.name == 'Website'" class="app-item__icon-img--web" 
                                :src="assets.webLogo" 
                                alt="user">
                            <img v-if="app.apptype.name == 'Game'" class="app-item__icon-img--game" 
                                :src="assets.gameLogo" 
                                alt="user">
                            <img v-if="app.apptype.name == 'Mobile app'" class="app-item__icon-img--mobile" 
                                :src="assets.mobileLogo" 
                                alt="user">
                        </div>
                        <span class="app-item__title">{{ app.name }}</span>
                    </div>
                    <a :href="getAppUrl(app)" class="button button--danger">Edit</a>
                </div>
                <CredentialList
                    :credentials="app.credentials"
                ></CredentialList>
                <AppItemFooter
                    :app="app"
                ></AppItemFooter>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { staticPath } from './config.ts';
import { App } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts'
import CredentialList from './views/CredentialList.vue';
import AppItemFooter from './views/AppItemFooter.vue'

export default defineComponent({
    components: {
        CredentialList,
        AppItemFooter
    },
    setup() {
        const apps = ref<App[]>([]);
        const assets: object = reactive({
            webLogo: <string>staticPath + 'icons/globe--black.svg',
            gameLogo: <string>staticPath + 'icons/game--black.png',
            mobileLogo: <string>staticPath + 'icons/mobile--black.png',
        });
        const search = ref<string>('');

        function getAppUrl(app: App){
            return `/app/${app.id}`;
        }

        const filteredApps = computed(() => {
            return apps.value.filter(app => app.name.toLowerCase().includes(search.value.toLowerCase()));
        });

        async function getData(): Promise<void>{
            apps.value = await getApps();
        }

        onMounted(() => {
            getData();
        });

        return {
            apps,
            assets,
            search,
            filteredApps,
            getAppUrl,
        }
    },
});
</script>