<template>
    <section>
        <div class="section__hedline">
            <h1>{{ app?.name }}</h1>
        </div>
        <hr>
        <AppForm
            :app="app"
            :appTypes="appTypes"
            @saveApp="saveApp"
            @destroyApp="destroyApp">
        </AppForm>
        <div class="app-item__wrapper app-item__wrapper--standalone">
            <CredentialList
                :credentials="app?.credentials"
            ></CredentialList>
            <AppItemFooter
                :app="app"
            ></AppItemFooter>
        </div>
        
    </section>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import { getAppTypes } from './components/appTypeCRUD.ts';
import { getApp, updateApp, deleteApp } from './components/appCRUD.ts'
import { App, AppType, AppSchema } from './components/interfaces.ts';
import AppForm from './views/AppForm.vue'
import CredentialList from './views/CredentialList.vue';
import AppItemFooter from './views/AppItemFooter.vue'

export default defineComponent({
    components: {
        AppForm,
        CredentialList,
        AppItemFooter
    },
    setup() {
        const app = ref<App>()
        const appTypes = ref<AppType[]>();
        
        async function getData(){
            app.value = await getApp(appId);
            appTypes.value = await getAppTypes();
        }

        function saveApp(appSchema: AppSchema){
            updateApp(appId, appSchema)
                .then((result:App) => {
                    app.value = result;
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        function destroyApp(appSchema: AppSchema){
            deleteApp(appId, appSchema)
                .then((result: String) => {
                    window.location.href = "/dashboard";
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        onMounted(()=>{
            getData();
        });

        return {
            app,
            appTypes,
            saveApp,
            destroyApp
        }
    }
})
</script>