<template>
    <AppForm
        :newApp="true"
        :appTypes="appTypes"
        @saveApp="saveApp"
    ></AppForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { AppType, AppSchema, App } from './components/interfaces.ts';
import { getAppTypes } from './components/appTypeCRUD.ts';
import { createApp } from './components/appCRUD.ts';
import AppForm from './views/AppForm.vue'

export default defineComponent({
    components: {
        AppForm
    },
    setup() {      
        // View setup
        const appTypes = ref<AppType[]>();
        
        /**
         * Save app.
         * 
         * Redirects to app details page if successfull.
         * 
         * @param {AppSchema} app 
         * @returns {void}
         */
        function saveApp(app: AppSchema){
            createApp(app)
                .then((result: App) => {
                    window.location.href = "/app/" + result.id;
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        /**
         * Get data needed by view.
         * 
         * @returns {Promise<void>}
         */
        async function getData(): Promise<void>{
            appTypes.value = await getAppTypes();
        }

        onMounted(() => {
            getData(); 
        });

        return {
            appTypes,
            saveApp,
        }
    }
});
</script>