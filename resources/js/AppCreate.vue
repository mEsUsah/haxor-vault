<template>
    <AppForm
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
        const appTypes = ref<AppType[]>();
        
        async function getData(): Promise<void>{
            appTypes.value = await getAppTypes();
        }

        function saveApp(app: AppSchema){
            createApp(app)
                .then(result => {
                    console.log(result);
                })
                .catch(error=>{
                    console.log(error);
                });
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