<template>
    <div>
        <p>hello apps</p>
        <div>
            <div v-for="app in apps">
                <p>{{ app.name }}</p>
            </div>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive } from 'vue';
import {Credential, AppType, App} from './components/interfaces.ts';
import axios from 'axios';

const api_host = "http://127.0.0.1:8000";
const api_apps = "/api/v1/apps";


export default defineComponent({
    setup() {
        const apps = ref<App[]>([]);
        
        function getApps(){
            axios.get(api_host + api_apps, { withCredentials: true })
                .then(response => {
                    if(response.status == 200){
                        apps.value = response.data;
                    }
                });
        }

        onMounted(() => {
            getApps();
        });

        return {
            apps
        }
    },
});
</script>