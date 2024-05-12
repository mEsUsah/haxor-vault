<template>
    <section>
        <div class="section__hedline">
            <h1>{{ app?.name }}</h1>
        </div>
        <hr>
        <AppForm
            :app="app"
            :appTypes="appTypes"
            @saveApp="saveApp">
        </AppForm>
        
    </section>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { getAppTypes } from './components/appTypeCRUD.ts';
import { getApp, updateApp } from './components/appCRUD.ts'
import { App, AppType, AppSchema } from './components/interfaces.ts';
import AppForm from './views/AppForm.vue'

export default defineComponent({
    components: {
        AppForm
    },
    setup() {
        const app = ref<App>()
        const appTypes = ref<AppType[]>();
        
        async function getData(){
            app.value = await getApp(appId);
            console.log(app);
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

        onMounted(()=>{
            getData();
        });

        return {
            app,
            appTypes,
            saveApp
        }
    }
})
</script>