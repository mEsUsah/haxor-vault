<template>
    <div class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="app.apptype">
                <option value="" disabled>Select type:</option>
                <option v-for="appType in appTypes" :value="appType.id">
                    {{ appType.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="app.name" type="text" name="name" placeholder="Name">
        </div>
        <div class="form__buttons">
            <button 
                :disabled="disableSubmit"
                @click="saveApp"
                type="submit" class="button">Save</button>
            <a href="/dashboard" class="button button--nautral">Cancel</a>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { AppType, AppSchema } from './components/interfaces.ts';
import { getAppTypes } from './components/appTypeCRUD.ts';
import { createApp } from './components/appCRUD.ts';

export default defineComponent({
    setup() {
        const app: AppSchema = reactive({
            name: "",
            apptype: "",
            csrfmiddlewaretoken: csrfToken
        });
        
        const appTypes = ref<AppType[]>();
        const disableSubmit = computed(()=>{
            return app.name == "" || app.apptype == "";
        })
        
        async function getData(): Promise<void>{
            appTypes.value = await getAppTypes();
            console.log(appTypes.value);
        }

        function saveApp(){
            if(!disableSubmit.value){
                createApp(app)
                    .then(result => {
                        console.log(result);
                    })
                    .catch(error=>{
                        console.log(error);
                    });
            }
        }

        onMounted(() => {
            getData(); 
        });

        return {
            app,
            appTypes,
            disableSubmit,
            saveApp,
        }
    }
});
</script>