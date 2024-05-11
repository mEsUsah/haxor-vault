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
import axios from 'axios';

const api_host = "http://127.0.0.1:8000";
const api_apps = "/api/v1/apps";

interface Credential{
    app: string,
    id: string,
    password: string,
    username: string,
}

interface AppType{
    id: string,
    name: string,
}

interface App {
    id: string,
    name: string,
    apptype: AppType,
    credentials: Array<Credential|null>,
    user: number

};

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